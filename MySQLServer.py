# -- Creating a database in MySQL server

# The python mysql connector
import mysql.connector

#  -- Main function for creating databases
def create_database():
    """
    Connects to the MySQL server and creates a database named 'alx_book_store'
    if it does not already exist.
    """
    db_connection = None
    cursor = None

    try:
        db_connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            port = 3306,
            password = "mummy12.com"
        )

        cursor = db_connection.cursor()

        db_name = "alx_book_store"
        sql_query = f"CREATE DATABASE IF NOT EXISTS {db_name};"
        cursor.execute(sql_query)
        print(f"Database '{db_name}' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()
            print("Database connection closed.")


if __name__ == "__main__":
    create_database()
