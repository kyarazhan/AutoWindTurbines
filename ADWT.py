import os
import sys

def powersite():
    global row
    global g
    global x0
    global y0
    global xc
    global yc
    print('开始输入风电场及风机基本参数\n请正常输入！未加入纠错功能！\n\n参数之间请以空格键隔开！\n')

    print('请输入起始XY坐标:')
    x0, y0 = map(int, input().split())

    print('请分别输入行数、列数:')
    row, g = map(int, input().split())

    print('请分别输入叶轮直径、轮毂高度:')
    r, h = map(int, input().split())

    print('请分别输入前后、左右间距倍数:')
    left, right = map(int, input().split())

    xc = left*r
    yc = right*r

def jiusan():
    nu = 0

    for i in range(row):
        for j in  range(g):
            t = nu+1
            nu += 1
            result = 'T{} {} {}\t'.format(t,x0+i*xc,y0+j*yc,)

            print("外部打印%s"%result)

            with open('result.txt','a') as file_handle:
                file_handle.write(result)
                file_handle.write('\n')

if __name__ =='__main__':
    powersite()
    jiusan()
