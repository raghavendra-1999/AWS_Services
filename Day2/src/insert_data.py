import mysql.connector

# RDS Configuration
db_host = "mydbinstance.cjuasg0kyyl8.us-east-2.rds.amazonaws.com"
db_user = "admin"
db_password = "Raghav123"
db_name = "mydbinstance"

try:
    print(f"Connecting to {db_host}...")
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()

    # Insert data into 'employees' table
    insert_query = "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)"
    employees = [
        ("Alice Johnson", "IT", 75000.00),
        ("Bob Smith", "Finance", 80000.00),
        ("Charlie Brown", "HR", 70000.00)
    ]

    cursor.executemany(insert_query, employees)
    conn.commit()
    print(f" {cursor.rowcount} rows inserted into 'employees' table successfully!")

except mysql.connector.Error as err:
    print(f" Error: {err}")

finally:
    cursor.close()
    conn.close()
