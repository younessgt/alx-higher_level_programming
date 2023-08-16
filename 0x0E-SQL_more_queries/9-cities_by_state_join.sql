-- script that lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- 0nly one SELECT statement is allowed

SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id;