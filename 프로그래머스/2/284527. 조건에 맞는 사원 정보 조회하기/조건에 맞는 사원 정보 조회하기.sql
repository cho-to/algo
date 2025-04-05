-- 코드를 작성해주세요
SELECT 
    SUM(g.score) AS SCORE, 
    e.emp_no AS EMP_NO, 
    e.emp_name AS EMP_NAME, 
    e.position AS POSITION, 
    e.email AS EMAIL
FROM 
    hr_department d
INNER JOIN 
    hr_employees e ON d.dept_id = e.dept_id
INNER JOIN 
    hr_grade g ON e.emp_no = g.emp_no
GROUP BY 
    e.emp_no, e.emp_name, e.position, e.email
ORDER BY 
    SCORE DESC
limit 1