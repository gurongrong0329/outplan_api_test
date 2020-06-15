import pymysql

class DbServer:
    conn = None

    def __init__(self, address='192.168.88.53', user='root', pswd='kalamodo', db='etc_middle_office_coupon'):
        self.address = address
        self.user = user
        self.pswd = pswd
        self.db = db

    # 连接数据库
    def connect_db(self):
        if self.conn is None:
            self.conn = pymysql.connect(host=self.address,
                                        user=self.user,
                                        password=self.pswd,
                                        database=self.db,
                                        charset='utf8')
        return self.conn

    # 获取游标对象
    def get_cursor(self):
        return self.connect_db().cursor()

    # 关闭游标对象
    def close_cursor(self, cursor):
        if cursor:
            cursor.close()

    # 关闭数据库连接
    def close_conn(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def get_sql_one(self, sql):
        sursor = None
        data = None
        try:
            sursor = self.get_cursor()
            sursor.execute(sql)
            data = sursor.fetchone()
        except Exception as e:
            print("get_sql_one error:", e)
        finally:
            self.close_cursor(sursor)
            self.close_conn()
            return data

    def get_sql_all(self, sql):
        sursor = None
        data = None
        try:
            sursor = self.get_cursor()
            sursor.execute(sql)
            data = sursor.fetchall()
        except Exception as e:
            print("get_sql_one error:", e)
        finally:
            self.close_cursor(sursor)
            self.close_conn()
            return data

    def delete_sql(self, sql):
        sursor = None
        try:
            sursor = self.get_cursor()
            sursor.execute(sql)
            self.conn.commit()  # 事务提交
        except Exception as e:
            self.conn.rollback()  # 回滚
            print("get_sql_one error:", e)
        finally:
            self.close_cursor(sursor)
            self.close_conn()

    def add_sql(self, sql):
        sursor = None
        try:
            sursor = self.get_cursor()
            sursor.execute(sql)
            self.conn.commit()  # 事务提交
        except Exception as e:
            self.conn.rollback()  # 回滚
            print("get_sql_one error:", e)
        finally:
            self.close_cursor(sursor)
            self.close_conn()

    def update_sql(self, sql):
        sursor = None
        try:
            sursor = self.get_cursor()
            sursor.execute(sql)
            self.conn.commit()  # 事务提交
        except Exception as e:
            self.conn.rollback()  # 回滚
            print("get_sql_one error:", e)
        finally:
            self.close_cursor(sursor)
            self.close_conn()
