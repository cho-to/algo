-- 코드를 입력하세요
SELECT f.flavor as FLAVOR
from first_half f inner join (
    select FLAVOR, sum(total_order) as TOTAL_ORDER
    from JULY
    group by FLAVOR
    ) j
    on f.flavor = j.flavor
order by f.total_order + j.total_order desc
limit 3