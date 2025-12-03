from behave import given, when, then


@given("我们已经安装 behave")
def step_impl(context):
    pass


@when("我们实现了 {number:d} 测试")
def step_impl(context, number):
    assert number >= 0
    context.tests_count = number
    pass


@then("behave 将为我们测试它们！")
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0
