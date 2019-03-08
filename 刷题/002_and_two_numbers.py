#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/7 20:43
# @author: Paulson●Wier
# @file: 002_and_two_numbers.py
# @desc: 是我太菜了嘛，看不懂这道题
'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self,l1,l2):
        '''
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        '''
        # n is the node of l1
        n = l1
        i = 1
        num_l1 = 0

        # get num of l1
        while n:
            num_l1 = num_l1 + n.val*i
            i = i*10
            n=n.next

        # m is the node if l2
        m=l2
        j=1
        num_l2 = 0
        while m:
            num_l2 = num_l2 + m.val*j
            j = j*10
            m = m.next

        # get the sum of l1,l2
        str_num = str(num_l1+num_l2)

        # reverse str_num
        str_num = str_num[::-1]

        #turn to list output
        list_result =[]
        for s in str_num:
            list_result.append(int(s))
        return list_result

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
s = Solution()
s=s.addTwoNumbers(l1,l2)
print(s)


