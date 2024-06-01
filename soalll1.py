#Anda diminta untuk mencari seluruh teks yang berupa tanggal dengan format YYYY-MM-DD dan kemudian seluruh tanggal tersebut
#diambil dan ditampilkan kembali dalam format DD-MM-YYYY ditambah dengan perhitungan selisih dengan tanggal sekarang dalam hari.
#Contoh:
#Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11),
#Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02).

import re
from datetime import datetime

with open("textx.txt", "r") as file:
    teks = file.read()

tanggal_regex = r'\b(\d{4}-\d{2}-\d{2})\b'
tanggal_list = re.findall(tanggal_regex, teks)

tanggal_sekarang = datetime.now()
for tanggal in tanggal_list:
    tanggal_obj = datetime.strptime(tanggal, '%Y-%m-%d')
    tanggal_str = tanggal_obj.strftime('%d-%m-%Y')
    if tanggal_obj > tanggal_sekarang:
        selisih_hari = (tanggal_obj - tanggal_sekarang).days
    else:
        selisih_hari = (tanggal_sekarang - tanggal_obj).days
    print(f"{tanggal_str} 00:00:00 selisih {selisih_hari} hari")