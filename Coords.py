def XYZ():
    print('请输入起始XY坐标，X坐标为8位数，Y坐标为7位数:')

    while True:
        try:
            x0, y0 = map(int, input().split())
            if x0 == 0 or y0 == 0:
                print("坐标不能全为 〇 ，请重新输入！")
                continue
            elif 8 != len(str(x0)) or 7 != len(str(y0)):
                print("X坐标为8位数，Y坐标为7位数，请重新输入！")
                continue
            else:
                print("初次打印 X%d"%x0 +"  " + "Y%d"%y0)
                return x0,y0
                break
                
        except ValueError:
        
            print('输入有误！请重新输入')
            
            
if __name__=='__main__':
    XYZ()