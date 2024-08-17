
import re
def getname(answer):
  if answer == '': 
    
    print("Sorry, please enter your name!")
  else: 
    a = re.sub(pattern = "[^\w\s]", repl = '', string = answer)
    b = a.split() 
    i = b[-1] 
    
  return i


print("Hey there! My name is Chatbot. What's your name?")

answer = input()  

name = getname(answer) 


print(name, 'I like that! So then where are you from?')
location = input("I'm from...") 
print('So your name is', name, "and you're from" , location + '.', "What kinds of cuisine \n do they have in", location + '?')


food_genre = ['american', 'mexican', 'italian', 'pizza', 'french']

food = input()


if food.lower() in food_genre:
  print("mmmmmm that sounds yummy,", name +',',  "I wonder if we have that in Singapore where I'm from.")

else:
  print("Great choice,", name + ',', "we might have a couple places like that. If you're in the neighborhood, we should grab a bite!") 

print('What things do you do for fun in', location +',', name + '?')
fun = input()

print(fun, "sounds neat,", name + '.', "I like to do Physics and Math problems for \n fun.")

print('') 
print("Well, it was lovely speaking with you,", name+',', "and hearing about some of the great food you have in", location, "like", food+'.', "Can't wait to hear from you soon!")