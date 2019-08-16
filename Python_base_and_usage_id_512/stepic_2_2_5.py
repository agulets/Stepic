'''
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.
'''

from datetime import date, timedelta

input_date = input().split()
date = date(int(input_date[0]), int(input_date[1]), int(input_date[2]))
delta = timedelta(days=int(input()))
print((date + delta).strftime("%Y %-m %-d"))
