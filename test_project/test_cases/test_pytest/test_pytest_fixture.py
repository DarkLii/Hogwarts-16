# -*- coding:utf-8 -*-
import allure
import pytest
from pytest_allure.case.base_case import TestBaseCase


# PS：可将 fixture 装饰的函数统一管理在 conftest.py 文件中，conftest.py 文件的作用域是当前包内及其子包
# 函数调用固件优先从当前测试类（class）中寻找 --> 然后是模块（.py文件）中 --> 接着是当前包中寻找（conftest.py中） --> 如果没有再找父包直至根目录
# 如果要声明全局的 conftest.py 文件，可以将其放项目在根目录下

@allure.feature("fixture 示例")
class TestFixture(TestBaseCase):

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

    def test_data_drive(self, input_params):
        """
        测试用例描述：使用 @pytest.fixture 数据驱动
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
        测试用例描述：使用 @pytest.fixture 数据驱动演示登录测试
        """
        msg = f"测试数据 user: {user}， password: {password}"
        self.print(msg)
        self.log.info(msg)

    # 实现单个用例的 setUp 和 tearDown
    @pytest.fixture(scope="function", autouse=False)  # autouse=Ture 时，默认每个用例都使用该 fixture
    def setup_teardown(self):
        msg = "测试用例 执行前 执行：Run Test Case SetUp"
        self.print(msg)
        self.log.info(msg)
        self.setup_info = "SetUp 创建的资源"
        yield
        msg = "测试用例 执行后 执行：Run Test Case TearDown"
        self.print(msg)
        self.log.info(msg)

    def test_setup_teardown(self, setup_teardown):
        self.print(f"Test Case 访问: {self.setup_info}")
        self.log.info(f"Test Case 访问: {self.setup_info}")
        msg = "执行 测试用例：Run Test Case"
        self.print(msg)
        self.log.info(msg)

    @pytest.fixture(scope="function")  # autouse=Ture 时，默认每个用例都使用该 fixture
    def test_case_1(self):
        self.ret = "This is case_1 value"
        print(f"test_case_1:{self.ret}")

    @pytest.fixture(scope="function")  # autouse=Ture 时，默认每个用例都使用该 fixture
    def test_case_2(self, test_case_1):
        print(f"test_case_2:{self.ret}")

    def test_case_3(self, test_case_2):
        print(f"test_case_3:{self.ret}")


class TestFixTure:

    def test_one(self, test_class_fixture):
        print("执行：test_one")

    def test_two(self, test_case_fixture):
        print("执行：test_two")

    def test_three(self, test_case_fixture_return):
        print(f"获取 fixture 的参数:{test_case_fixture_return}")
        print("执行：test_three")
        print("执行：test_two")

    def test_four(self, test_case_fixture_yield):
        print(f"获取 fixture 的参数:{test_case_fixture_yield}")
        print("执行：test_three")
