import numpy as np


def Carmer():
    n = int(input('columns : ')) # columns
    m = int(input('rows : ')) # rows
    #print(n,m)
    matrixA = [] #[[x], [y], [z]]
    
    for i in range(0,m):
        matrixA.append([])
        for j in range(0,n):
            matrixA[i].append(0)
            matrixA[i][j] = int(input('ตัวเลข [โดย เรียงจากใส่ค่า X1, Xn จนหมด แล้วใส่ค่า Y1, Yn , Z1, Zn ต่อๆไป] : '))
    print (matrixA)
    
    
    ans = [int(x) for x in input('Ans [x, y, .... ]: ').split()]  # x + y = n
    detA = np.linalg.det(matrixA)

  
    


    for i in range(len(matrixA)):
        aCal = matrixA[:] #Clone list
        valueCal = 0
        aCal[i] = ans

        valueCal = (np.linalg.det(aCal)) / detA

        print('                                                ')
        print('Det A : ', detA)
        print('A : ', aCal, ' = ', np.linalg.det(aCal))
        print('Value Ans: ', np.linalg.det(aCal), ' / ', detA, ' = ', valueCal)
        print('                                                ')
        

        
    #print(a)
     
    


Carmer()
