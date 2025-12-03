#!/usr/bin/env python3
# coding=utf-8

import os
import time


# ============ 测试执行周期钩子 ============

def before_all(context):
    """
    在所有测试开始之前执行一次
    """
    print("=== 开始执行所有测试 ===")
    root = os.getcwd()
    context.project_root = root

    mock_root = os.path.join(root, "mock")
    os.makedirs(mock_root, exist_ok=True)

    context.network_file = os.path.join(mock_root, "network_status.txt")
    context.user_passwd_file = os.path.join(mock_root, "user_passwd.json")


def after_all(context):
    """
    在所有测试结束后执行一次
    """
    print("=== 所有测试执行完毕 ===")


# ============ Feature 级别钩子 ============

def before_feature(context, feature):
    """
    在每个 feature 文件执行前执行
    """
    print(f"开始执行 feature: {feature.name}")
    if "api" in feature.tags:
        context.client = None


def after_feature(context, feature):
    """
    在每个 feature 文件执行后执行
    """
    print(f"feature 执行完成: {feature.name}")
    if hasattr(context, 'client'):
        context.client.close()


# ============ Scenario 级别钩子 ============

def before_scenario(context, scenario):
    """
    在每个 scenario 执行前执行
    """
    print(f"开始 scenario: {scenario.name}")
    context.scenario_data = {}

    # 根据标签执行不同操作
    if 'browser' in scenario.tags:
        print("browser in tags")


def after_scenario(context, scenario):
    """
    在每个 scenario 执行后执行
    """
    print(f"scenario 完成: {scenario.name}")

    # 记录测试结果
    if scenario.status == 'failed':
        print(f"{scenario.name}: failed")


# ============ Step 级别钩子 ============

def before_step(context, step):
    """
    在每个 step 执行前执行
    """
    print(f"执行步骤: {step.name}")
    context.step_start_time = time.time()


def after_step(context, step):
    """
    在每个 step 执行后执行
    """
    duration = time.time() - context.step_start_time
    print(f"步骤完成，耗时: {duration:.2f}秒")

    # 处理失败步骤
    if step.status == 'failed':
        print(f"{step.name} failed")


# ============ Tag 特定的钩子 ============

def before_tag(context, tag):
    """
    在带有特定标签的 scenario 执行前执行
    """
    if tag == 'requires_db':
        print("tag requires_db before")
    elif tag == 'slow':
        context.timeout = 30  # 设置更长的超时时间


def after_tag(context, tag):
    """
    在带有特定标签的 scenario 执行后执行
    """
    if tag == 'requires_db':
        print("tag requires_db after")
