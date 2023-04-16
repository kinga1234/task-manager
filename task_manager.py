import psycopg2


class TaskManager:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()

    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS tasks
               (id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id),
                name VARCHAR(255) NOT NULL,
                description TEXT,
                deadline DATE,
                status INTEGER NOT NULL)'''
        self.cur.execute(sql)
        self.conn.commit()

    def add_task(self, user_id, name, description, deadline, status):
        sql = "INSERT INTO tasks (user_id, name, description, deadline, status) VALUES (%s, %s, %s, %s, %s)"
        values = (user_id, name, description, deadline, status)
        self.cur.execute(sql, values)
        self.conn.commit()

    def update_task(self, task_id, name=None, description=None, deadline=None, status=None):
        set_sql = []
        values = []
        if name:
            set_sql.append("name = %s")
            values.append(name)
        if description:
            set_sql.append("description = %s")
            values.append(description)
        if deadline:
            set_sql.append("deadline = %s")
            values.append(deadline)
        if status:
            set_sql.append("status = %s")
            values.append(status)
        set_sql = ", ".join(set_sql)
        sql = f"UPDATE tasks SET {set_sql} WHERE id = %s"
        values.append(task_id)
        self.cur.execute(sql, values)
        self.conn.commit()

    def delete_task(self, task_id):
        sql = "DELETE FROM tasks WHERE id = %s"
        values = (task_id,)
        self.cur.execute(sql, values)
        self.conn.commit()

    def get_tasks(self, user_id):
        sql = "SELECT * FROM tasks WHERE user_id = %s"
        values = (user_id,)
        self.cur.execute(sql, values)
        tasks = self.cur.fetchall()
        return tasks
