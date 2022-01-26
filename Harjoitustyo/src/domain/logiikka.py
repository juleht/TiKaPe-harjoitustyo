import dao.tietokanta as tietokanta
import dao.alusta as alusta
from datetime import datetime, timedelta
import random
import time
from dao.helper import gen_datetime

def lisaa_paikka(nimi):
    '''
    Lisää uusi paikka tietokantaan, kun annetaan paikan nimi.
    '''
    paikka = tietokanta.get_paikka(nimi)
    if paikka is None:
        tietokanta.add_paikka(nimi)

def lisaa_asiakas(nimi):
    '''
    Lisää uusi asiakas tietokantaan, kun annetaan asiakkaan nimi.
    '''
    asiakas = tietokanta.get_asiakas(nimi)
    if asiakas is None:
        tietokanta.add_asiakas(nimi)

def lisaa_paketti(seurantakoodi, asiakkaan_nimi):
    '''
    Lisää uusi paketti tietokantaan, kun annetaan paketin seurantakoodi ja asiakkaan nimi.
    Asiakkaan tulee olla valmiiksi tietokannassa.
    '''
    asiakas = tietokanta.get_asiakas(asiakkaan_nimi)
    paketti = tietokanta.get_paketti(seurantakoodi)
    if paketti is None and asiakas is not None:
        tietokanta.add_paketti(asiakas[0], seurantakoodi)

def lisaa_tapahtuma(seurantakoodi, nimi, kuvaus):
    '''
    Lisää uusi tapahtuma tietokantaan, kun annetaan paketin seurantakoodi, tapahtuman paikka sekä kuvaus.
    Paketin ja paikan tulee olla valmiiksi tietokannassa.

    '''
    paketti = tietokanta.get_paketti(seurantakoodi)
    paikka = tietokanta.get_paikka(nimi)
    tapahtuma_id = tietokanta.add_tapahtuma(kuvaus, datetime.now())
    tietokanta.add_tapahtuma_paikka(tapahtuma_id, paikka[0])
    tietokanta.add_tapahtuma_paketti(tapahtuma_id, paketti[0])

def hae_tapahtumat_koodi(seurantakoodi):
    '''
    Hae kaikki paketin tapahtumat seurantakoodin perusteella.
    '''
    tapahtumat = []
    paketti = tietokanta.get_paketti(seurantakoodi)
    tapahtuma_id = tietokanta.get_tapahtuma_id(paketti[0])
    for id in tapahtuma_id:
        tapahtuma = tietokanta.get_tapahtuma(id[0])
        tapahtumat.append(tapahtuma)

    for t in tapahtumat:
        try:
            aika = datetime.strptime(t[1], "%Y-%m-%d %H:%M:%S.%f")
            print(aika.strftime("%d.%m.%Y %H:%M"), t[0])
        except:
            print("ajan muuttaminen ei onnistu")


def hae_asiakkaan_paketit(nimi):
    '''
    Hae kaikki asiakkaan paketit ja niihin liittyvien tapahtumien määrä.
    '''
    tapahtumat = tietokanta.get_asikkaan_paketit(nimi)
    
    for t in tapahtumat:
        print(f"{t[0]}, {t[1]}")
        pass

def hae_tapahtumat_paikasta(paikka, paivamaara):
    '''
    Hae annetusta paikasta tapahtumien määrä tiettynä päivänä.
    '''
    try:
        alkuaika = datetime.strptime(paivamaara, "%Y-%m-%d")
        loppuaika = datetime.strptime(paivamaara, "%Y-%m-%d") + timedelta(days=1)
    except:
        print("ajan muuttaminen ei onnistu")
    tapahtuma = tietokanta.get_tapahtumat_paikasta(paikka, alkuaika, loppuaika)
    print(f"Tapahtumien määrä: {tapahtuma}")

def tehokkuustesti():
    '''
    1. Tietokantaan lisätään tuhat paikkaa nimillä P1, P2, P3, jne.
    2. Tietokantaan lisätään tuhat asiakasta nimillä A1, A2, A3, jne.
    3. Tietokantaan lisätään tuhat pakettia, jokaiselle jokin asiakas.
    4. Tietokantaan lisätään kymmenen tuhatta tapahtumaa, jokaiselle jokin paketti.
    5. Suoritetaan tuhat kyselyä, joista jokaisessa haetaan jonkin asiakkaan pakettien määrä.
    6. Suoritetaan tuhat kyselyä, joista jokaisessa haetaan jonkin paketin tapahtumien määrä.
    '''
    paikkalista = ["P" + str(i) for i in range(1,1001)]
    asikaslista = ["A" + str(i) for i in range(1,1001)]
    pakettilista = ["K00000" + str(i) for i in range(1,1001)]
    asiakas_id = [i for i in range(1,1001)]
    tapahtuma_kuvaus = ["kuvaus" + str(i) for i in range(1, 10001)]
    tapahtumahetki = [gen_datetime() for i in range(1, 10001)]

    pAika = time.time()
    for pNimi in paikkalista:
        tietokanta.add_paikka(pNimi)
    print(f"Paikkojen lisäämiseen kului: {time.time() - pAika}")
    
    aAika = time.time()
    for aNimi in asikaslista:
        tietokanta.add_asiakas(aNimi)
    print(f"Asiakkaiden lisäämiseen kului: {time.time() - aAika}")

    paAika = time.time()
    for i in range(0,1000):
        pKoodi = pakettilista[i]
        a_id = asiakas_id[i]
        tietokanta.add_paketti(a_id, pKoodi)
    print(f"Pakettien lisäämiseen kului: {time.time() - paAika}")

    tAika = time.time()
    for i in range(0, 10000):
        t_kuvaus = tapahtuma_kuvaus[i]
        t_hetki = tapahtumahetki[i]
        tapahtuma_id = tietokanta.add_tapahtuma(t_kuvaus, t_hetki)
        tietokanta.add_tapahtuma_paketti(tapahtuma_id, random.randint(1,1000))
    print(f"Tapahtumien lisäämiseen kului: {time.time() - tAika}")


    tHakuAika = time.time()
    hae_tapahtumat_koodi(random.choice(pakettilista))
    print(f"tapahtumien määrän hakemiseen kului: {time.time() - tHakuAika}")