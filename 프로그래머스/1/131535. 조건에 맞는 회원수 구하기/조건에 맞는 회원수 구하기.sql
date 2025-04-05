-- 코드를 입력하세요
SELECT COUNT(user_id) as USERS
from user_info
where age >= 20 and age <= 29 and joined like '%2021%'