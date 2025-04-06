-- 코드를 입력하세요
SELECT p.product_id as PRODUCT_ID, p.product_name as PRODUCT_NAME, sum(o.amount) * p.price as TOTAL_SALES
from food_product p inner join food_order o on p.product_id = o.product_id
where o.produce_date like '2022-05%'
group by p.product_id 
order by 3 desc, 1 asc
