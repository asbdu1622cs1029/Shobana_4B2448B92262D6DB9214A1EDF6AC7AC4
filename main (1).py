def isleapyear(year):
   if(year %4==0and year%100!=0)or year% 400==0:
     return True 
year=int(input("Enter a year:"))

if isleapyear(year):
  print('{}is leap year.'.format (year))
else:
  print('{}is not a leap year.'.format (year))