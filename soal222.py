#Anda diminta untuk mencari seluruh teks yang berupa email dan kemudian ambil semua username dari
#email tersebut untuk digenerate password random 8 karakter yang terdiri dari angka dan huruf.
#Contoh:
#Berikut adalah daftar email dan nama pengguna dari mailing list:
# anton@mail.com dimiliki oleh antonius
# budi@gmail.co.id dimiliki oleh budi anwari
# slamet@getnada.com dimiliki oleh slamet slumut
# matahari@tokopedia.com dimiliki oleh toko matahari
import re
import random
import string

def generate_password(length):
    password_characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password

email_regex = re.compile(r'\S+@\S+')
txt_file = open("teks.txt", "r")
txt_content = txt_file.read()    
emails = email_regex.findall(txt_content)

for email in emails:
    username = email.split('@')[0]
    print(f'{email}: {username}, password: {generate_password(8)}') 

