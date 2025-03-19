.read hw10_data.sql

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name,size FROM dogs,sizes WHERE height <= max AND height > min;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.name FROM dogs AS a,parents AS b,dogs AS c WHERE a.name = b.child AND b.parent = c.name ORDER BY c.height DESC;
  


-- Sentences about siblings that are the same size
CREATE TABLE help AS
  SELECT a.child AS c1, b.child AS c2 
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child < b.child;

CREATE TABLE sentences AS
  SELECT "The two siblings, " || c1 || " plus " || c2 || " have the same size: " || a.size
  FROM help, size_of_dogs AS a, size_of_dogs AS b
  WHERE a.size = b.size AND a.name = c1 AND b.name = c2;

