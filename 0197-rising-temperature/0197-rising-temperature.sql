SELECT today.id AS Id
FROM Weather AS today
    JOIN Weather AS yesterday ON DATE_ADD(yesterday.recordDate, INTERVAL 1 DAY) = today.recordDate
WHERE today.temperature > yesterday.temperature