def  Rug(n):
    global row
    row = n 
    rows= []

    for i in range(row):
        rows.append([])
        for j in range(row):
            rows[i].append(0)
  
    if n % 2 == 1 :
        for i in range(row):
            for j in range(row):
                if(abs(i - (row // 2)) > abs(j - (row // 2))):
                    rows[i][j] = abs(i - (row // 2)) 
                else:
                    rows[i][j] = abs(j - (row // 2)) 
    return rows

def show(rows):
        for i in range(row):
            for j in range(row):
                print(rows[i][j] , end = "  ")
            print("")

n = int(input("? :"))
if n % 2 == 1 :
    show(Rug(n))
else :
    print("\n your number should be odd")