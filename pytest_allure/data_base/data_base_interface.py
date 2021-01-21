# -*- coding: utf-8 -*-

# @Author: DarkLi
# @Time  : 2020/8/28
# @Desc  : DataBase 封装


from pytest_allure.data_base.mysql.mysql_op import MysqlOp
from pytest_allure.data_base.redis.redis_op import RedisOp


def data_base_connection(obj, db_info):
    """
    根据入参实例化数据库连接
    :param obj: 测试用例对象
    :param db_info: 需要实例化的数据库
    :return: 实例化的数据库连接
    """
    if hasattr(obj, "DataBase"):
        data_base_info = obj.DataBase.get(db_info, None)
        if not data_base_info:
            raise AttributeError(f"{obj.DataBase} has no attribute {db_info}")

        if data_base_info["engine"].upper() == "REDIS":
            return RedisOp(obj, data_base_info)
        elif data_base_info["engine"].upper() == "MYSQL":
            return MysqlOp(obj, data_base_info)
    else:
        raise AttributeError(f"{obj} has no attribute DataBase")


class Test:
    def __init__(self):
        self.DataBase = {
            "redis_1" : {
                "engine"  : "redis",
                "host"    : "xxx",
                "port"    : 6379,
                "database": 1,
                "user"    : "xxx",
                "password": "xxx",
            },
            "mysql_1": {
                "engine"  : "mysql",
                "host"    : "xxx",
                "port"    : 3306,
                "database": "xxx",
                "user"    : "xxx",
                "password": "xxx",
            },
        }


if __name__ == '__main__':
    data_base = "redis_13"

    test = Test()

    db = data_base_connection(test, data_base)

    test_key = "test_key"
    test_value = "test_value"
    db.set(test_key, test_value)
    data_base.get(test_key)

    key_value_dict = {
        "mset_key_1": {"mset_key_111": "mset_value_111"},
        "mset_key_2": {"mset_key_222": "mset_value_222"},
    }
    db.mset(key_value_dict)

    key_list = [test_key, "mset_key_1", "mset_key_2"]
    db.mdelete(key_list)

    data_base = "mysql_1"

    test = Test()

    db = data_base_connection(test, data_base)

    # 插入数据
    insert = """INSERT INTO xxx (uid, pid) values (1, "insert_1");"""
    db.insert(insert)
    insert_many = """INSERT INTO xxx (uid, pid) values (%s, %s);"""
    insert_list = [(2, "insert_2"), (3, "insert_3")]
    db.insert_many(insert_many, insert_list)

    # 查询数据
    query = """select * from xxx where uid in (1, 2, 3);"""
    ret = db.select(query)
    query = """select * from xxx where row_id < 2;"""
    ret = db.select(query)

    # 更新数据
    update = """UPDATE xxx SET pid="update_1" WHERE uid=1;"""
    db.update(update)
    update_many = """UPDATE xxx SET pid=%s WHERE uid=%s;"""
    update_list = [("update_2", 2), ("update_3", 3)]
    db.update_many(update_many, update_list)

    # 删除数据
    delete = """DELETE FROM xxx WHERE uid = 1;"""
    db.delete(delete)
    delete = """DELETE FROM xxx WHERE uid = %s;"""
    delete_list = [(2), (3)]
    db.delete_many(delete, delete_list)
