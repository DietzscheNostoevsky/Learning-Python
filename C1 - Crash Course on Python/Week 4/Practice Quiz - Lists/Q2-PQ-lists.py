#Let's create a function that turns text into pig latin: 
#a simple text transformation that modifies each word 
#moving the first character to the end and appending "ay" to the end. 
#For example, python ends up as ythonpay.

def pig_latin(text):

  phrase = []
  say = ""

  # Separate the text into words
  words = text.split()

  for word in words:

    # Create the pig latin word and add it to the list
    nword = word[1:]+word[0]+'ay'
    phrase.append(nword)

  for ph in phrase : 
    say = say + ph + ' '
    
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"