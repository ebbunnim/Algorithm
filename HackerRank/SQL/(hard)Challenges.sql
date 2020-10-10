/*
=> 동일한 애들은  max 아니면 삭제
*/

SELECT
    H.hacker_id, H.name, COUNT(*) AS challenges_created
FROM
    hackers H, challenges C
WHERE
    H.hacker_id=C.hacker_id
GROUP BY
    H.hacker_id, H.name
HAVING
    challenges_created=(
        SELECT
            MAX(cnt)
        FROM (SELECT COUNT(*) AS cnt
              FROM  challenges
              GROUP BY hacker_id
    ) sub
) OR
    challenges_created IN (  /*count가 하나인 것*/
        SELECT
            cnt
        FROM (SELECT COUNT(*) AS cnt
              FROM  challenges
              GROUP BY hacker_id
        ) sub
        GROUP BY cnt
        HAVING COUNT(*)=1
    )
ORDER BY
    challenges_created DESC, H.hacker_id
;