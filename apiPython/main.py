import pymysql 


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
           host='localhost',
           user='root',
           password='',
           db='demo' 
        )

        self.cursor = self.connection.cursor()

    def select_user(self, id):
        sql = 'SELECT id, username, email FROM users WHERE id = {}'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("Id:", user[0])
            print("Username:", user[1])
            print("Email:", user[2])
            
        except Exception as e :
            raise

    def select_user(self, id):

        sql = 'SELECT id, username, email FROM users '

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()

            for user in users:
                print("Id:", user[0])
                print("Username:", user[1])
                print("Email:", user[2])
                print("________\n")
            
        except Exception as e :
            raise

    def update_user(self, id, username):
        sql = "UPDATE users SET username='{}' WHERE id = {} ".format(username, id)
        try:
            self.cursor.execute(sql)
        except Exception as e :
            raise




database = DataBase()
database.select_user(1)

database.update_user(1, 'Cambio de nombre! ')

database.select_user(1)