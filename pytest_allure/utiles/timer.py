# -*- coding: utf-8 -*-

# @Author: DarkLi
# @Time  : 2020/8/15
# @Desc  : time、datetime 相关封装

import datetime
import time

DATETIME_FORMAT_S = "%Y-%m-%d %H:%M:%S"
DATETIME_FORMAT_MS = "%Y-%m-%d %H:%M:%S.%f"
TIME_FORMAT = "%H:%M:%S"


# 当前毫秒数
def cur_seconds():
    return int(time.time())


# 当前日期：%Y-%m-%d %H:%M:%S
def cur_datetime():
    return datetime.datetime.strftime(datetime.datetime.now(), DATETIME_FORMAT_S)


# 当前日期(微妙)：%Y-%m-%d %H:%M:%S.%f
def cur_datetime_ms():
    return datetime.datetime.strftime(datetime.datetime.now(), DATETIME_FORMAT_MS)


# 当前日期：%Y-%m-%d
def cur_date():
    return datetime.date.today()


# 当前年
def cur_yuar():
    return datetime.datetime.now().year


# 当前月
def cur_month():
    return datetime.datetime.now().month


# 当前日
def cur_day():
    return datetime.datetime.now().day


# 当前小时
def cur_hour():
    return datetime.datetime.now().hour


# 当前分钟
def cur_minute():
    return datetime.datetime.now().minute


# 当前秒
def cur_second():
    return datetime.datetime.now().second


# 当前星期几
def cur_week():
    return datetime.datetime.now().weekday()
