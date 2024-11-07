CREATE TABLE clubs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  club TEXT NOT NULL,
  category TEXT NOT NULL,
  location TEXT NOT NULL,
  provide TEXT NOT NULL,
  looking TEXT NOT NULL,
  description NOT NULL,
  contact NOT NULL
);

CREATE TABLE businesses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  business TEXT NOT NULL,
  location TEXT NOT NULL,
  provide TEXT NOT NULL,
  looking TEXT NOT NULL,
  description NOT NULL,
  contact NOT NULL
);
