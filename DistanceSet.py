
class distanceset():
    print('间距设置，叶轮直径倍数')
    global front_back
    global left_right
    print('\n请分别输入前后5-20、左右间距2-10，整数即可，以空格键隔开')
    while True:
        try:
            front_back,left_right = map(int,input().split())
            if front_back > 20 or front_back < 5:
                print('输入有误！请重新输入！')
                continue
            elif left_right > 10 or left_right < 2:
                print('输入有误！请重新输入！')
                continue
            break
        except ValueError:
            print('输入有误！请重新输入')

if __name__ == '__main__':
    distanceset()
