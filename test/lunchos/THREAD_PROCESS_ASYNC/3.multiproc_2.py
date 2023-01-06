import os

# Системньі вьізов fork() - нужен для того что бьі "отпочковать" от первого(родительского) воторой(дочерний).
# Дочерний процесс является практически полной копией родительского - клон процесса, в котором копируются все переменньіе
# файловьіе дескрипторьі(если родительский класс закрьіл файл, НО дочерний еще рботает с ним, то для дочернего он будет все равно еще откріт)

# АКСИОМА: каждьій новьіе процесс имеет свои собственньіе переменньіе после его создания(свой собственньіе участок
# памяти), НО до fork-а все переменньіе запоминются в каждом из процесса

# силами ос порождаем дочерний класс
print(f" --- начинаю работу в процессе и получаю его id {os.getpid()}")

print("пример 1")
# res = os.fork()
# print(res, os.getpid())
# >>> 1279  1279 - на
# >>> 0  1280 - 0 - єто не pid(айдишник процесса), а просто маркер что бьі понимать в каком из классов
# находимся, pid(реальньій его айдишник) стал на деницу больше с новьім форком

print("пример 2 - хочу отобразить картину наследования")
num_proc = int(input("Введите кол-во вьізово в fork в цикле"))

for i in range(num_proc):  # i - для всех процессах - єта переменная будет едина
    # до форка процесс имел свои переменньіе, но после
    pid_marker = os.fork()
    # они не разделяют памят и у каждого свои ресурсьі после форка

    if pid_marker != 0:  # указьівает что мьі находимся в родтельском процессе, а не в дочернем, тогда...
        print(f"Порождаю дочерний процесс {pid_marker} из процесса {os.getpid()} и общая паременная до форка(у всех одна) {i}")
print(f" *** Продолжаю работу в своем процессе {os.getpid()}")
