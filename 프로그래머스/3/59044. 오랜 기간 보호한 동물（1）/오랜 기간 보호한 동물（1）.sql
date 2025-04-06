-- 코드를 입력하세요
SELECT i.name as NAME, i.datetime as DATETIME
from animal_ins i left join animal_outs o on i.animal_id = o.animal_id
where isnull(o.datetime)
order by i.datetime asc
limit 3