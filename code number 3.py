import datetime
now = datetime.datetime.now()
age = float(input('What is your age? '))
year_born =  int(now.year - age)
print ("Awesome! you were born in ", year_born)
