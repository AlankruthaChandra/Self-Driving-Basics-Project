import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if self.h == 1:
            return self.g
        else:
            return ((self.g[0][0] * self.g[1][1]) - (self.g[0][1] * self.g[1][0]))
        

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        
        t = 0
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    t += self.g[i][j]
        return t
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 1:
            return (1/self.g)
            
        else:
            det = ((self.g[0][0] * self.g[1][1]) - (self.g[0][1] * self.g[1][0]))
            if det !=0:
                #inv = trace(self.g)*identity(2) - self.g
                inv = zeroes(self.h, self.w)
                d = self.g[1][1] * (1/det)
                b = -self.g[0][1]* (1/det)
                c = -self.g[1][0]* (1/det)
                a = self.g[0][0]* (1/det)
               
                inv = [[d, b], [c,a]]

                return Matrix(inv)
                
            else: 
               print("Inverse not possible")
        

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        res = zeroes(self.w, self.h)
        for i in range(len(self.g)): 
            for j in range(len(self.g[0])):
                res[j][i] = self.g[i][j]
        return res
        
        

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        sum_2 = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                sum_2[i][j] = self.g[i][j] + other[i][j]
        return sum_2
        #

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        neg = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                neg[i][j] = -self.g[i][j]
        return neg
                           
        #

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        sub_2 = zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                sub_2[i][j] = self.g[i][j] - other[i][j]
        return sub_2
        #

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #print (other) 
        S = zeroes(self.h, other.w)
        
        if self.w == other.h:
            
       
            for i in range(self.h):
   
                for j in range(other.w):
       
                    for k in range(other.h):
                        S[i][j] += self.g[i][k] * other[k][j]
                           
        return S
        #

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
        
            print (self.h, self.g)
            print (other)
            mat = identity(self.h)
            print (other)
            res = zeroes(mat.h, mat.w)
            for i in range(mat.h):
                for j in range(mat.w):
                    res[i][j] = other * mat[i][j]
            print (res)       
            return res
            