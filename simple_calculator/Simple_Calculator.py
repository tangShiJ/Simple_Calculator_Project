# -*- coding: utf-8 -*-
"""
Simple_Calculator inside package simple_calculator
"""
import random


class Calculator(object):

    def __init__(self):
        self.x = None
        self.y = None
        self.operator = {
            'add':'+',
            'subtract':'-',
            'multiply':'*',
            'divide':'/'
        }

    def get_number(self):
        try:
            self.x = int(input('输入第一个数：'))
            self.y = int(input('输入第二个数：'))
        except ValueError as e:
            print('请输入有效数字！')
            raise e

    def custom_operator(self):
        operator = input('运算符选项：1."+"\t2."-"\t3."*"\t4."/"\n请选择运算符：')
        if operator == '1':
            print(self.x + self.y)
            return self.x + self.y
        elif operator == '2':
            print(self.x - self.y)
            return self.x - self.y
        elif operator == '3':
            print(self.x * self.y)
            return self.x * self.y
        elif operator == '4':
            try:
                print(self.x / self.y)
                return self.x / self.y
            except ZeroDivisionError as e:
                print('除数不能为0！')
                raise e
        else:
            print('请输入正确的运算符！')
            return '请输入正确的运算符！'

    def ran_operator(self):
        ope_name = list(self.operator.keys())
        num_ope = random.choice(ope_name)
        ope_value = self.operator[num_ope]
        print(f'运算符为：{ope_value}')
        try:
            result = f"{self.x}{ope_value}{self.y}"
            print(eval(result))
        except ZeroDivisionError as e:
            print('除数不能为0！')

    def select_operator(self):
        while True:
            mode = input('运算模式：1.自定义运算符\t2.随即运算符\t3.退出程序\n请选择运算模式:')
            self.get_number()
            if mode == '1':
                print(f'{"您已选择自行选择运算符":-^10}')
                self.custom_operator()
            elif mode == '2':
                print('您已选择随机运算符运算')
                self.ran_operator()
            elif mode == '3':
                print('退出计算器')
                break
            else:
                print('请输入有效选项！')


if __name__ == '__main__':
    c = Calculator()
    c.select_operator()

