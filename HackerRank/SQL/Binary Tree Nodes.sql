SELECT
    CASE
        WHEN P IS NULL
        THEN CONCAT(N,' ','Root')
        WHEN N NOT IN (SELECT DISTINCT P FROM BST WHERE P IS NOT NULL)
        THEN CONCAT(N,' ','Leaf')
        ELSE CONCAT(N,' ','Inner')
    END
FROM BST
ORDER BY N
;