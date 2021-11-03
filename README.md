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
