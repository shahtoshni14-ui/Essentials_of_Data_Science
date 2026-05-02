def linear_search(arr, x):
	for i in range(len(arr)):
		if arr[i] == x:
			return i
	return -1

arr = list(map(int, input().split()))
x = int(input())

result = linear_search(arr, x)

if result != -1:
	print(result)
else:
	print('Not found')
