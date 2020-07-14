#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/7/14 6:56 下午
# @Author : vant.ling@klook.com
# @File : sum.py
# @desc: 求两数之和
# 给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的两个整数，并返回他们的数组下标
import random

def Sum(nums, target):
    hashmap = {}
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in hashmap:
            return [hashmap[another_num], index]
        hashmap[num] = index
    return None

if __name__ == '__main__':
    print(Sum([1,2,3,4,5],6))