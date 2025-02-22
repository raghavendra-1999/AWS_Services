import mysql.connector

# RDS Configuration
db_host = "mydbinstance.cjuasg0kyyl8.us-east-2.rds.amazonaws.com"  # Your RDS endpoint
db_user = "admin"  # Master username
db_password = "Raghav123"  # Your master password
db_name = "mydbinstance"  # Ensure this database exists, or use `None` first

try:
    print(f"Attempting to connect to {db_host}...")

    # Connect to MySQL without specifying a database first
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password
    )
    cursor = conn.cursor()
    print(" Connection successful!")

    # Check if the database exists
    cursor.execute("SHOW DATABASES;")
    databases = [db[0] for db in cursor.fetchall()]
    
    if db_name not in databases:
        print(f" Database '{db_name}' not found. Creating it now...")
        cursor.execute(f"CREATE DATABASE {db_name};")
        print(f" Database '{db_name}' created successfully!")

    # Now connect to the specific database
    conn.database = db_name
    print(f"Switched to database: {db_name}")

    # Get MySQL version
    cursor.execute("SELECT VERSION();")
    version = cursor.fetchone()
    print(f"MySQL version: {version[0]}")

except mysql.connector.Error as err:
    print(f" Error: {err}")

finally:
    # Ensure cursor and connection are closed properly
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
