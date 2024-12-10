#Чтобы мы могли убедиться в том, что вы действительно установили интерпретатор,
# исполните построчно в интерпретаторе Python следующий код:

#fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
#fib(31)

fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
print(fib(31)) #added print() by myself - because I didn't see result after running code