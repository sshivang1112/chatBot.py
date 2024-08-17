#Joseph Miller 07/10/2022
import re
def getname(answer):#Start by defining a function
  if answer == '': 
    #If there is nothing entered for a name, you cannot proceed
    print("Sorry, please enter your name!")
  else: #Otherwise we turn the answer into an array and use negative indexing to (hopefully) grab the name. 
#Use the re.sub() method to replace anything thats not a word or whitespace to a blank string
    a = re.sub(pattern = "[^\w\s]", repl = '', string = answer)
    b = a.split() #Splits answer into an array
    i = b[-1] #Negative indexing to grab the name
    
  return i

#Bot introduces itself and prompts the user to state their name
print("Hey there! My name is Chatbot. What's your name?")

answer = input()  #Stores their name in a variable entitled 'name'

name = getname(answer) #Envokes our defined function

#States the user's name and asks where they're from
print(name + ',', 'what a nice name! So then, where are you from?')
location = input("I'm from...") #Stores the variable entitled 'location'

#Bot repeats the users name and where they're from and asks what food they have in the area
print('So your name is', name, "and you're from" , location + '.', "What kinds of cuisine \n do they have in", location + '?')

#Generated a list with some foods I could think of. My bot is from Asia, so they're more likely to have Asian quisene. Hence why something like 'Chinese' isn't included
food_genre = ['american', 'mexican', 'italian', 'pizza', 'french']

food = input()

#If else statement has that if the food input belongs to a string in the list:
if food.lower() in food_genre:
  print("mmmmmm that sounds yummy,", name +',',  "I wonder if we have that in Singapore where I'm from.")
#Otherwise:
else:
  print("Great choice,", name + ',', "we might have a couple places like that. If you're in the neighborhood, we should grab a bite!") #It returns this

print('What things do you do for fun in', location +',', name + '?')
fun = input()

print(fun, "sounds neat,", name + '.', "I like to do Physics and Math problems for \n fun.")

print('') #Spacing between most recent and closing statement

print("Well, it was lovely speaking with you,", name+',', "and hearing about some of the great food you have in", location, "like", food+'.', "Can't wait to hear from you soon!")