SET sql_safe_updates = FALSE;

USE defaultdb;
DROP DATABASE IF EXISTS game CASCADE;
CREATE DATABASE IF NOT EXISTS game;

USE game;

CREATE TABLE scores (
    id uuid PRIMARY KEY NOT NULL DEFAULT gen_random_uuid(),
    playername STRING,
    points INT8,
    UNIQUE INDEX scores_playername (playername ASC)
);

INSERT INTO scores (playername, points)
  VALUES ('Marlene F. Martell', 1298);

INSERT INTO scores (playername, points)
  VALUES ('Curtis D. Torres', 800);

INSERT INTO scores (playername, points)
  VALUES ('Sandy D. Martinez', 765);

INSERT INTO scores (playername, points)
  VALUES ('James O. Ewing', 721);
