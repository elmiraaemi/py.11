class Fraction:
    #properties
    def __init__(self, ss , mm):
        self.s = ss
        self.m = mm

    #methods
    def sum(self, other) : 
        result_s = self.s * other.m + self.m * other.s
        result_m = self.m*other.m
        x = Fraction(result_s, result_m)
        return x
    
    def sub(self, other):
        b2=[]
        a2=[]
        for i in range(1 , (self.m * other.m)+1):
            c = self.m * i
            a2.append(c)
        for i in range(1 , (self.m * other.m)+1):
            d = other.m * i
            b2.append(d)
        bmm=list(set(a2).intersection(b2))
        result_m=min(bmm)
        
        nows1 = result_m // self.m
        now_s1 = self.s * nows1
        nows2 = result_m // other.m
        now_s2 = other.s * nows2

        result_s = now_s1 - now_s2

        x = Fraction(result_s, result_m)
        return x
    
    def mul(self,other) :
        result_s = self.s * other.s
        result_m = self.m * other.m
        x = Fraction(result_s, result_m)
        return x
    
    def div(self, other):
        result_s = self.s * other.m
        result_m = self.m * other.s
        x = Fraction(result_s, result_m)
        return x

    def Convert_fractions_to_percentages(self):
        result_s = (self.s * 100) // self.m
        result_m = 100
        x = Fraction(result_s, result_m)
        return x
    
    def Convert_fractions_to_number(self):
        x = self.s / self.m
        return x

    def Simpling_fractions(self):
        b2=[]
        a2=[]
        for i in range(1 , self.s+1):
            if self.s % i == 0:
                c = self.s // i
                a2.append(c)
        for i in range(1 , self.m+1):
            if self.m % i == 0:
                d = self.m // i
                b2.append(d)
        x=list(set(a2).intersection(b2))
        kmm = max(x)

        result_s = self.s // kmm
        result_m = self.m // kmm

        x = Fraction(result_s, result_m)
        return x
    
    def show(self):
        print(self.s,'/',self.m)

a = Fraction(3,6)
a.show()

b = Fraction(7,1)
b.show()

sum = b.sum(a)
sum.show()

sub = b.sub(a)
sub.show()

mul = a.mul(b)
mul.show()

div = a.div(b)
div.show()

percentages = a.Convert_fractions_to_percentages()
percentages.show()

number = a.Convert_fractions_to_number()
print(number)

simple_fractions = a.Simpling_fractions()
simple_fractions.show()