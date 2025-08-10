
print("enter year")
n = int(input())
if(n%4==0) or(n%100==0 and n%400==0):
	print("leap year")
else:
	print("not leap year")
