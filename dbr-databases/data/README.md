# 🗄️ Databases Backup Files

This folder contains the backup files for both the source1 (db1) and source2 (db2) databases.
Follow the instructions bellow to populate the databases with the backup data.

## 🚀 Usage

1. Clone the repository:
   ```bash
    git clone https://github.com/edupklein/db-replicator.git
   ```
1. Navigate to the project directory:
   ```bash
   cd dbr-databases/data
   ```
1. Run the following command to unzip the source 1 db data (db1):
    ```bash
   gunzip < ./backups/source1_backup.sql.gz | docker exec -i dbr-databases-mysql_source1-1 mysql -u root -proot1 db1
   ```
1. Run the following command to unzip the source 2 db data (db2):
    ```bash
   gunzip < ./backups/source2_backup.sql.gz | docker exec -i dbr-databases-mysql_source2-1 mysql -u root -proot2 db2
   ```

This will populate both db1 and db2 with backed up data from the populate_sources Python script.

## 📁 Creating a Backup

To create a new backup from the current database data, run the following commands:

1. Create a backup file for the source 1 db data (db1):
    ```bash
   docker exec -i dbr-databases-mysql_source1-1 mysqldump -u root -proot1 db1 | gzip > ./backups/source1_backup.sql.gz
   ```
1. Create a backup file for the source 2 db data (db2):
    ```bash
   docker exec -i dbr-databases-mysql_source2-1 mysqldump -u root -proot2 db2 | gzip > ./backups/source2_backup.sql.gz
   ```