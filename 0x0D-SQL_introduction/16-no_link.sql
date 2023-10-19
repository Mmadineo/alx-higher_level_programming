-- List all records of second_table having name value
-- Records are ordered by descendng order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
