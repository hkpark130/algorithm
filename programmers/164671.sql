-- https://school.programmers.co.kr/learn/courses/30/lessons/164671

-- 코드를 입력하세요
SELECT concat("/home/grep/src/",a.BOARD_ID,"/",b.FILE_ID,b.FILE_NAME,b.FILE_EXT) as FILE_PATH
from USED_GOODS_BOARD  a join USED_GOODS_FILE b on a.BOARD_ID = b.BOARD_ID
and a.BOARD_ID in (select BOARD_ID from USED_GOODS_BOARD where VIEWS = (select max(VIEWS) from USED_GOODS_BOARD))
order by FILE_ID desc
