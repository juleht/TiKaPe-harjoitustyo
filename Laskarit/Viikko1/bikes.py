import sqlite3

db = sqlite3.connect("bikes.db")
cursor = db.cursor()

def distance_of_user(user):
    '''
    ilmoittaa kayttajan (name) ajaman kokonaismatkan
    '''
    sql = "SELECT SUM(T.distance) FROM Users U, Trips T WHERE U.id = T.user_id AND U.name = ?"
    cursor.execute(sql, [user])
    return cursor.fetchone()[0]

def speed_of_user(user):
    '''
    ilmoittaa käyttäjän keskinopeuden (km/h) kaikilla matkoilla kahden desimaalin tarkkuudella.
    '''
    distance = distance_of_user(user)
    sql = "SELECT SUM(T.duration) FROM Users U, Trips T WHERE U.id = T.user_id AND U.name = ?"
    cursor.execute(sql, [user])
    duration = cursor.fetchone()[0]
    speed = (distance / 1000.0) / (duration / 60.0)
    return round(speed, 2)

def duration_in_each_city(day):
    '''
    ilmoittaa jokaisesta kaupungista, kauanko pyörillä ajettiin annettuna päivänä.
    '''
    sql = "SELECT C.name, SUM(T.duration) FROM Bikes B, Cities C, Trips T WHERE C.id = B.city_id AND B.id = T.bike_id AND day = ? GROUP BY C.name"
    cursor.execute(sql, [day])
    return cursor.fetchall()

def users_in_city(city):
    '''
    ilmoittaa, montako eri käyttäjää pyörillä on ollut annetussa kaupungissa.
    '''
    sql = "SELECT COUNT(DISTINCT T.user_id) FROM Cities C, Bikes B, Trips T WHERE C.id = B.city_id AND B.id = T.bike_id AND C.name = ?"
    cursor.execute(sql, [city])
    return cursor.fetchone()[0]

def trips_on_each_day(city):
    '''
    ilmoittaa jokaisesta päivästä, montako matkaa kyseisenä päivänä on ajettu.
    '''
    sql = "SELECT T.day, COUNT(T.day) FROM Cities C, Bikes B, Trips T WHERE C.id = B.city_id AND B.id = T.bike_id AND C.name = ? GROUP BY T.day"
    cursor.execute(sql, [city])
    return cursor.fetchall()

def most_popular_start(city):
    '''
    ilmoittaa kaupungin suosituimman aloitusaseman matkalle sekä matkojen määrän.
    '''
    sql = "SELECT S.name, COUNT(T.from_id) AS maara FROM Stops S, Cities C, Trips T WHERE S.city_id = C.id and S.id = T.from_id and C.name = ? GROUP BY S.name ORDER BY maara DESC LIMIT 1"
    cursor.execute(sql, [city])
    return cursor.fetchall()