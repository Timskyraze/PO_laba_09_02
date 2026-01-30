# Лабораторная работа 9: Интеграция автотестов в CI/CD

## Описание
Проект демонстрирует интеграцию автоматических тестов в CI/CD пайплайн с использованием GitHub Actions.

## Структура проекта
- `calculator.py` - класс Calculator с математическими операциями
- `test_calculator.py` - автотесты с использованием pytest
- `requirements.txt` - зависимости Python
- `.github/workflows/run-tests.yml` - конфигурация GitHub Actions

## Запуск тестов локально
```bash
pip install -r requirements.txt
pytest test_calculator.py -v