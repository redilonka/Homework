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
