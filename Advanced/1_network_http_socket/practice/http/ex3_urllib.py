from urllib import request

response = request.urlopen('https://example.com/')

print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)
# получаем заголовки в виде внутреннего обьекта
print(response.headers)
# получаем словарь всех заголовков
print(response.getheaders())
# получение заголовка
print(response.headers.get('Content-Type'))
print(response.getheader('Content-Type'))

# но есть более удобная библиотека, которая реализует в себе все методы http протокола

