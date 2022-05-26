import psycopg2


class DateB:
    def __init__(self):
        self.connection = psycopg2.connect(dbname='NetBD',
                                           user='postgres',
                                           password='G',
                                           host='localhost',
                                           port="5432")
        self.cursor = self.connection.cursor()

    # ------------------------- Проверка есть ли пользоватеь в бд -----------------------------------------

    def user_exists(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
            res = self.cursor.fetchall()
            return bool(len(res))

    # ---------------------- Взять всех пользователей из бд -------------------------
    def get_users(self):
        with self.connection:
            self.cursor.execute("SELECT user_id FROM users")
            return self.cursor.fetchall()

        # ----------------- ------- Добавление пользователя ----------------------------------------------------

    def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
            check = self.cursor.fetchall()
            res = bool(len(check))
            if not res:
                return self.cursor.execute("INSERT INTO users (user_id) VALUES(%s)", (user_id,))

    def get_all_group(self):
        with self.connection:
            self.cursor.execute('SELECT group_name FROM groups')
            return self.cursor.fetchall()



