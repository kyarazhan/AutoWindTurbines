
class windturbine():
    print('请输入风机参数')
    global hub
    global dia
    print('\n请分别输入风机桨叶直径及轮毂高度，整数即可，以空格键隔开')
    while True:
        try:
            dia,hub = map(int,input().split())
            if hub > 200 or hub < 0:
                print('输入有误！请重新输入！')
                continue
            elif dia > 200 or dia < 100:
                print('输入有误！请重新输入！')
                continue
            elif dia > 2*hub:
                print('桨叶触地！')
                continue
            break
        except ValueError:
            print('输入有误！请重新输入')

if __name__ == '__main__':
    windturbine()
