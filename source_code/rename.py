# -*- coding = utf-8 -*-
# @Time : 2021/6/18 15:04
# @Author : Godot
# @File : rename.py
# @Software : PyCharm

import os
import re

con = 'y'       # 判断是否继续标志 初始为y
num = 0

while con == 'y' or con == 'Y':
    # 循环计数，用于处理第一次运行，下方delete未赋值问题
    num = num + 1
    try:
        # 获取指定目录下的 所有子目录和文件名
        path = input('\n输入文件所在路径：')       # path = r'D:\T\01_01_Mathematics\01_微积分\02_强化阶段\04.高等数学（武忠祥）'
        old_names = os.listdir(path)
    except FileNotFoundError as fe:
        print('\n', fe)
    else:
        new_names = []      # 用于 打印新名字

        print('\n该目录下 文件名：')
        for old in old_names:
            print(old)

        if num == 1:
            delete = input('\n请输入 针对该目录下所有文件 对于文件名 要删掉的部分（仅修改文件名）：')
        else:
            y = input('\n(y/n)修改内容是否还为 ' + delete + '：')
            if y != 'y' and y != 'Y':
                delete = input('\n请输入 针对该目录下所有文件 对于文件名 要删掉的部分（仅修改文件名）：')

        for old in old_names:
            new = re.sub(delete, '', old)
            if new != old:
                # 若无需修改，则不动     否则对于所有文件 都用新名字替换旧名字 ， 这样对于某些正在工作修改不了、且实际上无需修改的文件 进行操作会报错
                # 也会加快速度，减少不必要的替换操作
                os.rename(path + os.sep + old, path + os.sep + new)
            new_names.append(new)  # 用于 打印新名字

        print('\n修改前后对比：')
        for old, new in zip(old_names, new_names):
            print(old + '\t' + new)

        con = input('\n是否继续对其它目录修改（y/n）')
else:
    input('\n修改完成 Please Say bye:')
