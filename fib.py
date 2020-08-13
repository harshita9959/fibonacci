def fib(num):
  a=0
  b=1
  series=0
  for i in range(num):
    print(series,end=" ");
    a=b;
    b=series;
    series=a+b;
    
num=int(input("Enter the number:"))
fib(num)
