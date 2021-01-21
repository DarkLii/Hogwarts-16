# !encoding=utf-8

import allure
import pytest
from pytest_allure.case.base_case import TestBaseCase


@allure.feature("数据驱动模块")
class TestDataDrive(TestBaseCase):

    @classmethod
    def setupClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def teardownClass(cls):
        pass

    params_list = [
        {
            "name": "张三",
            "age": "23",
            "interest": "打游戏"
        },
        {
            "name": "李四",
            "age": "18",
            "interest": "踢足球"
        },
        {
            "name": "王五",
            "age": "30",
            "interest": "健身"
        }
    ]

    ids = [f"Test Point: {items[key]}" for items in params_list for key in items.keys() if key == "name"]

    @pytest.mark.parametrize("params", params_list, ids=ids)  # ids 用于测试用例名称描述，增强日志可读性
    def test_data_drive_first(self, params):
        """
        测试用例描述：使用 @pytest.mark.parametrize 数据驱动
        """

        with allure.step("测试用例步骤：数据驱动示例"):
            """
            数据驱动示例
            """
            say = f'大家好，我是{params["name"]}，今年{params["age"]}岁，爱好：{params["interest"]}'
            self.print(say)
            self.log.info(say)

    params_list = [
        pytest.param({
            "name": "张三",
            "age": "23",
            "interest": "打游戏"
        }, id="Test Point: 张三"),  # id 用于测试用例名称描述，增强日志可读性
        pytest.param({
            "name": "李四",
            "age": "18",
            "interest": "踢足球"
        }, id="Test Point: 李四"),  # id 用于测试用例名称描述，增强日志可读性
        pytest.param({
            "name": "王五",
            "age": "30",
            "interest": "健身"
        }, id="Test Point: 王五"),  # id 用于测试用例名称描述，增强日志可读性
    ]

    @pytest.mark.parametrize("params", params_list)
    def test_data_drive_second(self, params):
        """
        测试用例描述：使用 @pytest.mark.parametrize 数据驱动
        """

        with allure.step("测试用例步骤：数据驱动示例"):
            """
            数据驱动示例
            """
            say = f'大家好，我是{params["name"]}，今年{params["age"]}岁，爱好：{params["interest"]}'
            self.print(say)
            self.log.info(say)

    params_list = [
        pytest.param({
            "name": "张三",
            "age": "23",
            "interest": "打游戏"
        }, id="Test Point: 张三"),  # id 用于测试用例名称描述，增强日志可读性
        pytest.param({
            "name": "李四",
            "age": "18",
            "interest": "踢足球"
        }, id="Test Point: 李四"),  # id 用于测试用例名称描述，增强日志可读性
        pytest.param({
            "name": "王五",
            "age": "30",
            "interest": "健身"
        }, id="Test Point: 王五"),  # id 用于测试用例名称描述，增强日志可读性
    ]

    @pytest.fixture(params=params_list)
    def input_params(self, request):
        return request.param

    def test_data_drive_third(self, input_params):
        """
        测试用例描述：使用 @pytest.fixture 数据驱动
        """

        with allure.step("测试用例步骤：数据驱动示例"):
            """
            数据驱动示例
            """
            say = f'大家好，我是{input_params["name"]}，今年{input_params["age"]}岁，爱好：{input_params["interest"]}'
            self.print(say)
            self.log.info(say)

    # 测试登录
    test_user = ["user_1", "user_2"]
    test_password = ["111111", "222222"]

    @pytest.fixture(params=test_user)
    def user(self, request):
        user = request.param
        return user

    @pytest.fixture(params=test_password)
    def password(self, request):
        password = request.param
        return password

    # 当 同一个 函数使用多个 fixture 的时候， 会对几个fixture进行组合测试每一种情况
    def test_login(self, user, password):
        """
        测试用例描述：使用 @pytest.fixture 演示登录测试
        """
        msg = f"测试数据 user: {user}， password: {password}"
        self.print(msg)
        self.log.info(msg)
