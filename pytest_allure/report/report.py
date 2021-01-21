# -*- coding: utf-8 -*-

# @Author: DarkLi
# @Time  : 2020/8/15
# @Desc  : Test Report

import os
import json
import time
import datetime
from collections import Counter


def generate_test_report(report_path, allure_result_path):
    """
    
    :param report_path: 
    :param allure_result_path:
    :return:
    """
    # report_path 目录是否存在，不存在则创建
    mkdir_lambda = lambda x: os.makedirs(x) if not os.path.exists(x) else True
    mkdir_lambda(report_path)

    run_time_list = []
    run_status_list = []
    # 从 allure result json 文件获取测试用例执行结果状态
    for file_name in os.listdir(allure_result_path):
        if ".json" not in file_name:
            continue
        file_path = os.path.join(allure_result_path, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            result = json.load(f)

        if "container" in file_name:
            run_time_list.append(result["start"])
            run_time_list.append(result["stop"])
        else:
            run_status_list.append(result["status"])

        # 此处删除 allure report 下 Test body 中的 log 节点日志，如自定义日志未正常显示，请确认是否是因此处影响
        if result.get("attachments", None):
            attachments = result["attachments"]
            for attachment in attachments:
                if attachment["name"] == "log":
                    attachments.remove(attachment)
                    break
            with open(file_path, "w") as f:
                json.dump(result, f)

    # 计算开始时间、结束时间、用例执行时长
    start_time = min(run_time_list) / 1000
    end_time = max(run_time_list) / 1000
    use_time = end_time - start_time
    test_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
    test_end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
    test_use_time = str(datetime.timedelta(seconds=use_time))

    # 统计测试结果
    test_ret = Counter(run_status_list)
    # test_total = int(len(run_status_list)) - int(test_ret.get("skipped"), 0)
    test_total = int(len(run_status_list))
    test_result = {
        "test_start_time": test_start_time,
        "test_end_time": test_end_time,
        "test_use_time": test_use_time,
        "total": test_total,
        "passed": int(test_ret.get("passed", 0)),
        "failed": int(test_ret.get("failed", 0)),
        "skipped": int(test_ret.get("skipped", 0)),
        "broken": int(test_ret.get("broken", 0)),
        "unknown": int(test_ret.get("unknown", 0))
    }

    if test_result["passed"] == 0:
        test_result["passing_rate"] = "0.00%"
    else:
        test_result["passing_rate"] = "{:.2%}".format(
            int(test_ret.get("passed", 0)) / (test_total - int(test_ret.get("skipped", 0))))

    report_json = os.path.join(report_path, "report_json.json")
    with open(report_json, "w+", encoding="utf-8") as fw:
        json.dump(test_result, fw)
