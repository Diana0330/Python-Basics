'''
Задание 1 Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:
среднюю букву, если число букв в слове нечетное; две средних буквы, если число букв четное.
'''


word = input('Please enter a word:')
length = len(word)
if len(word) % 2  == 0: # четное
  first_middle_letter = (length//2) -1
  second_middle_letter = length//2
  print(word[first_middle_letter] + word[second_middle_letter] )
else:
  second_middle_letter = length//2
  print(word[second_middle_letter])