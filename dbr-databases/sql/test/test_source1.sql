use db1;
select *
from client;

select count(id)
from client;

select *
from user;

select count(id)
from user;

SELECT 
    table_schema AS database_name,
    SUM(data_length + index_length) AS size_bytes
FROM 
    information_schema.tables
WHERE 
    table_schema = 'db1'
GROUP BY 
    table_schema;