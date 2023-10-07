class Time:
    #properties
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    #methods
    def time_to_second(self):
        result_h = self.hour * 3600
        result_m = self.minute * 60
        result_s = self.second + result_h + result_m
        return result_s
    
    def second_to_time(self):
        if 60 <= self.second <3600 :
            result_m = int( self.second / 60)
            c = result_m * 60
            result_s = self.second - c
            # print(result_m , ":" , result_s)
            x = Time(0, result_m, result_s)
            return x
        elif self.second >= 3600 :
            result_h = int( self.second / 3600)
            e = result_h * 3600
            result_s = self.second - e
            if result_s < 60 :
                # print(result_h , ":" , "00" , ":" , result_s )
                x = Time(result_h, 00, result_s)
                return x
            if result_s > 60 :
                result_m = int( result_s / 60)
                k = result_m * 60
                result_s = result_s - k
                # print(result_h , ":" , result_m , ":" , result_s )
                x = Time(result_h, result_m, result_s)
                return x
        elif self.second < 60 :
            print("Less than a minute")
        x = Time(result_h, result_m, result_s)
        return x
    
    def sum(self, other):
        result_s = self.second + other.second
        if result_s>59 :
            result_s-=60
            result_m = self.minute + other.minute + 1
            if result_m>59 :
                result_m-=60
                result_h = self.hour + other.hour + 1
            else:
                result_h = self.hour + other.hour
        else:
            result_m = self.minute + other.minute
            if result_m>59 :
                result_m-=60
                result_h = self.hour + other.hour + 1
            else:
                result_h = self.hour + other.hour
        x = Time(result_h, result_m, result_s)
        return x
    
    def sub(self, other):
        result_s = self.second - other.second
        if result_s<0 :
            self.minute-=1
            self.second+=60
            result_s = self.second - other.second
            result_m = self.minute - other.minute
            if result_m<0 :
                self.hour-=1
                result_m+=60
                result_m = self.minute - other.minute
                result_h = self.hour - other.hour
            else:
                result_h = self.hour - other.hour
        else:
            result_m = self.minute - other.minute
            if result_m<0 :
                self.hour-=1
                result_m+=60
                result_m = self.minute - other.minute
                result_h = self.hour - other.hour
            else:
                result_h = self.hour - other.hou
        x = Time(result_h, result_m, result_s)
        return x
    
    def show(self):
        print(self.hour, ':', self.minute, ':',self.second)
    
a = Time(7, 45, 8)
a.show()

b = Time(4, 17, 50)
b.show()

c = Time(0, 0, 58741)
c.second_to_time()
c.show()

time_to_second = a.time_to_second()
print(time_to_second)

sum = a.sum(b)
sum.show()

sub = a.sub(b)
sub.show()