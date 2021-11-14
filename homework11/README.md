OS work
===

Цель
---
Попрактиковаться в работе с процессами ОС Linux

Для выполнения задания нужно написать парсер системных процессов команды 'ps aux' на языке Python с использованием стандартной библиотеки и модуля subprocess.
Парсер должен вывести в стандартный вывод в качестве результата работы следующую информацию (все цифры и данные для примера):

Отчёт о состоянии системы:
Пользователи системы: 'root', 'user1', ...
Процессов запущено: 833

Пользовательских процессов:
root: 533
user1: 231
...

Всего памяти используется: 553.3 mb
Всего CPU используется: 33.2%
Больше всего памяти использует: (%имя процесса, первые 20 символов если оно длиннее)
Больше всего CPU использует: (%имя процесса, первые 20 символов если оно длиннее)

Так же этот отчёт должен быть сохранён в отдельный txt файл с названием текущей даты и времени проверки.
Например, 10-12-2021-12:15-scan.txt


How to test
---
```
(.venv) ➜  Homework git:(homework11) ✗ python homework11/app.py
Отчёт о состоянии системы:
Пользователи системы: redilonka, root
Процесcов запущено: 597

Пользовательских процессов:
redilonka: 414
root: 116

Всего памяти используется: 7389.2 mb
Всего CPU используется: 273.3%
Больше всего памяти использует: com.docker.hyperkit
Больше всего CPU использует: softwareupdated
```