n = int(input())
marks = list(map(int, input().split()))
aggregate = sum(marks) / n 
if any(m < 40 for m in marks):
	print('Fail')
else:
	print(f'Aggregate Percentage: {aggregate:.2f}')
	if aggregate > 75:
		print('Grade: Distinction')
	elif aggregate >=60:
		print('Grade: First Division')
	elif aggregate >= 50:
		print('Grade: Second Division')
	elif aggregate >= 40:
		print('Grade: Third Division')
