-- 코드를 작성해주세요
select a.id as ID, b.FISH_NAME as FISH_NAME, a.length as LENGTH
from fish_info a
inner join fish_name_info b on a.fish_type = b.fish_type
where a.length = (
    select max(length)
    from fish_info
    where a.fish_type = fish_type
)
order by id asc