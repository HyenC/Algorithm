SELECT P.product_name, S.year, s.price
FROM Sales S
    JOIN Product P ON S.product_id = P.product_id
