CREATE TABLE kayttaja (
  id SERIAL PRIMARY KEY,
  kayttajanimi TEXT,
  salasana TEXT
);

CREATE TABLE video (
  id SERIAL PRIMARY KEY,
  kayttaja_id INTEGER REFERENCES kayttaja(id)
  nimi TEXT,
  kuvaus TEXT,
  julkaisupaiva datetime,
  arvioitu BOOLEAN
);

CREATE TABLE katselut (
  id SERIAL PRIMARY KEY,
  video_id INTEGER REFERENCES video(id)
);

CREATE TABLE kommenttivideo (
  id SERIAL PRIMARY KEY,
  kommentti_id INTEGER REFERENCES kommentti(id),
  video_id INTEGER REFERENCES video(id)
);

CREATE TABLE kayttajakommentti (
  id SERIAL PRIMARY KEY,
  kayttaja_id INTEGER REFERENCES kayttaja(id),
  kommentti_id INTEGER REFERENCES kommentti(id)
);

CREATE TABLE kommentti (
  id SERIAL PRIMARY KEY,
  teksti TEXT
);

CREATE TABLE arviovideo (
  id SERIAL PRIMARY KEY,
  arvio_id INTEGER REFERENCES arvio(id),
  video_id INTEGER REFERENCES video(id)
);

CREATE TABLE arviot (
  id SERIAL PRIMARY KEY,
  arvio BOOLEAN
);

CREATE TABLE soittolista (
  id SERIAL PRIMARY KEY,
  kanava_id INTEGER REFERENCES kanava(id),
  lisaa_video BOOLEAN
);

CREATE TABLE kanava (
  id SERIAL PRIMARY KEY,
  video_id INTEGER REFERENCES video(id),
  kayttaja_id INTEGER REFERENCES kayttaja(id),
  sivu TEXT
);

CREATE TABLE tilaus (
  id SERIAL PRIMARY KEY,
  kayttaja_id INTEGER REFERENCES kayttaja(id),
  kanava_id INTEGER REFERENCES kanava(id)
);

CREATE TABLE tekstitys (
  id SERIAL PRIMARY KEY,
  video_id INTEGER REFERENCES video(id),
  sanat TEXT,
  aika datetime
);

CREATE TABLE seuraaja (
  id SERIAL PRIMARY KEY,
  tilaaja_id INTEGER REFERENCES kayttaja(id),
  tilattu_id INTEGER REFERENCES kayttaja(id),
  estetty BOOLEAN,
  viesti TEXT,
  aloitettu datetime
);