import os

import jaydebeapi


def get_starburst_connection():
    # Path to the JDBC driver jar file
    driver_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trino-jdbc-448-e.jar')

    # Connection parameters (replace placeholders with actual values)
    url = 'jdbc:trino://thenumerix-boa.trino.galaxy.starburst.io:443'
    user = 'kecho001@ucr.edu/accountadmin'
    password = 'StreetScience11!'  # Replace with your actual password

    # Load JDBC driver and establish connection
    conn = jaydebeapi.connect(
        'io.trino.jdbc.TrinoDriver',
        url,
        {'user': user, 'password': password},
        driver_path
    )
    
    return conn

def execute_query(query):
    conn = get_starburst_connection()
    curs = conn.cursor()
    curs.execute(query)
    result = curs.fetchall()
    curs.close()
    conn.close()
    return result
