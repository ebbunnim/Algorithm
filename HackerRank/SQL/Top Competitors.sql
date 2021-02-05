
SELECT
    H.hacker_id, H.name
FROM
    HACKERS H
INNER JOIN
    SUBMISSIONS S ON H.hacker_id=S.hacker_id
INNER JOIN
    CHALLENGES C ON S.challenge_id=C.challenge_id
WHERE
    S.score=(
        SELECT
            D.score
        FROM
            DIFFICULTY D
        WHERE
            C.difficulty_level=D.difficulty_level
    )
GROUP BY
    H.hacker_id, H.name
HAVING
    COUNT(*)>1
ORDER BY
    COUNT(*) DESC, H.hacker_id
;