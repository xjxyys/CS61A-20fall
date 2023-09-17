.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students
  WHERE pet = 'dog' AND color = 'blue';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students
  WHERE pet = 'dog' AND color = 'blue';


CREATE TABLE smallest_int AS
  SELECT time, smallest from students
  WHERE smallest > 2
  ORDER BY smallest ASC
  LIMIT 20;


CREATE TABLE matchmaker AS
  SELECT a.pet AS pet, a.song AS song, a.color AS first_color, b.color AS second_color
  FROM students AS a, students AS b
  WHERE a.pet = b.pet AND a.song = b.song AND a.time < b.time;


CREATE TABLE sevens AS
  SELECT students.seven from students, numbers
  WHERE students.number = 7 AND numbers.'7' = 'True' AND students.time = numbers.time;
