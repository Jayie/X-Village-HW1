import random

from copy import deepcopy


class Matrix:
    matrix = [[]]
    row = 0
    col = 0
    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.row = nrows
        self.col = ncols
        self.matrix = [[0]* self.col for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                self.matrix[i][j] = random.randrange(0,10)

    def add(self, m):
        """return a new Matrix object after summation"""
        a = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                a.matrix[i][j] = self.matrix[i][j] + m.matrix[i][j]
        return a
        
    def __add__(self, m): return self.add(m)

    def sub(self, m):
        """return a new Matrix object after substraction"""
        a = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                a.matrix[i][j] = self.matrix[i][j] - m.matrix[i][j]
        
        return a
        

    def __sub__(self, m): return self.sub(m)

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        a=[[0]* self.col for i in range(m.col)]
        a = Matrix(self.row, m.col)
        for i in range(self.row):
            for j in range(self.col):
                a.matrix[i][j] = 0
                for k in range(m.col):
                    a.matrix[i][j] += self.matrix[i][k] * m.matrix[k][j]
        return a

    def __mul__(self, m): return self.mul(m)

    def transpose(self):
        """return a new Matrix object after transpose"""
        a = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                a.matrix[i][j] = self.matrix[j][i]
        return a
    
    def display(self):
        """Display the content in the matrix"""
        for i in self.matrix:
            for j in i: print(j, end = '\t')
            print()

    def __str__(self):
        self.display()
        return ""

def input_num(question, b = 0):
    while True:
        try:
            a = input(question)
            a = int(a)
            if a > 0:
                if b == 0: return a
                if a == b: return a
        except:
            pass
        print("invalid input")

def main():
    #input A
    arow = input_num("Enter A matrix's rows: ")
    acol = input_num("Enter A matrix's cols: ")
    print("Matrix A(%d, %d):" % (arow, acol))
    a = Matrix(arow, acol)
    a.display()

    #input B
    brow = input_num("Enter B matrix's rows: ", arow)
    bcol = input_num("Enter B matrix's cols: ", acol)
    print("Matrix B(%d, %d):" % (arow, acol))
    b = Matrix(brow, bcol)
    b.display()

    #A + B
    print("========= A + B =========")
    print(a+b)

    #A - B
    print("========= A - B =========")
    print(a-b)

    #A * B
    print("========= A * B =========")
    print(a*b)

    #trans(A*B)
    print("========= the transpose of A*B =========")
    print((a*b).transpose())

if __name__ == '__main__':
    main()