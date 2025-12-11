# CI/CD Demo Project

[![CI Pipeline](https://github.com/florell/ci-cd-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/florell/ci-cd-demo/actions/workflows/ci.yml)
[![CD Pipeline](https://github.com/florell/ci-cd-demo/actions/workflows/cd.yml/badge.svg)](https://github.com/florell/ci-cd-demo/actions/workflows/cd.yml)

Демонстрационный проект с настроенными CI/CD пайплайнами.

## Содержание

- [Описание](#описание)
- [CI Pipeline](#ci-pipeline-статический-анализ-и-тесты)
- [CD Pipeline](#cd-pipeline-сборка-и-публикация-docker)
- [Настройка](#настройка)
- [Локальный запуск](#локальный-запуск)

## Описание

Простое Flask REST API приложение с полностью настроенными CI/CD пайплайнами для GitHub Actions и GitLab CI/CD.

### API Endpoints

| Endpoint | Метод | Описание |
|----------|-------|----------|
| `/` | GET | Главная страница с информацией об API |
| `/health` | GET | Health check |
| `/api/sum/<a>/<b>` | GET | Сумма двух чисел |
| `/api/factorial/<n>` | GET | Факториал числа |

## CI Pipeline 

### Инструменты статического анализа:

- **Black** - форматирование кода
- **isort** - сортировка импортов
- **flake8** - проверка стиля кода
- **pylint** - расширенный линтинг
- **mypy** - проверка типов
- **bandit** - проверка безопасности

### Тестирование:

- **pytest** - запуск unit тестов
- **pytest-cov** - покрытие кода тестами
- Матрица тестирования: Python 3.10, 3.11, 3.12

### Запуск пайплайна:

```
Push в ветку main/develop -> Автоматический запуск CI
Pull Request в main -> Автоматический запуск CI
```

## CD Pipeline

### Функции:

- Сборка мультиархитектурного Docker образа (amd64, arm64)
- Публикация в Docker Hub
- Автоматическое тегирование (latest, sha, semver)
- Кэширование слоёв для ускорения сборки

### Запуск пайплайна:

```
Push в main -> Автоматическая сборка и публикация
Push тега v* -> Релизная версия
Manual trigger -> Ручной запуск с кастомным тегом
```

## Настройка

### GitHub Actions

1. Создайте репозиторий на GitHub
2. Настройте секреты в Settings -> Secrets and variables -> Actions:

| Секрет | Описание |
|--------|----------|
| `DOCKERHUB_USERNAME` | Ваш username на Docker Hub |
| `DOCKERHUB_TOKEN` | Access Token от Docker Hub |

3. Push код в репозиторий

### GitLab CI/CD

1. Создайте репозиторий на GitLab
2. Настройте переменные в Settings -> CI/CD -> Variables:

| Переменная | Описание |
|------------|----------|
| `DOCKERHUB_USERNAME` | Ваш username на Docker Hub |
| `DOCKERHUB_TOKEN` | Access Token от Docker Hub |

3. Push код в репозиторий

### Создание Docker Hub Access Token

1. Войдите на [hub.docker.com](https://hub.docker.com)
2. Account Settings -> Security -> New Access Token
3. Дайте имя токену и выберите права (Read, Write)
4. Скопируйте токен и добавьте в секреты

## Локальный запуск

### С Python

```bash
# создание виртуального окружения
python -m venv venv
source venv/bin/activate  # linux/mac
# или
venv\Scripts\activate  # windows

# установка зависимостей
pip install -r requirements-dev.txt

# запуск тестов
pytest tests/ -v --cov=app

# запуск линтеров
black --check app/ tests/
flake8 app/ tests/
pylint app/

# запуск приложения
python -m app.main
```

### С Docker

```bash
# сборка образа
docker build -t ci-cd-demo:local .

# запуск контейнера
docker run -d -p 5000:5000 --name ci-cd-demo ci-cd-demo:local

# проверка
curl http://localhost:5000/health

# остановка
docker stop ci-cd-demo && docker rm ci-cd-demo
```

### Pull из Docker Hub

```bash
# после успешного CD пайплайна
docker pull florell/ci-cd-demo:latest
docker run -d -p 5000:5000 YOUR_USERNAME/ci-cd-demo:latest
```

## Результаты

### GitHub Actions
- CI Pipeline: `https://github.com/florell/ci-cd-demo/actions/workflows/ci.yml`
- CD Pipeline: `https://github.com/florell/ci-cd-demo/actions/workflows/cd.yml`

### GitLab CI/CD
- Pipelines: `https://github.com/florell/ci-cd-demo/actions`

### Docker Hub
- Registry: `https://hub.docker.com/r/florell/ci-cd-demo`

## Лицензия

MIT License
