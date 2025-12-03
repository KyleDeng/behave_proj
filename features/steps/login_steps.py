import os
import json
from behave import given, when, then


@given("登录系统初始化")
def init_login_system(context):
    user_passwd_file = context.user_passwd_file
    if not os.path.exists(user_passwd_file):
        with open(user_passwd_file, 'w') as f:
            f.write("{}")
    pass


@when("用户密码初始化 {username} {passwd}")
def init_username_passwd(context, username, passwd):
    user_passwd_file = context.user_passwd_file
    with open(user_passwd_file, 'r') as f:
        login_data = json.load(f)
    login_data[username] = passwd

    json_str = json.dumps(login_data, indent=4, ensure_ascii=False)
    with open(user_passwd_file, 'w') as f:
        f.write(json_str)
    pass


@then("登录系统初始化 {status} {username} {passwd}")
def assert_login_system(context, status, username, passwd):
    user_passwd_file = context.user_passwd_file
    try:
        with open(user_passwd_file, 'r') as f:
            login_data = json.load(f)
        assert login_data[username] == passwd
    except Exception as e:
        print(f"Exception: {str(e)}")
        assert False


@given("读取所有用户密码")
def read_all_user_passwd(context):
    user_passwd_file = context.user_passwd_file
    with open(user_passwd_file, 'r') as f:
        login_data = json.load(f)
    context.login_data = login_data
    pass


@when("获取用户密码 {username}")
def get_passwd_by_username(context, username):
    if not context.login_data:
        context.current_passwd = ""
    else:
        context.current_passwd = context.login_data.get(username, "")
    pass


@then("比对用户密码 {passwd} {success}")
def assert_passwd(context, passwd, success):
    if success == "成功":
        assert context.current_passwd == passwd
    else:
        assert context.current_passwd != passwd


@then("用户不存在")
def assert_username_notfound(context):
    assert context.current_passwd == ""
