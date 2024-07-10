SELECT P.project_id, 
       ROUND(COALESCE(SUM(E.experience_years) / COUNT(*), 0), 2) AS average_years
FROM Project P
    LEFT JOIN Employee E ON P.employee_id = E.employee_id
GROUP BY P.project_id