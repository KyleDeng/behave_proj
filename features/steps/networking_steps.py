from behave import given, when, then


@given("重置网络状态")
def reset_network(context):
    network_file = context.network_file
    with open(network_file, 'w') as f:
        f.write("")
    pass


@given("网络状态 {status}")
def set_network_status(context, status):
    network_flag = "2"  # 阻塞
    if "通顺" == status:
        network_flag = "0"
    elif "延时" == status:
        network_flag = "1"

    network_file = context.network_file
    with open(network_file, 'w') as f:
        f.write(network_flag)
    pass


@when("尝试联网")
def try_networking(context):
    network_file = context.network_file
    with open(network_file, 'r') as f:
        network_flag = f.read()
    if "0" == network_flag:
        context.networking_status = True
        context.networking_delay = 0
    elif "1" == network_flag:
        context.networking_status = True
        context.networking_delay = 10
    elif "2" == network_flag:
        context.networking_status = False
        context.networking_delay = 30
    pass


@then("联网状态 {status}")
def assert_networking(context, status):
    print(f"status: {status}")
    if "成功" == status:
        assert context.networking_status is True
    else:
        assert context.networking_status is False
    pass


@then("联网延迟大于 {delay:d}")
def assert_networking_dely(context, delay):
    print(f"delay: {delay}")
    assert context.networking_delay > delay
    pass
