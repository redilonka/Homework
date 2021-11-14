# Homework
pythonの授業を出席しています。 このリポジトリは宿題についてがあります。


Homework 4
---

How to test:

```
> python -m homework4.books
> cat homework4/result.json
```


Homework 6 and 7
---

How to test

```
> OPENCART_PORT=8081 PHPADMIN_PORT=8888 LOCAL_IP=$(ipconfig getifaddr en0) docker compose -f opencart.yml up -d
> pytest homework6/test_opencart.py
```


Homework 8
---

Что было сделано:
- добавлен и сконфигурирован логер
- использовано логирование в тестах, фикстуре, page objects и в элементах
- добавлены репорты allure
- использованы анноации, северити
- запуущен Selenoid
- запущены тесты в двух браузерах (Chrome и Firefox)
- добавленна возможность запуска удаленного исполнителя или лоального драйвера

![Alt text](images/chrome.png?raw=true "Chrome")
![Alt text](images/firefox.png?raw=true "Firefox")
![Alt text](images/allure.png?raw=true "Allure")


P.S.
- с удаленным селеноидом произведен запуск тестов на demo.opencart.com, где обнаружена версточная бага с отсутствующим сообщением в корзине
- также там отсутствует возможность добавлять и удалять пользователей, что и показано в отчете Allure


Homework 10
---

Echo server:
- сервер не завершает работу после ответа клиенту
- сервер корректно обрабатывает некорректный статус
- сервер возвращает заголовки запроса в виде ответа

![Alt text](images/status_202.png?raw=true "Status 202")
![Alt text](images/bad_status.png?raw=true "Bad Status")

How to test:
- python echo_server/app.py
- open http://localhost:8080/?status=202
- open http://localhost:8080/?status=bad_status
- curl http://localhost:8080/\?status\=bad_status
```
<ul><li>Request Method: GET</li><li>Request Source: ('127.0.0.1', 49643)</li><li>Response Status: 200 OK</li><li>Host: localhost:8080</li><li>User-Agent: curl/7.77.0</li><li>Accept: */*</li></ul>%
```

Homework 12
---

How to test:

```bash
OPENCART_PORT=8081 PHPADMIN_PORT=8888 LOCAL_IP=$(ipconfig getifaddr en0) docker compose -f opencart.yml up -d
docker compose run opencart_e2e --url=http://$(ipconfig getifaddr en0):8081 --executor=chrome-standalone --bversion=95.0

+] Running 2/0
 ⠿ Container chrome-standalone   Running                                                                                        0.0s
 ⠿ Container firefox-standalone  Running                                                                                        0.0s
================= test session starts =====================
platform linux -- Python 3.8.10, pytest-6.2.4, py-1.11.0, pluggy-0.13.1
rootdir: /app, configfile: pytest.ini
plugins: allure-pytest-2.9.45
collected 11 items

homework6/test_opencart.py ...........                                                                                         [100%]

============= 11 passed, 5 warnings in 24.86s ============
```