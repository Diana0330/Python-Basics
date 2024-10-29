'''
Задание 3 Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек. Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки! 
Но мы не будем никого знакомить, если кто-то может остаться без пары.
'''

boys = ['Peter', 'Alex', 'John', 'Michael', 'Richard']
girls = ['Kate', 'Liza', 'Jeanna', 'Emma', 'Anna']


if len(boys) ==len(girls):
  sorted_boys = sorted(boys)
  sorted_girls = sorted(girls)
  zipped_list = zip(boys, girls)
  print('Here are our ideal matches:')
  for i in zipped_list:
      print(f'{i[0]} and {i[1]}')
else:
 print('Attention, someone may be left without a partner!')
