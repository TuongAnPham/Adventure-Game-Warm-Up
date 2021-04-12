from adventurelib import *

print("Hello. In this game, you will try to find the right key from other people to enter room x, you can enter 'help' in order to see what input you can use. Have fun!")

@when("enter hallway", context='library')
def phallway():
  set_context('hallway')
  print("You enter the hallway.")

@when("where am i", context='hallway')
def ask1():
  print("Hallway with person 1.")

@when("enter library", context='hallway')
def plibrary():
  set_context('library')
  print("You enter the library.")

@when("where am i", context='library')
def ask2():
  print("Library with person 2.")

@when("ask person one", context='hallway')
def person1():
  print("I'm a rabit.")

@when("ask person one", context='library')
def notperson1():
  print("Person 1 is not here.")

@when("ask person two", context='library')
def person2():
  print("I'm a penguin.")

@when("ask person two", context='hallway')
def notperson2():
  print("Person 2 is not here.")

@when("take key", context='hallway')
def nokey():
  set_context('wrongkey')
  print("You took the key from person 1.")

@when("enter x", context='wrongkey')
def fail():
  set_context('hallway')
  print("You can't enter room X.")

@when("take key", context='library')
def key():
  set_context('rightkey')
  print("You took the key from person 2.")

@when("enter x", context='rightkey')
def win():
    set_context('room X')
    print("You enter room X")

@when("look around", context='room X')
def look():
    print("On the table, there is a red book, a green book, and a white book. Open one of them, if you make the right choice, you'll win.")

wrongthing = [
  "red book",
  "green book"
]
@when("open THING", context='room X')
def open (thing):
  if thing in wrongthing:
    print("You lose. You'll be back in hallway with person 1.")
    set_context('hallway')
  else:
    print("The white book is the correct answer! Since you take your key from person 2 'penguin,' remember the color of penguin? With that, this is the end of your journey, thanks for playing.")

@when("exit room x", context='room X')
def exit():
    set_context('library')
    print("You exit room X")

set_context('hallway') 

start()

