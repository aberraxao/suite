from sqlite3 import Error, connect


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
        :param db_file: database file
        :return: Connection object or None
    """
    try:
        conn = connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_one_row(conn, table_name, columns):
    values = '(' + ','.join('?' * len(columns)) + ')'
    sql = ' INSERT OR REPLACE INTO ' + table_name + ' VALUES' + values
    c = conn.cursor()
    c.execute(sql, columns)


def insert_many_rows(conn, table_name, columns):
    values = '(' + ','.join('?' * len(columns[0])) + ')'
    sql = ' INSERT OR REPLACE INTO ' + table_name + ' VALUES' + values
    c = conn.cursor()
    c.executemany(sql, columns)


def update_columns(conn, table_name, constrain, columns_to_update, columns):
    c = conn.cursor()
    sets = '=%s, '.join(columns_to_update) + '=%s'
    c.execute('UPDATE ' + table_name + ' SET ' + sets +
              'WHERE %s=?' % columns, (constrain,))
    conn.commit()


def fetch_value(conn, what, table_name, constrain, prms=None):
    # Check if exists in the db
    try:
        c = conn.cursor()
        sql = "SELECT " + what + " FROM " + table_name + " WHERE " + constrain
        c.execute(sql, prms)
        data = c.fetchone()
        if data is not None:
            data = data[0]
        return data
    except Error as e:
        print(e)


def fetch_all(conn, what, table_name, constrain, prms=None):
    # Check if exists in the db
    try:
        c = conn.cursor()
        sql = "SELECT " + what + " FROM " + table_name + " WHERE " + constrain
        c.execute(sql, prms)
        data = c.fetchall()
        return data
    except Error as e:
        print(e)
