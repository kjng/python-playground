# Program to generate a story using name, verb, and noun inputs in OOP

class StoryGenerator:
  def __init__(self):
    self.welcome()
    self.getName()
    self.getVerb()
    self.getNoun()

  def welcome(self):
    greeting = "***Welcome to your story! I'm Kevin and I'll be guiding you on this wonderful adventure."
    print(greeting)

  def getName(self):
    self.name = input("What's your name? ")
    print('Okay! Hi %s' % self.name)

  def getVerb(self):
    self.verb = input("Input a verb: ")

  def getNoun(self):
    self.noun = input("Give me a noun: ")

  def renderStory(self):
    print("Your story is...")
    print("Once upon a time, %s %s %s!" % (self.name, self.verb, self.noun))
    print("Thanks for playing!")

story = StoryGenerator()
story.renderStory()
