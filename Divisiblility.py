# seeing if number are divisible by each other
fir_num = int(input("Enter the first number"))
sec_num = int(input("Enter the second number"))

if fir_num%sec_num==0:
    print(str(fir_num)+"is divisible by"+str(sec_num))
else:
    print(fir_num,"is not divisible by", sec_num)