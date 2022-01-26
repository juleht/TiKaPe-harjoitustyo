from datetime import datetime
from dao.alusta import yhteys_tietokantaan


def add_paikka(nimi):
    try:
        cursor = yhteys_tietokantaan()
        sql = "INSERT INTO paikka(nimi) VALUES (?)"
        cursor.execute(sql, [nimi])
    except:
        print("asiakkaan lisääminen tietokantaan ei onnistu")

def get_paikka(nimi):
    try:
        cursor = yhteys_tietokantaan()
        sql = "SELECT * FROM paikka WHERE nimi = ?"
        cursor.execute(sql, [nimi])
        return cursor.fetchone()
    except:
        print("paikan hakeminen tietokannasta ei onnistu")

def add_asiakas(nimi):
    try:
        cursor = yhteys_tietokantaan()
        sql = "INSERT INTO asiakas(nimi) VALUES (?)"
        cursor.execute(sql, [nimi])
    except:
        print("asikkaan lisääminen tietokantaa ei onnistu")

def get_asiakas(nimi):
    try:
        cursor = yhteys_tietokantaan()
        sql = "SELECT * FROM asiakas WHERE nimi = ?"
        cursor.execute(sql, [nimi])
        return cursor.fetchone()
    except:
        print("asiakkaan hakeminen tietokannasta ei onnistu")

def add_paketti(asiakas_id, seurantakoodi):
    try:
        cursor = yhteys_tietokantaan()
        sql = "INSERT INTO paketti(asiakas_id, seurantakoodi) VALUES (?, ?)"
        cursor.execute(sql, [asiakas_id, seurantakoodi])
    except:
        print("paketin lisääminen tietokantaan ei onnistu")

def get_paketti(seurantakoodi):
    try:
        cursor = yhteys_tietokantaan()
        sql = "SELECT * FROM paketti WHERE seurantakoodi = ?"
        cursor.execute(sql, [seurantakoodi])
        return cursor.fetchone()
    except:
        print("paketin hakeminen ei onnistu")

def add_tapahtuma(kuvaus, lisayshetki):
    try:
        cursor = yhteys_tietokantaan()
        sql = "INSERT INTO tapahtuma(kuvaus, lisayshetki) VALUES (?, ?)"
        lisayshetki = datetime.now()
        cursor.execute(sql, [kuvaus, lisayshetki])
        return cursor.lastrowid
    except:
        print("tapahtuman lisääminen ei onnistu")

def add_tapahtuma_paketti(tapahtuma_id, paketti_id):
    try:
        cursor = yhteys_tietokantaan()
        sql = "INSERT INTO tapahtumapaketti(tapahtuma_id, paketti_id) VALUES (?, ?)"
        cursor.execute(sql, [tapahtuma_id, paketti_id])
    except:
        print("tapahtumapaketin lisääminen ei onnistu")
    
def add_tapahtuma_paikka(tapahtuma_id, paikka_id):
    try:
        cursor = yhteys_tietokantaan()
        sql = "INSERT INTO tapahtumapaikka(tapahtuma_id, paikka_id) VALUES (?, ?)"
        cursor.execute(sql, [tapahtuma_id, paikka_id])
    except:
        print("tapahtumapaikan lisääminen ei onnistu")

def get_tapahtuma_id(paketti_id):
    try:
        cursor = yhteys_tietokantaan()
        sql = "SELECT tapahtuma_id FROM tapahtumapaketti WHERE paketti_id = ?"
        cursor.execute(sql, [paketti_id])
        return cursor.fetchall()
    except:
        print("tapahtumien hakeminen ei onnistu")

def get_tapahtuma(id):        
    try:
        cursor = yhteys_tietokantaan()
        sql = "SELECT kuvaus, lisayshetki FROM tapahtuma WHERE id = ?"
        cursor.execute(sql, [id])
        return cursor.fetchone()
    except:
        print("tapahtuman hakeminen ei onnistu")

def get_asikkaan_paketit(nimi):
    try:
        cursor = yhteys_tietokantaan()
        sql = "SELECT P.seurantakoodi, T.kuvaus FROM asiakas A, paketti P, tapahtumapaketti TP, tapahtuma T WHERE A.id = P.asiakas_id AND P.id = TP.paketti_id AND TP.tapahtuma_id = T.id AND A.nimi = ?"
        cursor.execute(sql, [nimi])
        return cursor.fetchall()
    except:
        print("asiakkaan pakettien hakeminen ei onnistu")

def get_tapahtumat_paikasta(paikka, alkuaika, loppuaika):
    try:
        cursor = yhteys_tietokantaan()
        sql = "SELECT COUNT(T.id) FROM paikka P, tapahtumapaikka TP, tapahtuma T WHERE P.id = TP.paikka_id AND TP.tapahtuma_id = T.id AND P.nimi = ? AND T.lisayshetki BETWEEN ? AND ?"
        cursor.execute(sql, [paikka, alkuaika, loppuaika])
        return cursor.fetchone()[0]
    except:
        print("tapahtumien hakeminen paikasta ei onnistunut")