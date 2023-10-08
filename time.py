import datetime
import pytz

class Time:

    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s
        self.fix()

    
    def time_to_second(self):
        result_h = self.hour * 3600
        result_m = self.minute * 60
        result_s = self.second + result_h + result_m
        x = Time(0, 0, result_s)
        return x
    
    def second_to_time(self):
        if 60 <= self.second <3600 :
            result_m = self.second // 60
            c = result_m * 60
            result_s = self.second - c
            result_h = 0
        elif self.second >= 3600 :
            result_h = self.second // 3600
            e = result_h * 3600
            result_s = self.second - e
            if result_s < 60 :
                result_m =0
            else :
                result_m = result_s // 60
                k = result_m * 60
                result_s = result_s - k
        elif self.second < 60 :
            result_h = 0
            result_m = 0
            result_s = self.second
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

    def GMT_to_tehran_time(self) :
        result_h = self.hour + 3
        result_m = self.minute + 30 
        result_s = self.second 
        x = Time(result_h, result_m, result_s)
        return x
    
    #     gmt = pytz.timezone('GMT')
    #     tehran = pytz.timezone('Asia/Tehran')
    #     gmt_time = datetime.datetime.now(tz=gmt)
    #     tehran_time = gmt_time.astimezone(tehran)
    #     print(tehran_time, ": زمان فعلی تهران ")

    def fix(self):
        if self.second >= 60 :
            self.second -= 60
            self.minute += 1 

        if self.minute >= 60 :       
            self.minute -= 60 
            self.hour += 1

        if self.second < 0 : 
            self.second += 60 
            self.minute -= 1

        if self.minute < 0 :
            self.minute += 60
            self.hour -= 1

    def show(self):
        print(self.hour, ':', self.minute, ':',self.second)
    
a = Time(7, 45, 8)
a.show()

b = Time(4, 17, 50)
b.show()

c = Time(0, 0, 58741)
c.show()

second_to_time = c.second_to_time()
second_to_time.show()


time_to_second = a.time_to_second()
time_to_second.show()

sum = a.sum(b)
sum.show()

sub = a.sub(b)
sub.show()

gmt_to_tehran_tim = a.GMT_to_tehran_time()
gmt_to_tehran_tim.show()

sub.show()
