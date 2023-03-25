-- NULL 처리하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/59410

SELECT ANIMAL_TYPE, (CASE WHEN NAME is null THEN "No name" ELSE NAME END), SEX_UPON_INTAKE from ANIMAL_INS;
