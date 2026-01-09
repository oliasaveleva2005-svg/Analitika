Weather Data Pipeline — это полноценный пайплайн данных для сбора, хранения, анализа и визуализации погодных метрик в реальном времени. Проект демонстрирует навыки работы с современным стеком Data Engineering: от генерации данных до создания интерактивных дашбордов.
End-to-end система для сбора, хранения, визуализации и анализа метеорологических данных в реальном времени.

Архитектура Docker-контейнеров
1 Сбор и анализ данных
- **data-generator/** - генератор реалистичных погодных данных
- **database/** - PostgreSQL для хранения данных  
- **notebooks/** - Jupyter Notebook для анализа

2 Настройка визуализации
- **setup-master/** - автоматическая настройка Redash
- Настройка источников данных
- Конфигурация дашбордов
- Импорт запросов

Структура проекта
── setup-master/            # Контейнер 2: Настройка Redash
│   ├── Dockerfile          # Конфигурация контейнера настройки
│   ├── setup.sh           # Скрипт автоматической настройки
│   ├── requirements.txt   # Зависимости Python для настройки
│   └── config/            # Конфигурационные файлы Redash
weather-data-pipeline/
├── data-generator/           # Генератор погодных данных
│   ├── Dockerfile           # Конфигурация контейнера
│   ├── requirements.txt     # Зависимости Python
│   └── weather_generator.py # Основной скрипт генерации
├── database/                # База данных
│   └── init.sql            # SQL для создания таблиц
├── notebooks/              # Jupyter Notebooks
│   └── weather_analysis.ipynb # Анализ с графиками
├── docker-compose.yml      # Оркестрация контейнеров
├── README.md              # Документация
└── .gitignore             # Исключения Git


Быстрый старт
Клонируем репозиторий
git clone https://github.com/oliasaveleva2005-svg/Analitika.git
cd Analitika

*Закрыть перед запуском*(Остановливаем предыдущие запуски)
docker-compose down

Запуск системы
docker-compose up -d

Проверка запуска
docker-compose ps

Проверка, что данные генерируются
docker-compose exec postgres psql -U postgres -d weather_db -c "SELECT COUNT(*) FROM weather_metrics;"

Открывыем в браузере:
# Redash: http://localhost:5000
# Jupyter: http://localhost:8888