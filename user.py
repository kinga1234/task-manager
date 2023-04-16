import psycopg2


class User:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def create_table(self):
        sql_users = '''CREATE TABLE IF NOT EXISTS users
               (id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL)'''
        with psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        ) as conn, conn.cursor() as cur:
            cur.execute(sql_users)

    def add_user(self, name):
        sql = "INSERT INTO users (name) VALUES (%s)"
        values = (name,)
        with psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        ) as conn, conn.cursor() as cur:
            cur.execute(sql, values)

    def get_users(self):
        sql = "SELECT * FROM users"
        with psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        ) as conn, conn.cursor() as cur:
            cur.execute(sql)
            users = cur.fetchall()
        return users
