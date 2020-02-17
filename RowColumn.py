
class rowcolumn():
    print('行列数目最小1、最大100')
    global row
    global column
    print('\n请分别输入风机请输入行、列数，整数即可，以空格键隔开')
    while True:
        try:
            row,column = map(int,input().split())
            if row > 100 or row < 0:
                print('输入有误！请重新输入！')
                continue
            elif column > 100 or column < 0:
                print('输入有误！请重新输入！')
                continue
            break
        except ValueError:
            print('输入有误！请重新输入')

if __name__ == '__main__':
    rowcolumn()
