-- Create a new table 'second_table'
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(255),
    score INT
);

-- Insert some data into table 'second_table'
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8)
;
