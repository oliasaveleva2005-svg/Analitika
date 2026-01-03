import time
import random
from datetime import datetime
import psycopg2
import os

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'postgres'),
        database=os.getenv('DB_NAME', 'weather_db'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'password'),
        port=5432
    )

def generate_weather_data():
    hour = datetime.now().hour
    
    if 0 <= hour < 6:
        base_temp = 10
    elif 6 <= hour < 12:
        base_temp = 15
    elif 12 <= hour < 18:
        base_temp = 22
    else:
        base_temp = 18
    
    temp = round(base_temp + random.uniform(-3, 3), 1)
    humidity = random.randint(40, 90)
    pressure = random.randint(980, 1030)
    wind_speed = round(random.uniform(0, 10), 1)
    
    conditions = ['clear', 'cloudy', 'partly_cloudy', 'rain', 'fog']
    condition = random.choice(conditions)
    
    return temp, humidity, pressure, wind_speed, condition

def main():
    print("Starting weather data generator...")
    time.sleep(10)
    
    while True:
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            temp, humidity, pressure, wind_speed, condition = generate_weather_data()
            
            cursor.execute("""
                INSERT INTO weather_metrics 
                (temperature_c, humidity_percent, pressure_hpa, wind_speed_ms, weather_condition)
                VALUES (%s, %s, %s, %s, %s)
            """, (temp, humidity, pressure, wind_speed, condition))
            
            conn.commit()
            cursor.close()
            conn.close()
            
            print(f"{datetime.now().strftime('%H:%M:%S')} | "
                  f"Temp: {temp}C | Hum: {humidity}% | "
                  f"Press: {pressure}hPa | Wind: {wind_speed}m/s | "
                  f"Cond: {condition}")
            
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(5)

if __name__ == "__main__":
    main()