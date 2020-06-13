import telebot
import mysql.connector

import mytoken


from datetime import datetime
TOKEN=mytoken.TOKEN
mybot = telebot.TeleBot(TOKEN)
myDb=mysql.connector.connect(host='localhost',user='root',database='db_belajarbot')
sql=myDb.cursor()
from telebot import apihelper
waktusekarang=datetime.now()

class Mybot:
    def __init__(self):
        self.message

    @mybot.message_handler(commands=['start', 'help'])
    def start(message):
        # photo = open('img/rpl.jpg', 'rb')
        # myBot.send_photo(message.from_user.id, photo)
        teks = mytoken.SAPA + "\n-- admin @yashinta fazrin - murid SMK Taruna Bhakti -- "+"\n" \
                        " Hari ini tanggal "+str(waktusekarang)
        mybot.reply_to(message, teks)

    @mybot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "SELECT `nipd`,`nama`,`kelas` FROM `tabel_siswa` "
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata=''
        if(jmldata>0):
            #print(data)
            # no=0
            for x in data:
                # no += 1
                kumpuldata = kumpuldata+ str(x) + '\n'
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(', '')
                kumpuldata = kumpuldata.replace(')', '')
                kumpuldata = kumpuldata.replace("'", '')
                kumpuldata = kumpuldata.replace(",", '')
        else:
            print('data kosong')

        mybot.reply_to(message,str(kumpuldata))

print(myDb)
print("-- Bot sedang berjalan --")
mybot.polling(none_stop=True)
