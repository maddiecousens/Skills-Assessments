
-- Include your solutions to the More Practice problems in this file.


-- INSERT

INSERT INTO models (year, brand_name, name) 
    VALUES (2015, 'Chevrolet', 'Malibu'), (2015, 'Subaru', 'Outback');



-- CREATE TABLE


-- Instructions says capital 'Awards' but lowercasing for good form/ to match 
--  other tables.
CREATE TABLE awards ( 
--Unique identifier, useful for deleting rows
    id SERIAL PRIMARY KEY, 
    name VARCHAR(50) NOT NULL,
--name: Every award entered should have a corresponding year of the award, the same 
--  aware can have different years.
    year INTEGER NOT NULL,
-- winner_id: (NOT NULL) not required becaue awards should be able to be entered 
--even if there are no winners yet.
    winner_id INTEGER
        --REFERENCES models
    );
--NOTE: I think that this should reference the models table, however, in the
--  instructions for the INSERT they have us entereing a reference to a model
--  that doesn't exist. If the REFERENCE models line exists, this is illegal.


-- More INSERT
INSERT INTO awards (name, year, winner_id) 
    VALUES ('IIHS Safety Award', 2015, 49), ('IIHS Safety Award', 2015, 50);



