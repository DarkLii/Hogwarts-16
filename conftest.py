# -*- coding:utf-8 -*-
import pytest


# @pytest.fixture(scope="class")
@pytest.fixture(autouse=True, scope="class")
def test_class_fixture():
    print("测试套执行前 执行：test_class_fixture")  # test suit_setup
    yield
    print("测试套执行后 执行：test_class_fixture")  # test suit_teardown


@pytest.fixture(autouse=True, scope="module")
def test_module_fixture():
    print("测试套执行前 执行：test_module_fixture")
    yield
    print("测试套执行后 执行：test_module_fixture")


@pytest.fixture(params=["fixture 方法参数1", "fixture 方法参数2"])
def test_case_fixture_return(request):
    print("用例执行前 执行：test_case_fixture")
    return request.param  # 需要返回的时候加
    # yield request.param  # 也可使用 yield


@pytest.fixture(autouse=False)
def test_case_fixture():
    print("\nStart Run: setup")  # test case setup
    yield
    print("\nStart Run: teardown")  # test case teardown


@pytest.fixture(params=["fixture 方法参数1", "fixture 方法参数2"])
def test_case_fixture_yield(request):
    print("用例执行前 执行：test_case_fixture")  # test case setup
    yield request.param  # 类似 return ，当需要返回且需要执行 teardown 时用 yield
    print("用例执行后 执行：test_case_fixture")  # test case teardown


# hook 函数
def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")  # 解决测试用例名字是中文时，打印日志为unicode的情况
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")  # 解决测试用例名字是中文时，打印日志为unicode的情况
