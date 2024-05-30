
team1 = "Мастера кода"
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
challenge_result = None
tasks_total = 82
time_avg = 350.4

# % usage
print('"В команде %s участников: %s"' % (team1, team1_num))
print('"Итого сегодня в кмандах участников: %s и %s"' % (team1_num, team2_num))

# format() usage
print('"Команда {} решила задач: {}"'.format(team2, score_2))
print('"{} решили задачи за {} c !"'.format(team2, team1_time))

# f-string usage
print(f'"Команды решили {score_1} и {score_2} задач."')
print(f'"Результат битвы: Ничья"' if score_1 == score_2 else f'"Победа команды {team1}!"' if score_1 > score_2 else\
		f'"Победа команды {team2}!"')
print(f'"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"')
