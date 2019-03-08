#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/7 18:03
# @author: Paulson●Wier
# @file: 001_two_sum.py
# @desc:

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，
并返回他们的数组下标

给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

class Solution:
    def twoSum(self,nums,target):
        num={}
        for index,value in enumerate(nums):
            if target - value in num:
                return [num[target-value],index]
            else:
                num[value] = index
        # return []

s =Solution()

print(s.twoSum([3,3,4,4,5],9))


class Solution1():

    def twoSum(self,nums,target):
        i=0
        while i < len(nums):
            if i == len(nums)-1:
                return 'No solution here'
            r = target-nums[i]
            num_follow = nums[i+1:]
            if r in num_follow:
                return [i,num_follow.index(r)+i+1]
            i+=1

s1 = Solution1()
print(s1.twoSum([3,3,4,4,5],9))


