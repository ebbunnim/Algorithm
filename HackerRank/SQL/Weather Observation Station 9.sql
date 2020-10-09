SELECT
    DISTINCT(CITY)
FROM
    STATION
WHERE CITY
    REGEXP '^[^aeiou]'  // []안에 ^ 있으면 제외를 의미
;