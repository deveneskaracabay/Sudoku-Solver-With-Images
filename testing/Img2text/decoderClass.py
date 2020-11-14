
class Sudoku():
    def __init__(self,matrix):
        self.matrix =  matrix
        if self.control() : 
            self.flag = self.solve()
        else:
            self.flag = False

    def control(self):
        for row in self.matrix:
            for i in row:
                if i<0 or i>9:
                    return False

        for row in self.matrix:
            for i in row:
                if i == 0:
                    continue
                if row.count(i) > 1 :
                    return False

        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(self.matrix[j][i])
            for i in temp:
                if i == 0:
                    continue
                if temp.count(i)>1:
                    return False
                
        for x0 in [0,3,6]:
            for y0 in [0,3,6]:

                temp = []
                for x in range(3):
                    for y in range(3):
                        temp.append(self.matrix[x+x0][y+y0])

                for j in temp:
                    if j == 0:
                        continue
                    if temp.count(j)>1:
                        return False

        return True
            

    def possible( self, row, col, num):
        for i in range(9):
            if self.matrix[row][i] == num:
                return False
            
        for i in range(9):
            if self.matrix[i][col] == num:
                return False
            
        row0=(row//3)*3
        col0=(col//3)*3
        for i in range(3):
            for j in range(3):
                if self.matrix[row0+i][col0+j] == num :
                    return False
        return True

    def solve(self, row=0, col=0):
        if (row == 8) and (col == 9):
            return True
        
        if col==9:
            row += 1
            col  = 0
            
        if (self.matrix[row][col] > 0):
            return self.solve(row,col+1)
        
        for num in range(1,10):
            if self.possible(row, col, num):
                self.matrix[row][col] = num
                if self.solve(row, col+1):
                    return True
                self.matrix[row][col] = 0

        return False
