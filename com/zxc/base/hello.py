#!/usr/bin/env python3     
# -*- coding: utf-8 -*-  
# create by zhuxc@joyowo.com
# 2017/8/21

# s1 = 72
# s2 = 85
# r = (s2 - s1) / s1 * 100
# # print('%.1f' % r + "%")
#
# # 数字前补0，补30个
# s = "%030d" % 11
# # print(len(s))
#
# l = list(range(4))
# # for x in range(5):
#     # print(x)
#     # l[x] = x
# # print(l)
# l[0] = 9
# # print(l)
# # print("===============")
#
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2




#
# d = {s: "1"}
# s = 9
# # print(d)
# t1 = (1, 2)
# t11 = (1, 2)
# t2 = (2, 1)
# set1 = set([t1, t11, t2])
# print(set1)
# d = {t1: 1}
# # print(d)

s = b"\xe6\xb3\xa8\xe5\x86\x8c\xe6\x88\x96\xe7\x99\xbb\xe5\xbd\x95".decode("utf-8")
# print(s)


urls = ['aaa{}djfdk'.format(str(i)) for i in range(0, 100, 20)]
for url in urls:
    print(url)