import Coords
import WindTurbine
import RowColumn
import DistanceSet


"""
zz = DistanceSet.front_back + DistanceSet.left_right
hh = DistanceSet.front_back
gg = DistanceSet.left_right
print(str(zz))
print("mian打印X%s"%hh + "  " + "main打印Y%s"%gg)

"""
def calculate2():
    zz = DistanceSet.front_back + DistanceSet.left_right
    hh = DistanceSet.front_back
    gg = DistanceSet.left_right
    print(str(zz))
    print("mian打印X%s" % hh + "  " + "main打印Y%s" % gg)
def calculate():
    nu = 0

    for i in range(RowColumn.row):
        for j in  range(RowColumn.column):
            t = nu+1
            nu += 1
            result = 'T{} {} {}\t'.format(str(t),str(Coords.x0+i*WindTurbine.hub*DistanceSet.front_back),str(Coords.y0+j*WindTurbine.hub*DistanceSet.left_right))

            print("外部打印%s"%result)

            with open('result.txt','a') as file_handle:
                file_handle.write(result)
                file_handle.write('\n')


if __name__=='__main__':
    calculate()






