SELECT
    DISTINCT(CITY)
FROM
    STATION
WHERE CITY
    REGEXP '^[aeiou].*[aeiou]$'    // 어떤 길이(*)의 글자(.)건 상관없이
;