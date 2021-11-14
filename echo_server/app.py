"""
Echo server app.

Ваш сервер должен принимать запрос от клиента и отправлять ему:

заголовки, которые получил в запросе
метод, которым был сделан запрос
выставлять статус, который передал клиент в GET параметре status (т.е. если передали /?status=404 то ответ будет со статусом 404) если параметр не передан или не валидный то отдавать 200, если значение
(опционально) сервер не должен прекращать работу после ответа клиенту, а продолжать ожидать следующего соединения
Заголовки должны отображаться на странице в виде строк текста:

Request Method: GET
Request Source: ('127.0.0.1', 47296)
Response Status: 200 OK
header-name: header-value
header-name: header-value
"""

import socket
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs

HOST = ""
PORT = 8080
CLRF = b'\r\n'

class InvalidRequest(Exception):
    pass


class Request:

    _MAP = {str(status.value): status for status in HTTPStatus}

    def __init__(self, raw_request):
        self._raw_request = raw_request.decode('utf-8')
        self._method, self._path, self._protocol, self._headers, self._status = self.parse_request()

    @property
    def status(self):
        return self._MAP.get(self._status, HTTPStatus.OK)

    def parse_request(self):

        temp = [i.strip() for i in self._raw_request.splitlines()]

        if -1 == temp[0].find('HTTP'):
            raise InvalidRequest('Incorrect Protocol')

        method, path, protocol = [i.strip() for i in temp[0].split()]

        status = None
        if status := parse_qs(urlparse(path).query)['status']:
            status = status[0]

        headers = {}
        for k, v in [i.split(':', 1) for i in temp[1:-1]]:
            headers[k.strip()] = v.strip()

        return method, path, protocol, headers, status

    def __repr__(self):
        return repr({
            'method': self._method,
            'path': self._path,
            'protocol': self._protocol,
            'headers': self._headers,
            'status': self._status
        })


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)

        while True:
            conn, addr = s.accept()

            with conn:
                data = conn.recv(1024)

                if not data:
                    break

                try:
                    request = Request(data)
                except InvalidRequest:
                    break

                conn.send(f'HTTP/1.0 {request.status.value} {request.status.phrase}'.encode())
                conn.send(CLRF)
                conn.send(b'Content-Type: text/html' + CLRF*2)

                # Can't use jinja2 due to requirements to use only standart library
                response_string = ""
                response_string += f"<li>Request Method: {request._method}</li>"
                response_string += f"<li>Request Source: {addr}</li>"
                response_string += f"<li>Response Status: {request.status.value} {request.status.phrase}</li>"

                for key, value in request._headers.items():
                    response_string += (f"<li>{key}: {value}</li>")

                response_string = "<ul>" + response_string + "</ul>"

                conn.sendall(response_string.encode())
