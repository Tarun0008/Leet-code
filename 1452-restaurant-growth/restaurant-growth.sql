SELECT 
    A.visited_on,
    SUM(B.amount) AS amount,
    ROUND(SUM(B.amount) / 7, 2) AS average_amount
FROM 
    (SELECT DISTINCT visited_on FROM Customer) A
JOIN 
    Customer B 
    ON B.visited_on BETWEEN DATE_SUB(A.visited_on, INTERVAL 6 DAY) AND A.visited_on
GROUP BY 
    A.visited_on
HAVING 
    COUNT(DISTINCT B.visited_on) = 7  -- Ensure 7 continuous days are present
ORDER BY 
    A.visited_on;
