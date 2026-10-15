# 计算斐波那契数列的第n项
def fibonacci(n):
    # 假设n是正整数
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a


# 测试函数
print("斐波那契数列第5项是:", fibonacci(5))  # 预期结果应该是5
print("斐波那契数列第0项是:", fibonacci(0))  # 特殊情况测试
print("斐波那契数列第-3项是:", fibonacci(-3))  # 异常情况测试
