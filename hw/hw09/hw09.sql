CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes
  WHERE height > min AND height <= max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT p.child FROM dogs AS d, parents AS p
  WHERE d.name = p.parent ORDER BY d.height DESC;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.name AS first, b.name AS second
  FROM dogs AS a, dogs AS b, parents AS p1, parents AS p2
  WHERE a.name < b.name AND p1.child = a.name AND p2.child = b.name AND p1.parent = p2.parent;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || siblings.first || " plus " || siblings.second || " have the same size: " || s1.size AS sentence
  FROM siblings, size_of_dogs AS s1, size_of_dogs AS s2
  WHERE s1.name = siblings.first AND s2.name = siblings.second AND s1.size = s2.size;