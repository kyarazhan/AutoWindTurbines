print("开始风机自动排布计算\n输入参数无特别说明，均以空格隔开\n")
class XYZ():
    print('请输入起始XY坐标')
    global x0
    global y0

    while True:
        try:
            x0, y0 = map(int,input("X坐标为8位数，Y坐标为7位数:\n").split())
            if x0 == 0 or y0 == 0:
                print('输入有误！请重新输入！')
                continue
            elif 8 != len(str(x0)) or 7 != len(str(y0)):
                print('输入有误！请重新输入！')
                continue
            break

        except ValueError:
            print('输入有误！请重新输入')


if __name__ == '__main__':
    XYZ()
