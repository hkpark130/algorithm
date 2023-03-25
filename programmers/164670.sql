-- https://school.programmers.co.kr/learn/courses/30/lessons/164670

-- 코드를 입력하세요
SELECT USER_ID,NICKNAME,concat(CITY," ",STREET_ADDRESS1," ",STREET_ADDRESS2) as 전체주소,regexp_replace(TLNO,'(02|.{3})(.+)(.{4})', '$1-$2-$3') as 전화번호 from USED_GOODS_USER a
join USED_GOODS_BOARD b
on a.USER_ID = b.WRITER_ID
GROUP BY b.WRITER_ID
HAVING count(b.BOARD_ID) > 2
order by USER_ID desc
