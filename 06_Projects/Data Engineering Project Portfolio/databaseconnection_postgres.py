import configparser
import psycopg2

def get_database_config(config_file_name='postgres_dbconnection.ini'):
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read(config_file_name)

    # Retrieve database details
    host = config.get('Database', 'host')
    port = config.get('Database', 'port')
    password = config.get('Database', 'password')
    dbname = config.get('Database', 'dbname')
    user = config.get('Database', 'user')

    return host, port, dbname, user, password

def get_schema_and_tables():
    # Get database configuration
    host, port, dbname, user, password = get_database_config()

    # Establish a connection to the database
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Fetch schema and tables
    cursor.execute("SELECT schema_name FROM information_schema.schemata;")
    schemas = [row[0] for row in cursor.fetchall()]

    tables_info = {}
    for schema in schemas:
        cursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{schema}';")
        tables_info[schema] = [row[0] for row in cursor.fetchall()]

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return tables_info

# Example usage
schema_tables = get_schema_and_tables()
print(schema_tables)
