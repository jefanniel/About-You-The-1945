import time
from threading import Thread, Lock
import sys

kunci = Lock()

def animasi_teks(teks, jeda=0.1):
    with kunci:
        for huruf in teks:
            sys.stdout.write(huruf)
            sys.stdout.flush()
            time.sleep(jeda)
        print()

def nyanyiin_lirik(lirik, jeda_awal, kecepatan_tulis):
    time.sleep(jeda_awal)
    animasi_teks(lirik, kecepatan_tulis)

def nyanyi_lagu():
    lirik_dan_kecepatan = [
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten?", 0.1),
        ("Do you think I have forgotten", 0.1),
        ("about you?", 0.2),
        ("There was something bout you that now I cant remember", 0.08), #0.08, 0.1 itu seberapa cepet liriknya diketik
        ("Its the same damn thing that made my heart surrender", 0.1),
        ("And I miss you on a train, I miss you in the morning", 0.1),
        ("I never know what to think about", 0.1),
        ("I think about youuuuuuuuuuuuuuuuuuuuuuuuuuu", 0.1)
    ]

    jeda_per_baris = [0.3, 5.0, 10.0, 15.0, 20.3, 25.0, 27.0, 30.2, 33.3] # ini detik ke berapa lagunya muncul. 33.3 itu detik 33.3 muncul liriknya

    daftar_thread = []
    
    for i in range(len(lirik_dan_kecepatan)):
        lirik, kecepatan = lirik_dan_kecepatan[i]
        t = Thread(target=nyanyiin_lirik, args=(lirik, jeda_per_baris[i], kecepatan))
        daftar_thread.append(t)
        t.start()

    for t in daftar_thread:
        t.join()

if __name__ == "__main__":
    nyanyi_lagu()
