from urllib import request

response = request.urlopen('http://example.com')

print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)

# получаем заголовки в виде внутреннего обьекта
print(response.headers)

# получаем словарь всех заголовков. (просто в виде словаря)
print(response.getheaders())

# получение заголовка
print(response.headers.get('Content-Type'))
print(response.getheader('Content-Type'))
