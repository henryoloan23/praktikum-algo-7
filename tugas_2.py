x = False
n = ""

def buat_ordinal(n):

    n = int(n)
    akhiran = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        akhiran = 'th'
    print("",n,'',akhiran,'',"")
while (not x):
    print("Ketik '-1' untuk menghentikan")
    n = int(input("masukan angka: ")) 
    if n == -1:
        x = True
    else:
        buat_ordinal(n)
