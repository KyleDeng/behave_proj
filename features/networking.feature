Feature: 设备联网测试
    模拟设备联网状态
    分为网络通顺和网络阻塞场景

    @网络通顺
    Scenario: 正常联网
        Given 重置网络状态
        Given 网络状态 通顺
        When 尝试联网
        Then 联网状态 成功

    @网络阻塞
    Scenario: 联网速度慢
        Given 重置网络状态
        Given 网络状态 延时
        When 尝试联网
        Then 联网状态 成功
        But 联网延迟大于 5

    @网络阻塞
    Scenario: 联网失败
        Given 重置网络状态
        Given 网络状态 阻塞
        When 尝试联网
        Then 联网状态 失败
