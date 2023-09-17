.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) AS average_price 
  FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) AS lowest_price
  FROM inventory GROUP BY item ORDER BY item; 

CREATE TABLE best_deal AS
  SELECT name, MIN(MSRP / rating) AS best_price
  FROM products 
  GROUP BY category;

CREATE TABLE shopping_list AS
  SELECT bd.name, lp.store
  FROM best_deal AS bd, lowest_prices AS lp
  WHERE bd.name = lp.item;

CREATE TABLE total_bandwidth AS
  SELECT SUM(stores.Mbs)
  FROM stores, shopping_list
  WHERE stores.store = shopping_list.store;
