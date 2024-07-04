SELECT M.name
FROM Employee AS M
JOIN (SELECT managerId, COUNT(*) AS cnt
      FROM Employee
      GROUP BY managerId) AS E ON M.id = E.managerId
WHERE E.cnt >= 5;