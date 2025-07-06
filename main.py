import time  # buat ngatur delay (jeda waktu antar teks)
from threading import Thread, Lock  # biar bisa jalanin banyak teks barengan + pengaman biar gak numpuk
import sys  # buat ngatur output teks ke layar (biar bisa print per huruf)
import pygame  # buat muter lagu

kunci = Lock()  # kaya gembok digital, biar teks gak rebutan tampil pas barengan

# fungsi buat animasi teks muncul satu per satu kayak efek ngetik
def animasi_teks(teks, jeda=0.1):
    with kunci:  # aktifin kunci biar aman kalo lagi multitasking
        for huruf in teks:
            sys.stdout.write(huruf)  # nulis satu huruf ke layar
            sys.stdout.flush()  # langsung tampil di layar, gak nunggu baris selesai
            time.sleep(jeda)  # jeda antar huruf (semakin kecil, makin cepat)
        print()  # biar ganti baris abis selesai satu kalimat

# fungsi buat nampilin satu lirik dengan delay sebelum muncul dan animasi ketiknya
def nyanyiin_lirik(lirik, jeda_awal, kecepatan_tulis):
    time.sleep(jeda_awal)  # nunggu dulu sebelum mulai tampil
    animasi_teks(lirik, kecepatan_tulis)  # tampilin teksnya dengan animasi

# fungsi utama buat nyanyiin semua lirik
def nyanyi_lagu():
    # isi liriknya + seberapa cepat ditampilin per huruf
    lirik_dan_kecepatan = [
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten", 0.1),
        ("about you?", 0.2),
        ("There was something bout you that now I cant remember", 0.08),
        ("Its the same damn thing that made my heart surrender", 0.1),
        ("And I miss you on a train, I miss you in the morning", 0.1),
        ("I never know what to think about", 0.1),
        ("I think about youuuuuuuuuuuuuuuuuuuuuuuuuuu", 0.1)
    ]

    # jeda awal sebelum tiap baris muncul (kaya timing-nya biar pas kayak di lagu asli)
    jeda_per_baris = [0.3, 5.0, 10.0, 15.0, 20.3, 25.0, 27.0, 30.2, 33.3]

    daftar_thread = []  # list buat nyimpen semua thread (baris lirik)
    
    # looping(pengulangan) buat siapin dan jalanin setiap baris lirik
    for i in range(len(lirik_dan_kecepatan)):
        lirik, kecepatan = lirik_dan_kecepatan[i]  # ambil teks lirik & kecepatannya
        # bikin thread baru buat nampilin satu baris lirik
        t = Thread(target=nyanyiin_lirik, args=(lirik, jeda_per_baris[i], kecepatan))
        daftar_thread.append(t)  # simpen thread ke list
        t.start()  # mulai thread-nya (lirik mulai muncul sesuai waktunya)

    # nunggu semua thread selesai dulu sebelum program selesai
    for t in daftar_thread:
        t.join()

# ini buat jalanin fungsi nyanyi_lagu kalo file-nya langsung dijalankan
if __name__ == "__main__":
    pygame.mixer.init()  # siapin pemutar lagu (bisa mp3, wav, dll)
    pygame.mixer.music.load("about-you.mp3")  # sumber lagunya
    pygame.mixer.music.play()  # langsung muter lagunya
    nyanyi_lagu()  # mulai nyanyi (lirik jalan barengan musik)

print("ditantang Nesya, diterima oleh Jefanniel") # done ya nes
