class DBApiNotFound(Exception):
    def __init__(self, conn_string):
        dialect_to_db_apis = {
            'oracle+cx_oracle': 'cx_Oracle',
            'mysql': 'MySQL-python',
            'postgresql': 'psycopg2',
            'mssql+pyodbc': 'pyodbc',
            'sqlite': 'sqlite3'
        }
        dialect = conn_string.split(":")[0]
        db_api = dialect_to_db_apis.get(dialect) or "No driver found for dialect '{0}'".format(dialect)
        self.msg = """
        ************************************************************************************************************************\r
        ** While creating the engine for '{0}', SQLAlchemy tried to import the DB API module '{1}' but failed.\r
        ************************************************************************************************************************\r
        ** This is because 1 of 2 reasons:\r
        **  --> 1.) You forgot to install the DB API module '{1}'. (Try: 'pip install {1}')\r
        **  --> 2.) If the above step fails, you most likely forgot to install the actual database driver\r
        **  --> on your local machine! The driver is needed in order to install the Python DB API ('{1}')\r
        **  --> (see 'https://seanharr11.github.io/installing-database-drivers' for instructions!!)\r
        ************************************************************************************************************************ 
        """.format(conn_string, db_api)
    def __str__(self):
        return self.msg