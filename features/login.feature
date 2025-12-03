Feature: 登录测试

    Background: 用户打开登录系统
        Given 登录系统初始化

    Scenario Outline: 密码初始化
        When 用户密码初始化 <username> <passwd>
        Then 登录系统初始化 成功 <username> <passwd>

        Examples:
            | username | passwd |
            | 张三 | 333333 |
            | 李四 | 444444 |
            | 王五 | 555555 |
            | 赵六 | 666666 |

    Rule: 正确使用密码
        Background: 读取用户密码
            Given 读取所有用户密码

        @张三 @密码正确
        Scenario: 张三使用正确密码
            When 获取用户密码 张三
            Then 比对用户密码 333333 成功

        @李四 @密码正确
        Scenario: 李四使用正确密码
            When 获取用户密码 李四
            Then 比对用户密码 444444 成功

        @王五 @密码正确
        Scenario: 王五使用正确密码
            When 获取用户密码 王五
            Then 比对用户密码 555555 成功

        @赵六 @密码正确
        Scenario: 赵六使用正确密码
            When 获取用户密码 赵六
            Then 比对用户密码 666666 成功

    Rule: 正确错误密码
        Background: 读取用户密码
            Given 读取所有用户密码

        @张三 @密码错误
        Scenario: 张三使用错误密码
            When 获取用户密码 张三
            Then 比对用户密码 333331 失败

        @李四 @密码错误
        Scenario: 李四使用错误密码
            When 获取用户密码 李四
            Then 比对用户密码 444441 失败

        @王五 @密码错误
        Scenario: 王五使用错误密码
            When 获取用户密码 王五
            Then 比对用户密码 555551 失败

        @赵六 @密码错误
        Scenario: 赵六使用错误密码
            When 获取用户密码 赵六
            Then 比对用户密码 666661 失败

    Rule: 用户不存在
        Background: 读取用户密码
            Given 读取所有用户密码

        Scenario: 赵甲输入密码
            When 获取用户密码 赵甲
            Then 用户不存在

        Scenario: 钱乙输入密码
            When 获取用户密码 钱乙
            Then 用户不存在
