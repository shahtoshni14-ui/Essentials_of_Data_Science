int_list = []

while True:
	print('1. Add')
	print('2. Remove')
	print('3. Display')
	print('4. Quit')

	n = int(input('Enter choice: '))
	if n==1:
		element = (input('Integer: '))
		if element.isdigit():
			S1 = int(element)
			int_list.append(S1)
			print('List after adding:',int_list)
		else:
			print('Invalid input')
	elif n==2:
		if int_list:
			element = input('Integer: ')
			if element.isdigit:
				S2 = int(element)
				if S2 in int_list:
					int_list.remove(S2)
					print("List after removing:", int_list)
				else:
					print('Element not found')
			else:
				print('Invalid input')
		else:
			print('List is empty')
	elif n == 3:
		if int_list:
			print(int_list)
		else:
			print('List is empty')
	elif n == 4:
		break
	else:
		print('Invalid choice')
