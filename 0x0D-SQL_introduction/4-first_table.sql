-- Creates a table called first_table in the current database in my MySQL server
-- Should fail if first_table aready exist
-- Table Descrition:
--                  id INT
--                  name VARCHAR(256)
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
