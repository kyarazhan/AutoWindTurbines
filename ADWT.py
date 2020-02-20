import os
import sys
import math

class powersite():
    global row
    global g
    global x0
    global y0
    global xc
    global yc
    global getangle
    print('开始输入风电场及风机基本参数\n\n参数之间请以空格键隔开！\n')
    print('第一项：请输入起始XY坐标')
    while True:
        try:
            x0,y0 = map(int, input("X坐标为8位数，Y坐标为7位数:\n").split())
            if x0 == 0 or y0 == 0:
                print('输入有误！请重新输入！')
                continue
            elif 8 != len(str(x0)) or 7 != len(str(y0)):
                print('输入有误！请重新输入！')
                continue
            break

        except ValueError:
            print('输入有误！请重新输入')

    print('第二项：开始输入排布行、列数')
    while True:
        try:
            row, g = map(int,input("请分别输入行数、列数:\n").split())
            if row <1 or g < 1:
                print('输入有误！请重新输入！')
                continue
            elif row >101 or g > 101:
                print('上限100！请重新输入！')
                continue
            break

        except ValueError:
            print('输入有误！请重新输入')

    print('第三项：请输入叶轮直径、轮毂高度')
    while True:
        try:
            r, h = map(int,input("请输入叶轮直径、轮毂高度:\n").split())
            if r <60 or r > 200:
                print('60<直径<200！请重新输入！')
                continue
            elif h <60 or h > 180:
                print('60<轮毂高度<180！请重新输入！')
                continue
            elif r > 2*h:
                print('叶尖触地！请重新输入！')
                continue
            break
        except ValueError:
            print('输入有误！请重新输入')

    print('第四项：请输入前后、左右间距（叶轮直径）倍数')
    while True:
        try:
            left, right = map(int,input("请分别输入前后、左右间距倍数:\n").split())
            if left <5 or left > 20:
                print('5<前后间距<20！请重新输入！')
                continue
            elif right <3 or right > 10:
                print('3<左右<10！请重新输入！')
                continue
            break

        except ValueError:
            print('输入有误！请重新输入')

    xc = int(right*r)
    yc = int(left*r)
"""    
    print("第五项：请输入主风向")
    while True:
        getangle = input("请输入正整数：")
        if getangle.isdigit():
            break
        else:
            print("继续输入")

def get_angle():
    while True:
        try:
            if getangle >

"""
def jiusan():
    nu = 0


    for i in range(row):
        for j in  range(g):
            t = nu+1
            nu += 1
            result = 'T{} {} {}\t'.format(int(t),int(x0+i*xc),int(y0+j*yc))

            #print("外部打印%s"%result)

            with open('result.txt','a') as file_handle:
                file_handle.write(result)
                file_handle.write('\n')

print("输出结果在目录下result.txt文件")

if __name__ =='__main__':
    powersite()
    jiusan()
