import mysql.connector

# RDS Configuration
db_host = "mydbinstance.cjuasg0kyyl8.us-east-2.rds.amazonaws.com"  # Your RDS endpoint
db_user = "admin"  # Master username
db_password = "Raghav123"  # Your master password
db_name = "mydbinstance"  # Ensure this database exists

try:
    print(f"Connecting to {db_host}...")
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()

    # Create 'employees' table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        department VARCHAR(50),
        salary DECIMAL(10,2)
    );
    """
    cursor.execute(create_table_query)
    print("Table 'employees' created successfully!")

except mysql.connector.Error as err:
    print(f" Error: {err}")

finally:
    cursor.close()
    conn.close()
