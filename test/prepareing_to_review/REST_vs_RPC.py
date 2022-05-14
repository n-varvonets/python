# API - програмный интерфейс для общения компонентов программы друг с другом. Клиент - сервер, в вебе - это общенгие фронта с \
# беком или два бэка между собой. Есть два типа API - это REST и RPC. REST - хорошо кешируемый и не содержит состояние клиента. \
# Т.е. ни сервер ни клиент не знает о состоянии друг друга. В таких API мы напрямую управляем обьектами подобно файловой системе.\
# У таких обьектов есть своя иерархия(структура) - подобно файлам с папками. Например, мы делаем интернет магаз и у нас есть товар
# и мы с ним можем совершать различные действия: доавбить товар в корзину, удалить из ней, переимновать товар, посмотреть\
# описание, цену и прочее...


# REST(repr state transfer) - архитектурный стиль, который описывает то как различные программы могут общаться между собой и \
# представляет собой набор ограничений и требований. Архитектурный стиль - некий шаблон, по которому мы можем построить наше \
# приложение. Если мы построим наше приложение по этому шаблону, тогда это будет RESTful приложение. Клиент(для рест это
# программа) обращается на сервер и получает ответ. REST то альтернатива RPC(remote procedure call) - удаленный вызов процедур, \
# т.е. через одну программу вызываем функцию удаленно на другом компе и получаем результат её работы.
# Т.е. REST это рекомендации, которые говорят использовать в себе стандарты http, url, json, html.
# SOAP - это уже четкий стандарт(протокол, а не рекомендации) обмена СТРУКТУРИРОВАННЫМИ смс(ТОЛЬКО XML), которые, в том числе
# могут вызывать функции или целые скрипты на сервере. Т.е. фактически мы вызываем функцию с набором аргументов и получаем
# результат. SOAP неудобно читать и сообщения очень большие что негативно сказывается на трафике. WSDL схема описывает доступные
# функции на сервер и параметры.
#
#  ТРЕБОВАНИЕ RESTful API:
# 1) client-server -  т.е. общение происходит отдельно между клиентом и отдельно между сервером. Плюсы:
#   - это то что клиенты не связаны с хранением данных, которые есть на сервер. Т.е. сервер имеет все данные, а наши клиенты
# просто запрашивают её.
#   - т.к. они сервер не связан с интерфейсом клиента(его состоянием-сессией), то сервер знает что клиент будет приходить за
# инфой, А НЕ сервер будет распределять её по клиентам. Сервер - главное звена, а все клиенты обращаются за инфой к нему.
# 2) Stateless. ервер не должен хранить какой-либо инфы о клиентах. Т.е. у нас НЕТ логина и пароля, а если нужна индетификация,
# то используем сгенерируемый токен(api_key).
# 3)Cache. Ответ должен иметь отметку - является ли он кешируемым, для предотвращения использования клиентами устаревших данных.
# 4) Uniform Interface. Единый интерфейс, т.е. - это взаимодействия между клиентом и сервером, которое \
# позволяет развиваться независимо друг от друга, пока сервер не обновит это правило. Т.е. клиент может создать другой фронт, но\
# при этому работая с нашими данными. Принципы:
#   - Ресурсом(обьектом) является все то, чему можно дать имя(пользователь, изображение, предмет(майка, погода)), который не \
# должен меняться при изменинии состояния ресурса. Ресурс идентифицируется с URI. Например, у нас есть ресурс(обьект) погода с \
# соответсвующий URL и наш URL не должен меняться при изменении погоды.
#   - Манипуляция над ресурсами должна происходить через представления. Представление(использовать  view и/или url) - это \
# текущее(get) или желаемое(create, delete, update) состояние ресурса(собаки, погоды, пользователя, товара). Т.е. если ресурс это\
# погода, то с помощью представления мы можем создать запись о погоде, обновить некоторую инфу о погоде, удалить и т.д.
#   - *! НЕ должно быть доп.сообщений или кеша для обработки ОДНОГО запроса. Т.е. ОТСУТСТВИЕ  состояния, сохраняемого между
#  запросами к ресурсам. Т.е. когда мы делаем запрос к сервису, примаемы сервис должен видеть это как ПЕРВЫЙ запрос(хоть даже
#  если есть слои). Нас сервис НЕ ДОЛЖЕн хранить какой это запрос и ЧТО БЫЛО ДО ЭТОГО. Это важно для масштабирования \
#  системы(создания новых функций в текущем сервисе).
# 5) Layered System. Можно разделять слои, т.е. если есть наш клиент-сервер и сервер вызывает другой сервер, но с условием, что \
# каждый сервер может видеть компоненты только следующие слоя(не глубже, но труднее дебажить). Например, мы вызываем сервис \
# PayPal, который вызывает сервис Visa, но клиент ничего не должен знать об Visa.
#
# ПРЕИМУЩЕСТВА RESTFful API: (restful сервис должен иметь все это, иначе это не restful)
# - Надежность(за счет отсутвия сохранения инфы о клиенте)
# - Производительность (за счет использования кеша, если одинаковые запросы(дай ссылку на это видео), то можно их кешировать)
# - Масштабируемость(за счет разделения интерфйсов сервера и клиента, может развивать наш сервер отдельно, при этом не ламая
# работу клиент-сервера).Т.е. клиент может обращаться на свой url, который ему нужно, но при этом может добавлять \
# новые функционал(новые url)
# - Прозрачность системы взаимодействия(есть только клиент и сервер, никаких третьих сторон)
# - Простота интерфейсов(один интерфейс через http протокол, запрос - ответ)
# - Портативность компонентов(работа сервера не заточена под одного клиента, т.е если появятся другие клиенты, то - ок)
# - легкость внесения изменений(если фронт-енд сделан под наш сервер и появится другой фронт, который захочет кастомизировать, то
# не придется влезать на наш сервер и полностью переписывать свой фронт, как это с обычным django)
#


