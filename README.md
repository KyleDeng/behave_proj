# behave_proj

behave学习笔记

官方文档：https://behave.readthedocs.io/en/latest/

Zread文档: https://zread.ai/behave/behave

---

## 安装

```shell
pip install behave
```

## 概述

### 3个概念

1. `feature`文件：使用`Gherkin`语言编写，通过自然语言描述测试行为

2. `step`定义：使用`python`语言，实现自然语言的描述内容

3. `behave`工具：用于启动整个测试框架、执行用例、生成报告

### 目录结构

```
project_root/
├── features/
│   ├── example.feature          # 测试步骤
│   ├── example2.feature
│   ├── steps/
│   │   └── example_steps.py     # 步骤实现
│   └── environment.py           # 钩子和配置（可选）
├── behave.ini                   # 配置文件
└── requirements.txt             # 依赖项
```

**example.feature**

```gherkin
Feature: 展示behave

    Scenario: 第一个测试
        Given 我们已经安装 behave
        When 我们实现了 5 测试
        Then behave 将为我们测试它们！
```

**example_steps.py**

```gherkin
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
```


### 启动框架

使用命令：

`behave`：运行全部测试用例

`behave features/example.feature features/example2.feature`：指定用例执行

`behave --tags @smoke`：执行带有`smoke`标签的用例

日志：

```log
USING RUNNER: behave.runner:Runner
Feature: 展示behave # features/example.feature:1

  Scenario: 第一个测试         # features/example.feature:3
    Given 我们已经安装 behave   # features/steps/example_steps.py:4 0.000s
    When 我们实现了 5 测试       # features/steps/example_steps.py:9 0.000s
    Then behave 将为我们测试它们！ # features/steps/example_steps.py:16 0.000s

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipp	ed
Took 0min 0.000s
```

## 常用装饰

|装饰器|用途|示例用法|
|---|--|----|
|@given|设置/前提步骤|@given('我已登录')|
|@when|操作/事件步骤|@when('我点击提交')|
|@then|结果/验证步骤|@then('我看到成功消息')|
|@step|通用步骤类型|@step('我执行一个操作')|


## Gherkin语法

### 常用关键字

|Keyword|Purpose|Example|
|-------|-------|-------|
|Feature|描述被测试的高级功能|Feature: 用户管理|
|Scenario|表示特定的测试用例或行为|Scenario: 使用有效数据注册用户|
|Background|定义在每个场景之前运行的步骤|Background: 用户已登录|
|Given|设置初始上下文或前置条件|Given 我有一个包含商品的购物车|
|When|描述被测试的操作或事件|When 我进行结账|
|Then|陈述预期结果|Then 我应该看到订单确认|
|And|用于重复上一个关键字|And 我应该收到电子邮件确认|
|But|用于替代条件或预期|But 我不应该被重复收费|

### 其他关键字

`Background`

用于定义同一 Feature 下所有 Scenario（场景）的公共前置条件，避免重复编写相同的 Given 步骤

`Rule`

用于将一个大 Feature 拆分为多个独立的业务规则，每个 Rule 下可以包含自己的 Scenario/Scenario Outline，让用例结构更清晰

`Examples` 和 `Scenario Outline`

Scenario Outline（场景大纲）中使用 Examples，提供多组测试数据，实现 “一次编写场景，多次执行不同数据” 的参数化测试


