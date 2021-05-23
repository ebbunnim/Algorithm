-- id1에도 있고 id2에도 있는애 빼서 그룹핑 (서로 친구관계 - 양방향인 애들이 한번 카운팅 되므로 다 펼쳐서 카운팅)
SELECT A.ID1, COUNT(*)
FROM
(
    SELECT ID1 FROM FRIENDS
    UNION ALL
    SELECT ID2 FROM FRIENDS
) AS A
GROUP BY A.ID1
ORDER BY A.ID1
