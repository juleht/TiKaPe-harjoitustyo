CREATE TABLE paikka (
  id INTEGER PRIMARY KEY,
  nimi TEXT
);

CREATE TABLE asiakas (
  id INTEGER PRIMARY KEY,
  nimi TEXT
);

CREATE TABLE paketti (
  id INTEGER PRIMARY KEY,
  asiakas_id INTEGER REFERENCES asiakas,
  seurantakoodi TEXT
);

CREATE TABLE tapahtumapaikka (
  id INTEGER PRIMARY KEY,
  tapahtuma_id INTEGER REFERENCES tapahtuma,
  paikka_id INTEGER REFERENCES paikka
);

CREATE TABLE tapahtumapaketti (
  id INTEGER PRIMARY KEY,
  tapahtuma_id INTEGER REFERENCES tapahtuma,
  paketti_id INTEGER REFERENCES paketti
);

CREATE TABLE tapahtuma (
  id INTEGER PRIMARY KEY,
  kuvaus TEXT,
  lisayshetki TEXT
);
