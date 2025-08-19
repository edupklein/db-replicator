docker exec -i dbr-databases-mysql_source1-1 mysqldump -u root -proot1 db1 | gzip > ./data/backups/source1_backup.sql.gz

gunzip < ./data/backups/source1_backup.sql.gz | docker exec -i dbr-databases-mysql_source1-1 mysql -u root -proot1 db1
gunzip < ./data/backups/source2_backup.sql.gz | docker exec -i dbr-databases-mysql_source2-1 mysql -u root -proot2 db2
