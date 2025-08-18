-- Active: 1755541600708@@127.0.0.1@3308@db2
use db2;
select *
from clients

select count(id)
from clients

select *
from users

select count(id)
from users

SELECT 
    table_schema AS database_name,
    SUM(data_length + index_length) AS size_bytes
FROM 
    information_schema.tables
WHERE 
    table_schema = 'db2'
GROUP BY 
    table_schema;