print((lambda n:n not in(0,1)and all(n%i for i in range(2,int(n**.5+1))))(int(input())))
