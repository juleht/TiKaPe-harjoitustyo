import sqlite3


def yhteys_tietokantaan():
    cursor = None
    try:
        conn = sqlite3.connect('src/database.db', isolation_level=None)
        cursor = conn.cursor()
        return cursor
    except sqlite3.Error as e:
        print(e)
    return cursor

def alusta(komennot):
    cursor = yhteys_tietokantaan()
    try:
        cursor.execute("BEGIN")
        for komento in komennot:
            cursor.execute(komento)
        cursor.execute("COMMIT")
    except:
        print("error")


def lisaa_taulut():
    alusta(create_sql_komennot())

def poista_taulut():
    alusta(drop_tietokanta())

def lisaa_indeksit():
    alusta(create_indeksi())

def lisaa_test_data():
    alusta(sql_test())

def poista_indeksit():
    alusta(drop_indeksi())


def drop_indeksi():
    komennot = []
    komennot.append("DROP INDEX IF EXISTS idx_pnimi")
    komennot.append("DROP INDEX IF EXISTS idx_animi")
    komennot.append("DROP INDEX IF EXISTS idx_asikasid")
    komennot.append("DROP INDEX IF EXISTS idx_seurantakoodi")
    komennot.append("DROP INDEX IF EXISTS idx_kuvaus")
    komennot.append("DROP INDEX IF EXISTS idx_lisayshetki")
    komennot.append("DROP INDEX IF EXISTS idx_tapahtumaid")
    komennot.append("DROP INDEX IF EXISTS idx_paikkaid")
    return komennot



def create_indeksi():
    indeksit = []
    indeksit.append("CREATE INDEX idx_pnimi ON paikka(nimi)")
    indeksit.append("CREATE INDEX idx_animi ON asiakas(nimi)")
    indeksit.append("CREATE INDEX idx_asikasid ON paketti(asiakas_id)")
    indeksit.append("CREATE INDEX idx_seurantakoodi ON paketti(seurantakoodi)")
    indeksit.append("CREATE INDEX idx_kuvaus ON tapahtuma(kuvaus)")
    indeksit.append("CREATE INDEX idx_lisayshetki ON tapahtuma(lisayshetki)")
    indeksit.append("CREATE INDEX idx_tapahtumaid ON tapahtumapaikka(tapahtuma_id)")
    indeksit.append("CREATE INDEX idx_paikkaid ON tapahtumapaikka(tapahtuma_id)")
    return indeksit

def drop_tietokanta():
    taulut = []
    taulut.append("DROP TABLE paikka")
    taulut.append("DROP TABLE asiakas")
    taulut.append("DROP TABLE paketti")
    taulut.append("DROP TABLE tapahtumapaikka")
    taulut.append("DROP TABLE tapahtumapaketti")
    taulut.append("DROP TABLE tapahtuma")
    return taulut
    
def create_sql_komennot():
    sql_kommennot = []
    sql_kommennot.append("CREATE TABLE IF NOT EXISTS paikka (id INTEGER PRIMARY KEY, nimi TEXT);")
    sql_kommennot.append("CREATE TABLE IF NOT EXISTS asiakas (id INTEGER PRIMARY KEY, nimi TEXT);")
    sql_kommennot.append("CREATE TABLE IF NOT EXISTS paketti (id INTEGER PRIMARY KEY, asiakas_id INTEGER REFERENCES asiakas, seurantakoodi INTEGER);")
    sql_kommennot.append("CREATE TABLE IF NOT EXISTS tapahtumapaikka (id INTEGER PRIMARY KEY, tapahtuma_id INTEGER REFERENCES tapahtuma, paikka_id INTEGER REFERENCES paikka);")
    sql_kommennot.append("CREATE TABLE IF NOT EXISTS tapahtumapaketti (id INTEGER PRIMARY KEY, tapahtuma_id INTEGER REFERENCES tapahtuma, paketti_id INTEGER REFERENCES paketti);")
    sql_kommennot.append("CREATE TABLE IF NOT EXISTS tapahtuma (id INTEGER PRIMARY KEY, kuvaus TEXT, lisayshetki TEXT);")
    return sql_kommennot

def sql_test():
    sql_komennot = []
    sql_komennot.append("""INSERT INTO paikka(nimi) VALUES ('Varasto');""")
    sql_komennot.append("""INSERT INTO paikka(nimi) VALUES ('Satama');""")
    sql_komennot.append("""INSERT INTO paikka(nimi) VALUES ('Kalmankuja');""")
    sql_komennot.append("INSERT INTO asiakas(nimi) VALUES ('Kalle')")
    sql_komennot.append("INSERT INTO paketti(asiakas_id, seurantakoodi) VALUES (1, 'K000000100')")
    sql_komennot.append("INSERT INTO paketti(asiakas_id, seurantakoodi) VALUES (1, 'K000000101')")
    sql_komennot.append("INSERT INTO tapahtuma(kuvaus, lisayshetki) VALUES ('paketti kuljetukseen', '2022-01-26 12:00:00.000000')")
    sql_komennot.append("INSERT INTO tapahtuma(kuvaus, lisayshetki) VALUES ('paketti tullut maahan', '2022-01-26 13:00:00.000000')")
    sql_komennot.append("INSERT INTO tapahtuma(kuvaus, lisayshetki) VALUES ('paketti toimitettu', '2022-01-28 13:00:00.000000')")
    sql_komennot.append("INSERT INTO tapahtumapaikka(tapahtuma_id, paikka_id) VALUES (1, 1)")
    sql_komennot.append("INSERT INTO tapahtumapaikka(tapahtuma_id, paikka_id) VALUES (2, 2)")
    sql_komennot.append("INSERT INTO tapahtumapaikka(tapahtuma_id, paikka_id) VALUES (3, 3)")
    sql_komennot.append("INSERT INTO tapahtumapaketti(tapahtuma_id, paketti_id) VALUES (1, 1)")
    sql_komennot.append("INSERT INTO tapahtumapaketti(tapahtuma_id, paketti_id) VALUES (2, 1)")
    sql_komennot.append("INSERT INTO tapahtumapaketti(tapahtuma_id, paketti_id) VALUES (3, 1)")
    return sql_komennot