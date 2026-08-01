-- Lists the number of records per score, sorted by count (descending).
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score ORDER BY number DESC;
