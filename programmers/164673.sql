-- https://school.programmers.co.kr/learn/courses/30/lessons/164673

-- 코드를 입력하세요
SELECT A.TITLE,B.BOARD_ID,B.REPLY_ID,B.WRITER_ID,B.CONTENTS,DATE_FORMAT(B.CREATED_DATE,'%Y-%m-%d') as CREATED_DATE from USED_GOODS_BOARD A
join USED_GOODS_REPLY B
on A.BOARD_ID = B.BOARD_ID
where A.CREATED_DATE between '2022-10-01' and '2022-10-31'
order by B.CREATED_DATE, A.TITLE
