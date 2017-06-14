def read_pet_file(filepath):
  try:
    with open(filepath) as file_object:
      print(file_object.read())
  except FileNotFoundError:
    # print("The file, '" + filepath + "', was not found!")
    pass

files = ['cats.txt', 'dogs.txt']
for file in files:
  read_pet_file(file)
