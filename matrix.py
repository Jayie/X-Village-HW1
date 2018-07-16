import random

from copy import deepcopy

class AddException(Exception):
    def __str__(self):
        return "Matrixs' size should be in the same size"

class MultiException(Exception):
    def __str__(self):
        return "A.col and B.row should be the same"

class TransposeException(Exception):
    def __str__(self):
        return "Can't do Transpose"

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
        try:
            """return a new Matrix object after summation"""
            #check if the two matrices have the same size
            if (self.row != m.row) or (self.col != m.col):
                raise AddException()
            
            #do addition
            a = Matrix(self.row, self.col)
            for i in range(self.row):
                for j in range(self.col):
                    a.matrix[i][j] = self.matrix[i][j] + m.matrix[i][j]
            return a
        except AddException as e:
            print(e)
            return Matrix(0,0)
        
    def __add__(self, m): return self.add(m)

    def sub(self, m):
        try:
            """return a new Matrix object after substraction"""
            #check if the two matrices have the same size
            if (self.row != m.row) or (self.col != m.col):
                raise AddException()

            #do substraction
            a = Matrix(self.row, self.col)
            for i in range(self.row):
                for j in range(self.col):
                    a.matrix[i][j] = self.matrix[i][j] - m.matrix[i][j]
            
            return a
        except AddException as e:
            print(e)
            return Matrix(0,0)

    def __sub__(self, m): return self.sub(m)

    def mul(self, m):
        try:
            """return a new Matrix object after multiplication"""
            #check if a.col = b.row
            if self.col != m.row:
                raise MultiException()

            #do multiplication
            a = Matrix(self.row, m.col)
            for i in range(self.row):
                for j in range(m.col):
                    a.matrix[i][j] = 0
                    for k in range(self.col):
                        a.matrix[i][j] += self.matrix[i][k] * m.matrix[k][j]
            return a
        except MultiException as e:
            print(e)
            return Matrix(0,0)

    def __mul__(self, m): return self.mul(m)

    def transpose(self):
        try:
            """return a new Matrix object after transpose"""
            a = Matrix(self.col, self.row)
            if a.col == 0: raise TransposeException()
            for i in range(self.col):
                for j in range(self.row):
                    a.matrix[i][j] = self.matrix[j][i]
            return a
        except TransposeException as e:
            print(e)
            return Matrix(0,0)
    
    def display(self):
        """Display the content in the matrix"""
        for i in self.matrix:
            for j in i: print(j, end = '\t')
            print()

    def __str__(self):
        self.display()
        return ""

def input_num(question):
    while True:
        try:
            a = input(question)
            return int(a)
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
    brow = input_num("Enter B matrix's rows: ")
    bcol = input_num("Enter B matrix's cols: ")
    print("Matrix B(%d, %d):" % (brow, bcol))
    b = Matrix(brow, bcol)
    b.display()

    #A + B
    print("========= A + B =========")
    c = a + b
    print(c)

    #A - B
    print("========= A - B =========")
    c = a - b
    print(c)

    #A * B
    print("========= A * B =========")
    c = a * b
    print(c)

    #trans(A*B)
    print("========= the transpose of A*B =========")
    c = c.transpose()
    print(c)

if __name__ == '__main__':
    main()