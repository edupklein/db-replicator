-- Active: 1755541408006@@127.0.0.1@3307@db1
use db1;
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
    table_schema = 'db1'
GROUP BY 
    table_schema;