# 🐍 Python scripts

Python scripts used for DB manipulation and data creation. 

The script populate_sources.py is used to generate fake data for the databases bellow:
- db1, inside the container mysql_source1
- db2, inside the container mysql_source2

## 🚀 Usage

1. Clone the repository:
   ```bash
       git clone https://github.com/edupklein/db-replicator.git
   ```
1. Navigate to the project directory:
   ```bash
   cd dbr-databases/scripts
   ```
1. Setting up dependencies:
   - Install [python3.13](https://www.python.org/downloads/release/python-3130/)
   - Install python3 dependencies
   ```bash
   python3 -m pip install mysql-connector-python faker tqdm
   ```
1. Open terminal and run `populate_scripts.py`:
   ```bash
   python3 populate_scripts.py
   ```
1. If you need to clear the database's data to run the script again, you can just remove the containers with their respective volumes and run them again:
   ```bash
   cd ..
   docker compose down -v
   docker compose up -d
   ```
