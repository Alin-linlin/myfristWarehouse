# 测试可调用方法__call__()


class SalaryAccount:
    """工资计算类"""

    def __call__(self, salary):
        print("计算工资")
        yearSalary = salary * 12
        daySalay = salary // 22.5            # 国家规定的每个月平均工作天数
        hourSalary = salary // 8

        return dict(yearSalary=yearSalary, monthSalary=salary, daySalay=daySalay, hourSalary=hourSalary)


s = SalaryAccount()
print(s(4500))