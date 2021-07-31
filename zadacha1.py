print("Today's date?")
date = input()
print("Breakfast calories?")
BC = int(input())
print("Lunch calories?")
LC = int(input())
print("Dinner calories?")
DC = int(input())
print("Snack calories?")
SC = int(input())
sum = BC+LC+DC+SC
print ("Calorie content for " + date + ": " + str(sum))


