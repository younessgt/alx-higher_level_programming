-- Script that lists all records of the table second_table
-- Rows without a name value are not listed
SELECT score, name FROM second_table WHERE name IS NOT NULL AND > LEN(name) > 0 ORDER BY score DESC;
