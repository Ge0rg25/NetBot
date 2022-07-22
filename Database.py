import psycopg2


class DateB:
    def __init__(self):
        self.connection = psycopg2.connect(dbname='dek50mluj60fpc',
                                           user='fxdjzyolpwrdut',
                                           password='304e34c02ed968882d414ff29d5b7bf3e3544473ff1b07f07c1643f4096d97f9',
                                           host='ec2-176-34-215-248.eu-west-1.compute.amazonaws.com',
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

    def get_hi_msg(self):
        with self.connection:
            self.cursor.execute("SELECT hi_msg FROM other WHERE hi_msg = hi_msg")
            return self.cursor.fetchall()

    def get_hi_video(self):
        with self.connection:
            self.cursor.execute("SELECT start_video_url FROM other WHERE start_video_url = start_video_url")
            return self.cursor.fetchall()

    def get_other_resourses(self):
        with self.connection:
            self.cursor.execute("SELECT other_resourses FROM other WHERE other_resourses = other_resourses")
            return self.cursor.fetchall()
