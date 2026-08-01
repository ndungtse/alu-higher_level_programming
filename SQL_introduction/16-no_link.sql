-- Lists records with a name value, score and name, by descending score.
SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
