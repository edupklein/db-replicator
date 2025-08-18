# Databases DB Images

This docker compose file uses the `mysql:8.0` image to create 3 mysql images with the following structure inside the dbr-databases container:
- image: mysql_source1 -> inside there is database db1 with following connection info:
    - host = 'localhost'
    - user = 'root'
    - port = 3307 
    - password = 'root1'
    - database = 'db1'

- image: mysql_source2 -> inside there is database db2 with following connection info:
    - host = 'localhost'
    - user = 'root'
    - port = 3308 
    - password = 'root2'
    - database = 'db2'

- image: mysql_target -> inside there is database db_target with following connection info:
    - host = 'localhost'
    - user = 'root'
    - port = 3309 
    - password = 'root3'
    - database = 'db_target'

## Usage

1. Clone the repository:
   ```bash
       git clone https://github.com/edupklein/db-replicator.git
   ```
1. Navigate to the project directory:
   ```bash
   cd dbr-databases
   ```
1. Run docker the docker image:
    ```bash
   docker compose up -d
   ```

Databases started:
db1, db2, db_target

## Structure

1. When running the docker compose file, the sql commands inside dbr-databases/sql/init will create 2 tables in each database, tables:
    - clients
    - users
1. Initially the tables will have no data. To generate data, you can use the backup files inside 'data' folder and follow the README file inside this folder.
1. Or alternatively you can run a Python script the generate fake data. To do this, navigate to the 'scripts' folder and follow the README file inside this folder.
