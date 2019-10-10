def success():
    return '0', '成功'


def fail():
    return '1001', '失败'


def name_repetition():
    return '1002', '存在相同名称'


def parameter_wrong():
    return '1003', '参数有误'


def project_not_exist():
    return '1004', '项目不存在'


def project_is_exist():
    return '1005', '项目已存在'


def host_is_exist():
    return '1006', 'host已存在'


def host_not_exist():
    return '1007', 'host不存在'


def group_not_exist():
    return '1008', '分组不存在'


def api_not_exist():
    return '1009', '接口不存在'


def api_is_exist():
    return '1010', '接口已存在'


def history_not_exist():
    return '1011', '请求历史不存在'


def case_not_exist():
    return '1012', '用例不存在'


def task_not_exist():
    return '1013', '任务不存在'


def page_not_int():
    return '1014', 'page and page_size must be integer!'


def mock_error():
    return '1015', '未匹配到mock地址或未开启!'


def parameter_not_null():
    return '1016', '必填参数不能为空!'


def parameter_type_error():
    return '1017', '类型错误!'
