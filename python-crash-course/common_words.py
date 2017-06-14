"""Program to count common words in text files with encoding utf-8"""
def count_words(text, word):
  return text.lower().count(word)

try:
  with open('london_by_poore.txt', encoding="utf8") as file_object:
    text = file_object.read()
    the_count = count_words(text, 'the')
    print("Count of the use of the word 'the': " + str(the_count))
except FileNotFoundError:
  print("The file was not found.")
