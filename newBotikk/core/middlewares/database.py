import sqlite3 as sq

db = sq.connect('C:/Users/Alexey/PycharmProjects/newBotikk/data.sqlite')

cur = db.cursor()
cur.execute('SELECT id_day,id_grup,id_predmets,lessonsNamber,id_prepod,cab FROM `raspisanie` WHERE id_grup = "3" AND id_day == "1"')
fourteenth_gr = cur.fetchall()
infogrp = ''
#for el in users:
#    info += f"Имя {el[1]}, пароль: {el[2]}\n"
for raspis in fourteenth_gr:
    day = f"{raspis[0]}"
    if day == '1':
        print("Понедельник: ")
        break
    if day == '2':
        print("Вторник")
        break
    if day == '3':
        print("Среда")
        break
    if day == '4':
        print("Четверг")
        break
    if day == '5':
        print("Пятница")
        break
    if day == '6':
        print("Суббота")
        break




for raspis in fourteenth_gr:

    day = f"{raspis[0]}"
    infogrp = f"Айди предмета: {raspis[2]}\nНомер урока: {raspis[3]}\nАйди препода: {raspis[4]}\nКабинет: {raspis[5]}\n" #Давай заебал, завтра садись и пиши уебок
    print(infogrp)



cur.close()


db.close()




# ps = db.cursor()
# ps.execute('SELECT password FROM `user_create` WHERE password = "123"')
# passwords = ps.fetchall()
# infopsw = ''
# for el in users:
#    info += f"Имя {el[1]}, пароль: {el[2]}\n"
# for psw in passwords:
#    infopsw = f"пароль: {psw[0]}\n"
#    print(infopsw)


# ps.close()


# db.close()