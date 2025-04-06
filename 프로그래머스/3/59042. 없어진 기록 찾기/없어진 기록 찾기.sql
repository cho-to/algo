-- 코드를 입력하세요
SELECT o.animal_id as ANIMAL_ID, o.name as NAME
from animal_ins i right join animal_outs o on i.animal_id = o.animal_id
where isnull(i.intake_condition)