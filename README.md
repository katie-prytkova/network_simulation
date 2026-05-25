# Network Simulation

## Описание

Проект моделирует работу сетевого оборудования.
Реализованы:

- базовый класс `NetworkDevice`
- класс `Router`
- класс `Switch`
- автоматические тесты с использованием pyATS

---

## Требования

* Python 3.10+
* pip
* WSL (Windows Subsystem for Linux) для Windows

---

## Установка

Запуск на Windows через WSL

```powershell
wsl
```

Клонирование проекта

```bash
git clone <repository_url>
cd network_simulation
```

Создание виртуального окружения:

```bash
python3 -m venv venv
```

Активация виртуального окружения:

```bash
source venv/bin/activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Запуск программы:

```bash
python main.py
```

Запуск тестов:

```bash
pyats run job run_tests.py
```

---

## Реализованный функционал

### NetworkDevice

* включение устройства
* выключение устройства
* получение информации об устройстве

### Router

* добавление маршрутов
* удаление маршрутов
* вывод таблицы маршрутизации

### Switch

* создание VLAN
* удаление VLAN
* вывод информации о VLAN

---
