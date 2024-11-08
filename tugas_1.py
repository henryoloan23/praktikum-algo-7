import math
x = False
n = ""
def tidak_prima(n):
    if n % 2 == 0 and n > 2: 
        
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        print(n, "adalah bukan Prima")
        
    elif n == 1:
        print(n, 'bukan bilangan prima')
    else:
        bil_prima(n)
        
def bil_prima(n):
    print(n, "adalah Prima")
    
while (not x):
    print("Gunakan 0 untuk stop")
    n = int(input("masukan angka: "))
    if n == 0:
        x = True
    else:
        tidak_prima(n)