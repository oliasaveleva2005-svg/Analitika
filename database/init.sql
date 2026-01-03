CREATE TABLE IF NOT EXISTS weather_metrics (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature_c DECIMAL(4,2),
    humidity_percent INTEGER,
    pressure_hpa INTEGER,
    wind_speed_ms DECIMAL(4,2),
    weather_condition VARCHAR(50)
);