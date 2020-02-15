
class XYZ():
    print('请输入起始XY坐标，X坐标为8位数，Y坐标为7位数:')
    global x0
    global y0

    while True:
        #x0, y0 = input("请输入两个数：\n").split()
        x0 = input("请输入X坐标：\n")
        try:
            if x0 == 0 :
                print("坐标不能全为 〇 ，请重新输入！")
                continue
            elif 8 != len(str(x0)):
                print("X坐标为8位数，请重新输入！")
                continue
            elif False == x0.isdigit() :
                print("输入有误！")
                continue
        except ValueError:
            print("输入有误！")
            continue
        y0 = input("请输入Y坐标：\n")
        try:
            if y0 == 0:
                print("坐标不能全为 〇 ，请重新输入！")
                continue
            elif 7 != len(str(y0)):
                print("Y坐标为7位数，请重新输入！")
                continue
            elif False == y0.isdigit():
                print("输入有误！")
                continue
        except ValueError:
            print("输入有误！")
            continue
        break

if __name__ == '__main__':
    XYZ()
