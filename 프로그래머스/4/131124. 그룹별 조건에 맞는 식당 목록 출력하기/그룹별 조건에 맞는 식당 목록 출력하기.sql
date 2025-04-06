-- 코드를 입력하세요
SELECT m.member_name as MEMBER_NAME, r.review_text as REVIEW_TEXT, date_format(r.review_date, '%Y-%m-%d') as REVIEW_DATE
from member_profile m 
    inner join rest_review r on m.member_id = r.member_id
    inner join (
        select member_id, count(*)
        from rest_review
        group by member_id
        order by 2 desc
        limit 1
    ) r1 on m.member_id = r1.member_id
order by 3 asc, 2 asc