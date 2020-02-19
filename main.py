import Coords
import WindTurbine
import RowColumn
import DistanceSet

def calculate():
    nu = 0

    for i in range(RowColumn.row):
        for j in range(RowColumn.column):
            t = nu+1
            nu += 1
            result = 'T{} {} {}\t'.format(t,Coords.x0+i*WindTurbine.hub*DistanceSet.front_back,\
                                          Coords.y0+j*WindTurbine.hub*DistanceSet.left_right)

            print("外部打印%s"%result)

            with open('result.txt','a') as file_handle:
                file_handle.write(result)
                file_handle.write('\n')

if __name__=='__main__':
    calculate()
