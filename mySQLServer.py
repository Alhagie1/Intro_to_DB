
# Creating a database in a MySQL server
import mysql.connector
# Main Script Function
def create_database():
    db_connection = None
    cursor = None

    try:
        db_connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            port = 3306,
            passwd = "mummy12.com"
    )
        cursor = db_connection.cursor()
        
        db_name = "alx_book_store"

        sql_query = f"CREATE DATABASE IF NOT EXISTS {db_name};"
        
        cursor.execute(sql_query)
        print(f"Database '{db_name}' created successfully!")
    # The exception block   
    except mysql.connector.Error as err:
        print(f"Error: {err}")
            
    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()
            print("Database closed")


if __name__ == "__main__":
    create_database()
