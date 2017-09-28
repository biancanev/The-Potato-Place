DECLARE @counter smallint;  
SET @counter = 1;  
WHILE @counter < 5  
   BEGIN  
      SELECT RAND() Random_Number  
      SET @counter = @counter + 1  
   END;  
GO  
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition; 
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2; 
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City; 
