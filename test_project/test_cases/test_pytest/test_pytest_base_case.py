# !encoding=utf-8

import allure
from pytest_allure.http_op.http import Http
from pytest_allure.http_op.httpx import HttpX
from pytest_allure.case.base_case import TestBaseCase
from pytest_allure.utiles.dict_operate import get_dict_value, update_dict
from pytest_allure.data_base.data_base_interface import data_base_connection


@allure.feature("模块名称，用于描述一个class--模块级")
class TestPyTest(TestBaseCase):

    @classmethod
    def setupClass(cls):
        cls.http = Http(obj=cls)
        cls.http_x = HttpX(obj=cls)
        # # Redis 操作
        # redis_db_info = "redis_13"
        # cls.redis_db = data_base_connection(cls, redis_db_info)
        # # Msql 操作
        # mysql_db_info = "emd_model"
        # cls.mysql_db = data_base_connection(cls, mysql_db_info)
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def teardownClass(cls):
        cls.http.close()
        cls.http_x.close()
        # cls.mysql_db.close()
        pass

    @allure.title("测试用例标题：测试用例示例")
    @allure.description("测试用例描述：此用例用于示例日志使用、部分工具使用等")
    def test_case_eg(self):
        """
        测试用例描述：此用例用于示例日志使用、部分工具使用等
        PS：会被 @allure.description 内容覆盖
        """

        with allure.step("测试用例步骤：Http 请求示例"):
            """
            Http 请求示例
            """
            ret1 = self.http.post(url="https://www.baidu.com")
            ret = self.http_x.get(url="http://m.gaosan.com/gaokao/265440.html")
            print(1)

        # with allure.step("测试用例步骤：日志示例"):
        #     """
        #     日志示例
        #     """
        #     self.print("Print 调试日志")
        #     self.log.debug("Debug      日志")
        #     self.log.info("Info       日志")
        #     self.log.warning("Warning    日志")
        #     self.log.error("Error      日志")
        #     try:
        #         raise ValueError('An error happend !')
        #     except ValueError as e:
        #         self.log.exception("Exception 日志")
        #         pass
        #     self.log.critical("Critical   日志")
        #     self.allure_log.text(title="Allure Log", message="Allure Text Message")

        # with allure.step("测试用例步骤：Dict 操作示例"):
        #     """
        #     Dict 操作示例
        #     """
        #     test_dict = {
        #         "a": 0,
        #         "b": {"c": 1},
        #         "d": [{"e": 2}]
        #     }
        #
        #     # 更新 Dict
        #     key_values = {
        #         "a": 1,
        #         "b.c": 2,
        #         "c": 3,
        #         "d.0.e": 3,
        #         "d.1.f": 4,
        #         "g.h": 5,
        #         "i.0.j": 6,
        #         "i.1.k.0": 7
        #     }
        #     ret = update_dict(test_dict, key_values)
        #
        #     # 根据 key_path 从 Dict 获取 Value
        #     key_path_list = [
        #         "a",
        #         "b",
        #         "c",
        #         "b.c",
        #         "d",
        #         "d.0",
        #         "d.0.e",
        #         "x.0.c"
        #     ]
        #     breadth_ret = get_dict_value(test_dict, key_path_list, is_ignore_real_path=1)
        #     self.allure_log.text(title="Breadth First Search", message=breadth_ret)
        #     depth_ret = get_dict_value(test_dict, key_path_list, is_ignore_real_path=1, is_depth_first_search=1)
        #     self.allure_log.text(title="Depth First Search", message=depth_ret)

        # with allure.step("测试用例步骤：数据库操作示例"):
        #     """
        #     数据库操作示例
        #     """
        #     with allure.step("测试用例步骤：Redis 操作"):
        #         # Redis 操作
        #
        #         test_key = "test_key"
        #         test_value = "test_value"
        #         self.redis_db.set(test_key, test_value)
        #         self.redis_db.get(test_key)
        #
        #         key_value_dict = {
        #             "mset_key_1": {"mset_key_111": "mset_value_111"},
        #             "mset_key_2": {"mset_key_222": "mset_value_222"},
        #         }
        #         self.redis_db.mset(key_value_dict)
        #
        #         key_list = [test_key, "mset_key_1", "mset_key_2"]
        #         self.redis_db.mdelete(key_list)
        #
        #     with allure.step("测试用例步骤：Mysql 操作"):
        #         # Mysql 操作
        #
        #         # 插入数据
        #         insert = """INSERT INTO xha001_variable_record (uid, pid) values (1, "insert_1");"""
        #         self.mysql_db.insert(insert)
        #         insert_many = """INSERT INTO xha001_variable_record (uid, pid) values (%s, %s);"""
        #         insert_list = [(2, "insert_2"), (3, "insert_3")]
        #         self.mysql_db.insert_many(insert_many, insert_list)
        #
        #         # 查询数据
        #         query = """select * from xha001_variable_record where uid in (1, 2, 3);"""
        #         ret = self.mysql_db.select(query)
        #         self.allure_log.text(title="DataBase Select", message=ret)
        #         query = """select * from xha001_variable_record where row_id < 2;"""
        #         ret = self.mysql_db.select(query)
        #         self.allure_log.text(title="DataBase Select", message=ret)
        #
        #         # 更新数据
        #         update = """UPDATE xha001_variable_record SET pid="update_1" WHERE uid=1;"""
        #         self.mysql_db.update(update)
        #         update_many = """UPDATE xha001_variable_record SET pid=%s WHERE uid=%s;"""
        #         update_list = [("update_2", 2), ("update_3", 3)]
        #         self.mysql_db.update_many(update_many, update_list)
        #
        #         # 删除数据
        #         delete = """DELETE FROM xha001_variable_record WHERE uid = 1;"""
        #         self.mysql_db.delete(delete)
        #         delete = """DELETE FROM xha001_variable_record WHERE uid = %s;"""
        #         delete_list = [(2), (3)]
        #         self.mysql_db.delete_many(delete, delete_list)

        pass
