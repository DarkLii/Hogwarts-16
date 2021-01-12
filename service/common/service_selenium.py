import os
import time
import yaml
from selenium import webdriver

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def we_weixin_login_cookie_file_path():
    # ���ر��� we_weinxin ��ҳ���½ cookie ���ļ�·��
    return os.path.join(PROJECT_PATH, "data/we_weixin_login_cookie.yaml")


# ��ȡcookie�����л������yaml�ļ���
def test_get_cookie(obj):
    obj.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    cookie = obj.driver.get_cookies()
    print(cookie)
    with open(we_weixin_login_cookie_file_path(), "w", encoding="UTF-8") as f:
        yaml.dump(cookie, f)


# ʹ�����л�cookie�ķ������е�¼
def test_login(obj):
    obj.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open(we_weixin_login_cookie_file_path(), encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            obj.driver.add_cookie(cookie)
