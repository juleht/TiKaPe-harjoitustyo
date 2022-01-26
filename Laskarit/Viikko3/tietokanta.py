import sqlite3
import random
import string
import time
import os


db = sqlite3.connect('Viikko3/database.db')
cursor = db.cursor()

def luo_tietokanta():
    sql = "CREATE TABLE elokuvat (id INTEGER PRIMARY key, nimi TEXT, vuosi INTEGER)"
    cursor.execute(sql)

def poista_tietokanta():
    sql = "DROP TABLE elokuvat"
    cursor.execute(sql)

def lisaa():
    aloitusaika = time.time()
    cursor.execute("BEGIN")
    for i in range(1000000):
        vuosi = random.randint(1900,2000)
        nimi = ''.join(random.choices(string.ascii_lowercase, k=8))
        sql = "INSERT INTO elokuvat (nimi, vuosi) VALUES (?,?)"
        cursor.execute(sql, [nimi, vuosi])
    cursor.execute("COMMIT")
    print(f"Rivien lisäämiseen kuluva aika: {time.time() - aloitusaika}")

def hae():
    aloitusaika = time.time()
    for i in range(1000):
        vuosi = random.randint(1900,2000)
        sql = "SELECT COUNT(*) FROM elokuvat WHERE vuosi = ?"
        cursor.execute(sql, [vuosi])
    print(f"Kyselyiden suoritukseen kuluva aika: {time.time() - aloitusaika}")

def indeksi():
    sql = "CREATE INDEX idx_vuosi ON elokuvat(vuosi)"
    cursor.execute(sql)


def tietokannan_koko():
    print(f"Tietokannan koko on {os.path.getsize('Viikko3/database.db') / 1000000.0} megatavua")

time.time()


def ilman_indeksia():
    aloitusaika = time.time()
    luo_tietokanta()
    lisaa()
    hae()
    tietokannan_koko()
    poista_tietokanta()
    return f"sekuntia: {time.time() - aloitusaika}"

def indeksi_ennen_riveja():
    aloitusaika = time.time()
    luo_tietokanta()
    indeksi()
    lisaa()
    hae()
    tietokannan_koko()
    poista_tietokanta()
    return f"sekuntia: {time.time() - aloitusaika}"

def indeksi_ennen_kyselya():
    aloitusaika = time.time()
    luo_tietokanta()
    lisaa()
    indeksi()
    hae()
    tietokannan_koko()
    poista_tietokanta()
    return f"sekuntia: {time.time() - aloitusaika}" 