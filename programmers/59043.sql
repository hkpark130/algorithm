-- 있었는데요 없었습니다
-- https://school.programmers.co.kr/learn/courses/30/lessons/59043

SELECT o.ANIMAL_ID, o.NAME from ANIMAL_OUTS o, ANIMAL_INS i where o.ANIMAL_ID = i.ANIMAL_ID and o.DATETIME < i.DATETIME order by i.DATETIME;
