from datetime import date

'''
print('Enter Date of Completion:')
year = int(input('Year:'))
month = int(input('Month:'))
day = int(input('Day:'))
print()
'''

year = 2018
month = 7
day = 30

print('Morning!')

today = date.today()
future = date(year,month, day)
days_left = (future - today).days

print('You have', days_left, 'days left until end of July.')
print()

#total = int(input('Question in Total:'))
total = 2400

done = int(input('How many questions have you completed so far?'))
left = total-done
print()

print('Question Left:', left)
print('Question To Do Per Day:', int(left/days_left))
print('Percentage Complete:', str(int(done*100/total)) + '%')
