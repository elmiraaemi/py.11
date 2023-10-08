class Fraction:
    
    def __init__(self, r , i):
        self.r = r
        self.i = i

    
    def sum(self, other) : 
        result_r = self.r + other.r
        result_i = self.i + other.i
        x = Fraction(result_r, result_i)
        return x
    
    def sub(self, other):
        result_r = self.r - other.r
        result_i = self.i - other.i
        x = Fraction(result_r, result_i)
        return x
    
    def mul(self,other) :
        r1 = self.r * other.r
        i1 = self.i * other.r
        i2 = self.r * other.i
        r2 = self.i * other.i
        result_r = r1 - r2
        result_i = i1 + i2

        x = Fraction(result_r, result_i)
        return x

    def show(self):
        print(self.r,'+', self.i, 'i')

a = Fraction(7,3)
a.show()

b = Fraction(2,1)
b.show()

sum = a.sum(b)
sum.show()

sub = a.sub(b)
sub.show()

mul = a.mul(b)
mul.show()
