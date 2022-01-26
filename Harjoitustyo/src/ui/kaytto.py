import dao.alusta as alusta
import domain.logiikka as logiikka


def main():
    while True:
        print('''
        Valitse toiminto 0-9
        0 - poistusovelluksesta
        1 - luo tietokanta
        2 - lisaa paikka
        3 - lisaa asiakas
        4 - lisaa paketti asiakkaalle
        5 - lisaa paketti tapahtuma
        6 - hae paketin tapahtumat
        7 - asiakkaan paketit ja pakettien tapahtumat
        8 - tapahtumien määrä paikassa tiettyna paivana
        9 - tehokkuustesti
        10 - lisaa testi data
        11 - poista tietokanta 
        ''')
        komento = input()
        if komento == "0":
            print("Moi")
            break
        elif komento == "1":
            alusta.lisaa_taulut()
        elif komento == "2":
            nimi = input("Anna paikan nimi: ")
            logiikka.lisaa_paikka(nimi)
        elif komento == "3":
            nimi = input("Anna asiakkaan nimi: ")
            logiikka.lisaa_asiakas(nimi)
        elif komento == "4":
            koodi = input("Anna paketin seurantakoodi: ")
            nimi = input("Anna asiakkaan nimi: ")
            seurantakoodi = "K000000" + koodi
            print(seurantakoodi)
            logiikka.lisaa_paketti(seurantakoodi, nimi)
        elif komento == "5":
            koodi = input("Anna paketin seurantakoodi: ")
            paikka = input("Anna tapahtuman paikka: ")
            kuvaus = input("Anna tapahtuman kuvaus: ")
            seurantakoodi = "K000000" + koodi
            logiikka.lisaa_tapahtuma(seurantakoodi, paikka, kuvaus)
        elif komento == "6":
            koodi = input("Anna paketin seurantakoodi: ")
            seurantakoodi = "K000000" + koodi
            logiikka.hae_tapahtumat_koodi(seurantakoodi)
        elif komento == "7":
            nimi = input("Anna asiakkaan nimi: ")
            logiikka.hae_asiakkaan_paketit(nimi)
        elif komento == "8":
            nimi = input("Anna paikan nimi: ")
            paivamaara = input("Anna päivämäärä (vuosi-kuukausi-paiva):")
            logiikka.hae_tapahtumat_paikasta(nimi, paivamaara)
        elif komento == "9":
            vastaus = input("tehdäänkö testit indekseillä vai ilman? n/y ")
            if vastaus == "y":
                alusta.lisaa_indeksit()
            elif vastaus == "n":
                alusta.poista_indeksit()            
            logiikka.tehokkuustesti()
        elif komento == "10":
            alusta.lisaa_test_data()
        elif komento == "11":
            alusta.poista_taulut()