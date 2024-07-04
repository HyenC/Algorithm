SELECT a.machine_id,  
	   ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity as a
    JOIN (SELECT *
          FROM activity
          WHERE activity_type = "end"
          GROUP BY machine_id, process_id) AS b ON a.machine_id = b.machine_id
WHERE a.activity_type = "start"
GROUP BY a.machine_id;