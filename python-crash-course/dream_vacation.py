poll_results = []
poll_active = True

print('Enter "quit" to exit the program.')

while poll_active:
  place = input('If you could visit one place int he world, where would you go? ')
  if place == 'quit':
    poll_active = False
  else:
    poll_results.append(place)

print('\nPoll results: ')
for place in poll_results:
  print('Somebody wants to visit ' + place.title() + '.')
