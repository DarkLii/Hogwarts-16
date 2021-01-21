# -*- coding: utf-8 -*-

# @Author: DarkLi
# @Time  : 2020/8/15
# @Desc  : dict 操作


def analyze_data(data, key_path="", key_path_dict={}):
    """
    解析data对象路径并获取对应路径的值
    :param data: 支持的对象：dict、list、tuple
    :return：dict对象，key为路径，value为原对象对应路径的值
    """
    if isinstance(data, dict):
        for key, value in data.items():
            key_path_dict[key_path] = data
            if key_path:
                analyze_data(value, f"{key_path}.{key}")
            else:
                analyze_data(value, f"{key}")
    elif isinstance(data, (list, tuple)):
        key_path_dict[key_path] = data
        for index in range(len(data)):
            if key_path:
                analyze_data(data[index], f"{key_path}.{index}")
            else:
                analyze_data(data[index], f"{index}")
    else:
        # print(f"{key_path}={data}")
        key_path_dict[key_path] = data
    return key_path_dict


def _get_dict_value(obj, key):
    """
    获取对象的值，支持的对象：dict、list、tuple
    :param obj: 对象
    :param key:
        1、obj为dict时，key字典的key
        2、obj为list/tuple时，key为对应的index
    :return:
    """
    if isinstance(obj, (list, tuple)):
        value = obj[int(key)]
        return value

    for k in obj.keys():
        # 如果 key 是数字，则可能是 list 的序列号，将数字处理成 int 类型，才能获取 list 元素
        if isinstance(k, int):
            if key.isdigit():
                key = int(key)
        if key == k:
            value = obj[key]
            return value
        if type(obj[k]) == dict:
            value = _get_dict_value(obj[k], key)
            if value:
                return value


def _get_or_update_dict_value(dict_object, key_list, value=None, is_update=0, is_ignore_real_path=1):
    """
    获取或者更新dict的值
    :param dict_object: 需要获取或更新的dict
    :param key_list: key的路径
    :param is_update: 是否是更新字典的值，is_update=0，获取字典的值，is_update=1，更新字典的值，默认：is_update=0，获取字典的值
    :param value: 需要更新的值,is_update=1时必传
    :param is_ignore_real_path: is_ignore_real_path=0时，如果key不存在，则报错，默认：is_ignore_real_path=1
                                is_ignore_real_path=1时
                                    is_get=0时：当传入的key在dict_object不存在时，新增key
                                    is_get=1时：当传入的key在dict_object不存在时，返回None

    :return:
        is_get=0时：返回更新后的dict
        is_get=1时：返回对应key_path的值
    """

    if not isinstance(key_list, list):
        key_list = [key_list]

    if not is_update:
        # 如果key_list只有一个，那么获取第一个匹配到的值，深度优先  PS：这里不一定每个场景都适用（广度优先的不不适用），请小心适用此功能
        if len(key_list) == 1:
            value = _get_dict_value(dict_object, key_list[0])
            return value

        # 根据列表获取字典对应深度的值
        for key in key_list:
            # 如果 key 是纯数字，则当成 list 的序列号，将数字处理成 int 类型，才能获取 list 元素
            if key.isdigit():
                key = int(key)
            if is_ignore_real_path:  # 判断key是否在dict_object中（不在的话不会报错）
                if isinstance(dict_object, dict):
                    value = dict_object.get(key, None)
                    if value == None:
                        break
                else:  # 获取list或tuple的值
                    value = dict_object[key]
            else:
                value = dict_object[key]
            # 继续递归，直到查找到最后一个key
            key_list.pop(0)
            if key_list:
                value = _get_or_update_dict_value(value, key_list)
            return value
    else:
        # 根据列表获取字典对应深度的值
        for key in key_list:
            # 如果 key 是纯数字，则当成 list 的序列号，将数字处理成 int 类型，才能获取 list 元素
            if key.isdigit():
                key = int(key)
            if is_ignore_real_path:
                # 如果更新字典时，key不在原始字典中，那么就新增key
                if isinstance(dict_object, dict):
                    if not dict_object.__contains__(key):
                        index = 1 if len(key_list) > 1 else -1
                        if key_list[index].isdigit():
                            dict_object[key] = []
                        else:
                            dict_object[key] = {}

                # 如果给出的index不在原始字典的路径中，那么新增index
                if isinstance(dict_object, list):
                    max_len = len(dict_object)
                    if (not max_len or key >= max_len):
                        pop_key = key_list.pop(0)
                        if key_list:
                            key = key_list[0]
                        else:
                            key = pop_key
                        if pop_key.isdigit():
                            new_dict = {}
                            new_dict[key] = []
                            if key_list:
                                dict_object.append(new_dict)
                            else:
                                dict_object.append(value)
                            val = new_dict
                            _get_or_update_dict_value(val, key_list, value, is_update=1)
                        continue

            val = dict_object[key]
            # 继续递归，
            if key_list:
                key_list.pop(0)

            if key_list:
                _get_or_update_dict_value(val, key_list, value, is_update=1)
            else:
                dict_object[key] = value
            return dict_object


def update_dict(dict_object, key_values=None, is_ignore_real_path=1):
    """
    更新dict中某个key的值
    :param dict_object: dict类型的数据
    :param key_values: dict类型参数,key为待更新的key路径(路径参照Python取对象属性的方式)，value为待更新的值
    :param is_ignore_real_path: is_ignore_real_path=0时，如果key不存在，则报错，默认：is_ignore_real_path=1
                                is_ignore_real_path=1时，当传入的key在dict_object不存在时，新增key
    eg：dict_object = {
                        "a": 0,
                        "b": {"c": 1},
                        "d": [{"e": 2}]
                    }
    需要更新dict_object的key_values
    key_values =  {
                    "a": 1,
                    "b.c": 2,
                    "d.0.e": 3,
                    "d.1.f": 4,  # 列表内新增dict元素
                    "g.h": 5,  # 新增key
                    "i.0.j": 6,  # 新增key
                    "i.1.k.0": 7  # 列表内新增单个元素
                }
    更新后dict_object为:
    dict_object = {
                    "a": 1,
                    "b": {"c": 2},
                    "d": [{"e": 3}, {"f": 4}],
                    "g": {"h": 5},
                    "i": [{"j": 6}, {"k": [7]}]
                }
    """

    if key_values:
        # 修改指定路径下的value
        for key, value in key_values.items():
            key_list = key.split('.')
            dict_object = _get_or_update_dict_value(dict_object, key_list, value, is_update=1,
                                                    is_ignore_real_path=is_ignore_real_path)

    return dict_object


def get_dict_value(dict_object, key_path_list, is_ignore_real_path=0, is_depth_first_search=0):
    """
    根据key路径获取字典的值
    :param dict_object: dict对象
    :param key_path_list: 需要查找的key路径列表
    :param is_ignore_real_path: key不存在时是否报错
            is_ignore_real_path=0时，key不存在，则报错
            is_ignore_real_path=1时，key不存在，返回 None，默认：is_ignore_real_path=1
    :param is_depth_first_search: 当 is_ignore_real_path=1 时生效，如果key_path只有一层，获取第一个匹配到的值
            is_depth_first_search=0 时，广度优先查找，默认is_deep_search=0
            is_depth_first_search=1 时，深度优先查找
    :return: dict对象，key为路径，val为对应路径的值
        eg：
            dict_object = {
                            "a": 1,
                            "b": {"c": 2},
                            "c": 3,
                            "d": [
                                {"e": 4},
                                {"f": 5}
                            ]
                        }
            key_path_list = [
                                "a",
                                "b",
                                "c",
                                "b.c",
                                "d",
                                "d.0",
                                "d.0.e",
                                "x.0.c"
                            ]
        1、result = get_dict_value(dictionary, key_path_list)   报错：KeyError: 'x.0.c'
        2、result = get_dict_value(dictionary, key_path_list, is_ignore_real_path=1)   # 广度查找优先查找路径短的key
            result = {'a': 1, 'b': {'c': 2}, 'c': 3, 'b.c': 2, 'd': [{'e': 4}, {'f': 5}], 'd.0': {'e': 4}, 'd.0.e': 4, 'x.0.c': None}
        3、result = get_dict_value(dictionary, key_path_list, is_ignore_real_path=1, is_deep_search=1)   # 深度查找（先查找到 b.c）
            result = {'a': 1, 'b': {'c': 2}, 'c': 2, 'b.c': 2, 'd': [{'e': 4}, {'f': 5}], 'd.0': {'e': 4}, 'd.0.e': 4, 'x.0.c': None}

    """
    val = {}
    if not isinstance(key_path_list, list):
        key_path_list = [key_path_list]

    analyze_dict = analyze_data(dict_object)

    # 当为广度优先查找时，构造广度优先查找dict
    if is_ignore_real_path and not is_depth_first_search:
        res_list = sorted(analyze_dict, key=lambda k: len(k.split(".")))
        breadth_search_dict = {}
        for key in res_list:
            breadth_search_dict[key] = analyze_dict[key]

    for key_path in key_path_list:
        if is_ignore_real_path:
            value = analyze_dict.get(key_path, None)
            if is_depth_first_search:  # 深度优先查找
                if len(key_path.split(".")) == 1:
                    for key in analyze_dict.keys():
                        if key_path == key.split(".")[-1]:
                            value = analyze_dict.get(key, None)
                            break

            else:  # 广度优先查找
                if len(key_path.split(".")) == 1:
                    for key in breadth_search_dict.keys():
                        if key_path == key.split(".")[-1]:
                            value = analyze_dict.get(key, None)
                            break
        else:
            value = analyze_dict[key_path]
        val[key_path] = value

    return val


if __name__ == '__main__':
    dictionary = {
        "a": 0,
        "b": {"c": 1},
        "d": [{"e": 2}]
    }

    key_values = {
        "a": 1,
        "b.c": 2,
        "c": 3,
        "d.0.e": 3,
        "d.1.f": 4,
        "g.h": 5,
        "i.0.j": 6,
        "i.1.k.0": 7
    }
    a = update_dict(dictionary, key_values)
    print(a)

    key_path_list = [
        "a",
        "b",
        "c",
        "b.c",
        "d",
        "d.0",
        "d.0.e",
        "x.0.c"
    ]

    ret = get_dict_value(dictionary, key_path_list, is_ignore_real_path=1)
    print(f"Breadth First Search:{ret}")
    ret = get_dict_value(dictionary, key_path_list, is_ignore_real_path=1, is_depth_first_search=1)
    print(f"Depth First Search:{ret}")
