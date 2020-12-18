import time
import yaml
from selenium import webdriver


# ��ȡcookie�����л������yaml�ļ���
def test_get_cookie(obj):

    obj.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    cookie = obj.driver.get_cookies()
    print(cookie)
    with open("data.yaml", "w", encoding="UTF-8") as f:
        yaml.dump(cookie, f)
    print()


# ʹ�����л�cookie�ķ������е�¼
def test_login(obj):

    obj.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open("data.yaml", encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            obj.driver.add_cookie(cookie)
