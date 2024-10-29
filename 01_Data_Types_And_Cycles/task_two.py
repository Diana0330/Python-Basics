'''
Задание 2 Напишите программу, которая последовательно запрашивает у пользователя числа (по одному за раз) и после первого нуля выводит 
сумму всех ранее введенных чисел.
'''
number = int(input('Please enter a number:'))
sum = 0
while number !=0:
   sum +=number
   number = int(input('Please enter a number:'))
   #if number == 0:
print(f'Sum of all entered numbers:{sum}')
