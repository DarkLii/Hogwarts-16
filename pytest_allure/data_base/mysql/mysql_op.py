# -*- coding:utf-8 -*-

# @Author: DarkLi
# @Time: 2020/8/27
# @Desc: Mysql 操作封装


import pymysql
from dbutils.pooled_db import PooledDB
from pytest_allure.utiles.decorator import log_wrapper


class MysqlOp:

    def __init__(self, obj, data_base_config):

        # if hasattr(obj, "Log") and obj.Log.get("output_console", True):
        #     self.log = Logger(level='info')
        # else:
        #     self.log = None

        self.log = obj.log if hasattr(obj, "log") else None

        self.host = data_base_config["host"]
        self.port = data_base_config["port"]
        self.user = data_base_config["user"]
        self.password = data_base_config["password"]
        self.database = data_base_config["database"]
        self.charset = data_base_config.get("charset", "utf8mb4")

        # 使用流式游标，防止查询大量数据时缓存溢出，DictCursor为缓存式游标
        self.cursorclass = data_base_config.get("cursorclass", pymysql.cursors.SSDictCursor)

        self.pool = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=1,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
            maxshared=0,  # 链接池中最多共享的链接数量，0和None表示全部共享。
            # PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。

            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            setsession=[],  # 开始会话前执行的命令列表。
            ping=0,  # ping MySQL服务端，检查是否服务可用。
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset,
            cursorclass=self.cursorclass
        )

    def __connection(self):
        # 获取连接
        self.connection = self.pool.connection()
        return self.connection

    def __cursor(self):
        self.__connection()
        # 获取游标
        self.cursor = self.connection.cursor()
        return self.cursor

    def close(self):
        if self.connection:
            # 关闭连接
            self.connection.close()
            if self.log:
                self.log.info("断开 Mysql 连接")

    def execute(self, sql):
        self.__cursor()
        # 执行单条 sql 语句
        self.cursor.execute(sql)

    def execute_many(self, sql, args=[]):
        self.__cursor()
        # 执行多条 sql 语句
        self.cursor.executemany(sql, args)

    def __execute(self, sql, args=[], is_query=False, return_one=False, execute_many=False):
        # 执行sql语句
        query = False
        try:
            if execute_many:
                self.execute_many(sql, args)
            else:
                self.execute(sql)

            if is_query:
                results = self.cursor.fetchone() if return_one else self.cursor.fetchall()
                query = True
            else:
                self.connection.commit()

            is_suggess = True

        except Exception as e:
            is_suggess = False
            # 错误回滚
            self.connection.rollback()
            error = e

            if self.log:
                self.log.info(f"Sql 执行失败：{sql}")
                self.log.info(f"Sql 失败原因：{error}")
        # finally:
        #     self.close()

        if query:
            return results
        else:
            if not is_suggess:
                raise error
            else:
                return is_suggess

    @log_wrapper
    def insert(self, sql):
        # 插入数据库 执行单条语句
        return self.__execute(sql)

    @log_wrapper
    def insert_many(self, sql, args=[]):
        # 插入数据库 执行多条语句
        return self.__execute(sql=sql, args=args, execute_many=True)

    @log_wrapper
    def update(self, sql):
        # 更新数据库 执行单条语句
        return self.__execute(sql)

    @log_wrapper
    def update_many(self, sql, args=[]):
        # 更新数据库 执行多条语句
        return self.__execute(sql=sql, args=args, execute_many=True)

    @log_wrapper
    def select(self, sql):
        # 查询数据库 执行单条语句
        return self.__execute(sql=sql, is_query=True)

    @log_wrapper
    def delete(self, sql):
        # 删除数据库 执行单条语句
        return self.__execute(sql=sql)

    @log_wrapper
    def delete_many(self, sql, args=[]):
        # 删除数据库 执行多条语句
        return self.__execute(sql=sql, args=args, execute_many=True)


if __name__ == '__main__':
    data_base_config = {
        "host": "172.16.11.113",
        "port": 3306,
        "database": "emd_model",
        "user": "len_jian",
        "password": "len_jian_passwd",
    }

    data_base = MysqlOp(data_base_config)

    # 插入数据
    insert = """INSERT INTO xha001_variable_record (uid, pid) values (1, "insert_1");"""
    data_base.insert(insert)
    insert_many = """INSERT INTO xha001_variable_record (uid, pid) values (%s, %s);"""
    insert_list = [(2, "insert_2"), (3, "insert_3")]
    data_base.insert_many(insert_many, insert_list)

    # 查询数据
    query = """select * from xha001_variable_record where uid in (1, 2, 3);"""
    ret = data_base.select(query)
    query = """select * from xha001_variable_record where row_id < 2;"""
    ret = data_base.select(query)

    # 更新数据
    update = """UPDATE xha001_variable_record SET pid="update_1" WHERE uid=1;"""
    data_base.update(update)
    update_many = """UPDATE xha001_variable_record SET pid=%s WHERE uid=%s;"""
    update_list = [("update_2", 2), ("update_3", 3)]
    data_base.update_many(update_many, update_list)

    # 删除数据
    delete = """DELETE FROM xha001_variable_record WHERE uid = 1;"""
    data_base.delete(delete)
    delete = """DELETE FROM xha001_variable_record WHERE uid = %s;"""
    delete_list = [(2), (3)]
    data_base.delete_many(delete, delete_list)
