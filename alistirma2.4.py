#fibonacci fonksiyonu
def fib(N):
    if N==1:
        return 1
    elif N==2:
        return 1
    else:
        return fib(N-1) + fib(N-2)
    
#ilk 30 fibonacci sayısını ekrana yazdırmak için
for i in range(1,31):
    print(fib(i),end=" ")
