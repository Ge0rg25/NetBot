import psycopg2


class DateB:
    def __init__(self):
        self.connection = psycopg2.connect(dbname='d6pbbu8ltmfueb',
                                           user='rjnlyhjbwbnhit',
                                           password='72b1af9fffd9dff71bf45874851a3af2d80d835d97b059b0767cc0008b04e7fb',
                                           host='ec2-3-248-121-12.eu-west-1.compute.amazonaws.com',
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

    def get_short_vidios(self, group):
        with self.connection:
            self.cursor.execute("SELECT url FROM short_videos WHERE group_name = %s", (group, ))
            return self.cursor.fetchall()

    def get_long_vidios(self, group):
        with self.connection:
            self.cursor.execute("SELECT url FROM long_videos WHERE group_name = %s", (group, ))
            return self.cursor.fetchall()
