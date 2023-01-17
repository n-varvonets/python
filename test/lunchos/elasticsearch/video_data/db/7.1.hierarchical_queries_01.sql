CREATE TABLE Sotrudniki (
   ID         NUMBER PRIMARY KEY,
   FIO        VARCHAR(100),
   BossID     NUMBER,
   StatusName VARCHAR(100)
);

insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (1,'Главный Алексей Георгиевич',NULL,'Генеральный директор');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (2,'Задумчивая Людмила Анатольевна',1,'Главный бухгалтер');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (3,'Скоробогатый Антон Васильевич',1,'Директор по продажам');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (4,'Праворукий Петр Иванович',1,'Директор отдела ИТ');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (5,'Кувалдин Анатолий Андреевич',3,'Менеджер');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (6,'Дебет Ольга Васильевна',2,'Бухгалтер');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (7,'Кредитная Марина Павловна',2,'Бухгалтер');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (8,'Балансная Инна Ивановна',2,'Бухгалтер');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (9,'Стобухина Людмила Прокофьевна',3,'Менеджер');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (10,'Мегастар Олег Павлович',3,'Менеджер');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (11,'Продамручку Джон Иванович',3,'Менеджер');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (12,'Дискретный Дмитрий Константинович',4,'Программист');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (13,'Двойнов Руслан Михайлович',4,'Инженер');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (14,'Формат Константин Борисович',4,'Инженер');
insert into Sotrudniki (ID,FIO,BossID,StatusName) VALUES (15,'Тестовый Максим Эдуардович',4,'Программист');

COMMIT;


