1

-----

Select all fields for all brands in the brands table.

The result set for this query should be every record in the brands table.

-----


SELECT *
  FROM brands;


==========
2

-----

Select all fields for all car models made by Pontiac in the 
models table. 

The result set should be:
  id   | year  | brand_name |    name
-------+-------+------------+------------
    25 |  1961 | Pontiac    | Tempest
    27 |  1962 | Pontiac    | Grand Prix
    36 |  1963 | Pontiac    | Grand Prix
    42 |  1964 | Pontiac    | GTO
    43 |  1964 | Pontiac    | LeMans
    44 |  1964 | Pontiac    | Bonneville
    45 |  1964 | Pontiac    | Grand Prix
(7 rows)


-----


SELECT *
  FROM models
  WHERE brand_name = 'Pontiac';


==========
3

-----

Select the brand name and model name for all models made in 
1964 from the models table. 

The result set should be:
 brand_name |    name
------------+-------------
 Chevrolet  | Corvette
 Ford       | Mustang
 Ford       | Galaxie
 Pontiac    | GTO
 Pontiac    | LeMans
 Pontiac    | Bonneville
 Pontiac    | Grand Prix
 Plymouth   | Fury
 Studebaker | Avanti
 Austin     | Mini Cooper
 (10 rows)
 

-----


SELECT brand_name, 
       name
  FROM models
  WHERE year = 1964;


==========
4

-----

Select the model name, brand name, and headquarters for 
the Ford Mustang from the models and brands tables.

The result set should be:
  name   | brand_name | headquarters
---------+------------+--------------
 Mustang | Ford       | Dearborn, MI
 (1 rows)


-----


SELECT m.name,
       m.brand_name,
       b.headquarters
  FROM models m
    JOIN brands b
      ON b.name = m.brand_name
	WHERE m.name = 'Mustang';


==========
5

-----

Select all rows for the three oldest brands from the brands
table.

The result set should be:
  id   |    name    | founded |    headquarters     | discontinued
-------+------------+---------+---------------------+--------------
    10 | Studebaker |    1852 | South Bend, Indiana |         1967
    13 | Rambler    |    1901 | Kenosha, Washington |         1969
     6 | Cadillac   |    1902 | New York City, NY   |
(3 rows)


-----


SELECT *
  FROM brands
ORDER BY founded
LIMIT 3;


==========
6

-----

Count the Ford models in the database The output should be a 
number.

The result set should be:
   count
------------
          6
(1 rows)


-----


SELECT COUNT(*) 
  FROM models
  WHERE brand_name = 'Ford';


==========
7

-----

Select the name of any and all car brands that are not 
discontinued.

The result set should be:
   name
-----------
 Ford
 Chrysler
 Chevrolet
 Cadillac
 BMW
 Buick
 Tesla
(7 rows)


-----


SELECT name 
  FROM brands
  WHERE discontinued IS NULL;


==========
8

-----

Select everything from rows 15-24 of the models table in 
alphabetical order by name. The result set should have 10 records.

The result set should be:
  id   | year  | brand_name |   name
-------+-------+------------+----------
    38 |  1963 | Chevrolet  | Corvette
    11 |  1957 | Chevrolet  | Corvette
    20 |  1960 | Chevrolet  | Corvette
     5 |  1953 | Chevrolet  | Corvette
    13 |  1958 | Chevrolet  | Corvette
    10 |  1956 | Chevrolet  | Corvette
    17 |  1959 | Chevrolet  | Corvette
    26 |  1961 | Chevrolet  | Corvette
     8 |  1955 | Chevrolet  | Corvette
    28 |  1962 | Chevrolet  | Corvette
(10 rows)


-----


SELECT * 
  FROM models
ORDER BY name
LIMIT 10
OFFSET 14;


==========
9

-----

Select the brand, name, and year the model's brand was 
founded for all of the models from 1960. Include row(s)
for model(s) even if their brand(s) are not in the brands table.

Note that in the result set, the year the brand was founded should be NULL if
the brand is not in the brands table.

So, the result set should be:
   name   | brand_name | founded
----------+------------+---------
 Corvette | Chevrolet  |    1911
 Corvair  | Chevrolet  |    1911
 Rockette | Fairthorpe |    1954
 Fillmore | Fillmore   |
(4 rows)


-----


SELECT m.name, m.brand_name, b.founded FROM models m
  LEFT JOIN brands b on b.name = m.brand_name
  WHERE m.year = 1960;


==========
10

-----

Modify the query so that it shows all brands that are 
not discontinued regardless of whether they have any models in the models table.
The correct output should not include records for Fillmore and Outback, but should
show information about Tesla, a brand with no models in the models table.

-----


SELECT b.name,
         b.founded,
         m.name
  FROM brands AS b
    LEFT JOIN models AS m
      ON b.name = m.brand_name
  WHERE b.discontinued IS NULL;


==========
11

-----

Modify the query so it only selects models whose brands ARE in the brands table.
So, we shouldn't see models who brands aren't in the brands table (a.k.a. Fillmore,
Outback) nor should we see information about brands who don't have any models in 
the models table (a.k.a. Tesla).

-----


SELECT m.name,
       m.brand_name,
       b.founded
  FROM models m
    JOIN brands b
      ON b.name = m.brand_name;


==========
12

-----

Modify the query so that it only selects brands that do NOT have any
models in the models table.

The correct result set is:

 name  | founded
-------+---------
 Tesla |    2003
(1 rows)

-----


SELECT b.name, 
       b.founded
  FROM brands b
    LEFT JOIN models m
      ON b.name = m.brand_name
  WHERE m.id IS NULL;


==========
13

-----

Modify the query to add another field to the results that gives 
the number of years from the year of the model until the brand becomes 
discontinued.

Display this new field with the name years_until_brand_discontinued. The correct
result set is:

    name    |       name       | year | discontinued | years_until_brand_discontinued
------------+------------------+------+--------------+--------------------------------
 Austin     | Mini             | 1959 |         1987 |                             28
 Austin     | Mini             | 1963 |         1987 |                             24
 Austin     | Mini Cooper      | 1961 |         1987 |                             26
 Austin     | Mini Cooper      | 1964 |         1987 |                             23
 Austin     | Mini Cooper S    | 1963 |         1987 |                             24
 Fairthorpe | Rockette         | 1960 |         1976 |                             16
 Hillman    | Minx Magnificent | 1950 |         1981 |                             31
 Plymouth   | Fury             | 1964 |         2001 |                             37
 Pontiac    | Bonneville       | 1964 |         2010 |                             46
 Pontiac    | GTO              | 1964 |         2010 |                             46
 Pontiac    | Grand Prix       | 1962 |         2010 |                             48
 Pontiac    | Grand Prix       | 1963 |         2010 |                             47
 Pontiac    | Grand Prix       | 1964 |         2010 |                             46
 Pontiac    | LeMans           | 1964 |         2010 |                             46
 Pontiac    | Tempest          | 1961 |         2010 |                             49
 Rambler    | Classic          | 1963 |         1969 |                              6
 Studebaker | Avanti           | 1961 |         1967 |                              6
 Studebaker | Avanti           | 1962 |         1967 |                              5
 Studebaker | Avanti           | 1963 |         1967 |                              4
 Studebaker | Avanti           | 1964 |         1967 |                              3
(20 rows)

-----


SELECT b.name,
       m.name,
       m.year,
       b.discontinued,
       b.discontinued - m.year AS years_until_brand_discontinued
  FROM models m
    LEFT JOIN brands b
      ON m.brand_name = b.name
  WHERE b.discontinued IS NOT NULL
  ORDER BY b.name, m.name, m.year;


==========
14

-----

Select the name of any brand with more than 5 models in the 
database using a HAVING clause.

The correct result set is:

 brand_name
------------
 Chevrolet
 Pontiac
 Ford
(3 rows)


-----


SELECT brand_name
  FROM models 
GROUP BY brand_name
HAVING COUNT(*) > 5;


==========
15

-----

Using a subquery, select the name and year of any model whose 
year is the same year that ANY brand was founded.

The result set should be:

   name    | year
-----------+-------
 Imperial  |  1926
 Corvette  |  1954
 Fleetwood |  1954
(3 rows)

-----


SELECT name,
       year
  FROM models
  WHERE year IN (
      SELECT founded
        FROM brands);