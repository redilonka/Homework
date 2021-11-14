Echo server
---

- сервер не завершает работу после ответа клиенту
- сервер корректно обрабатывает некорректный статус
- сервер возвращает заголовки запроса в виде ответа

![Alt text](../images/status_202.png?raw=true "Status 202")
![Alt text](../images/bad_status.png?raw=true "Bad Status")

How to test:
- python echo_server/app.py
- open http://localhost:8080/?status=202
- open http://localhost:8080/?status=bad_status
- curl http://localhost:8080/\?status\=bad_status
```
<ul><li>Request Method: GET</li><li>Request Source: ('127.0.0.1', 49643)</li><li>Response Status: 200 OK</li><li>Host: localhost:8080</li><li>User-Agent: curl/7.77.0</li><li>Accept: */*</li></ul>%
```
