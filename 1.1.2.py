n=int(input())
if 1<=n<=9:
	print(n**2)
elif 10<=n<=99:
	result=n**0.5
	print(f"{result:.2f}")
elif 99<=n<=999:
	result=n**(1/3)
	print(f"{result:.2f}")
else:
	print("Invalid")
