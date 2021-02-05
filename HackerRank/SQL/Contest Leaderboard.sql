
SELECT
    A.hacker_id, MIN(H.name), SUM(A.score) /*H.name으로만 쓰면 groupby에서 못찾음*/
FROM ( /*메인 쿼리. inner 연산 처리*/
    SELECT
        hacker_id, challenge_id, MAX(score) AS score
    FROM
        Submissions
    GROUP BY
        hacker_id, challenge_id
) A, Hackers H
WHERE
    H.hacker_id=A.hacker_id
GROUP BY
    A.hacker_id
HAVING
    SUM(A.score)>0
ORDER BY
    SUM(A.score) DESC, A.hacker_id
;
