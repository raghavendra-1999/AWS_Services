import mysql.connector

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

    # Fetch and display data
    cursor.execute("SELECT * FROM employees;")
    rows = cursor.fetchall()

    print("\n Data in 'employees' table:")
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    conn.close()
