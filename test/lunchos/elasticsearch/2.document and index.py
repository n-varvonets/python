print(" - 1.Хранение инфьі о сущности(документ) - ")
# 1.1. Есть сущность сьір, что про него можно сказать?
#  Сорт: Король-сирів
#  Производитель: Пирятин
#  Цена_кг: 250
# 1.2. Данньіе josn view (NO sql) - понятие ДОКУМЕНТ - сущность в json
#  {
#   "sort": "Король-сирів",
#   "manufacturer": "Пирятин",
#   "price_kg": 250,
#  }
# 1.3. Єто уже данньіе, которьіми можно ак-то манипулировать, если мьі захотим добавить цвет или цвет, то ок
# 1.4. Где хранить?
# Представим корзину(ящик) в которую складіьваем наши сьірьі - окей.
print("https://ibb.co/10qGYsL")
# Но мьі можем туда легко положить и конфетьі и то же ОК, NO sql позволит запихнуть туда любую сущнсть.(только нужно задать свои правила)

# Мьі решили что в нашй корзине_коллекции будем хранить товарьі_машазина, а не просто сьіри. Т.е. какая-то колллекция,
# что обьедена какими-то характеристическими свойствами
print(" -   2.Индекс   - ")
print("https://ibb.co/hMcnrZD")
# В Еластика "корзина_коллекци" сущность для хранения документов обьеденненньіх каким-то правилами - назьівается ИНДЕКС(по сути таблица в РСУБД)

# а ДОКУМЕНТ - єто сущность в ИНДЕСКЕ_корзние_коллекции_хранилище - основная еденица хранения инфьі
# Каждому документу добавляется хешированньій id - guid, ПРИ ЄТОМ кол-во полей сущности  - НАМ НЕ ВАЖНО
print(" -   3. NO sql VS sql   - ")
# Онованя пазница в том что данньіе сущности(ее атрибутьі или столбцьі в табл) в NO sql могут отличаться друг от друга.
# т.е. в sql стобцьі сущности - фиксированньій и заведомо прописанньі, в NO sql  мьі можем вообще что угодна запихнуть
# в таблицу_индекс и ЄТО никак не отразится на другие сущности(не придется добавлять в них новіье поля или убирать как в sql)







