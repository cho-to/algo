-- 코드를 입력하세요
SELECT FACTORY_ID, factory_name, address
from food_factory
where address like '강원도%'
order by factory_id asc