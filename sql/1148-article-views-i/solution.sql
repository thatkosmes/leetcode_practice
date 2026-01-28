# MySQL
SELECT 
    author_id AS id
FROM Views
WHERE viewer_id = author_id
GROUP BY id
ORDER BY id;