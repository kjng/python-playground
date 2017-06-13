def display_message():
  print('I am learning about defining functions in Python!')
display_message()

def favorite_book(title):
  print('One of my favorite books is ' + title.title() + '.')
favorite_book('the hobbit')

def make_shirt(size='large', message='I love Python'):
  print('You ordered a t-shirt size of ' + size + ' with a message of ' + message + '!')
make_shirt('small', 'Hello World')
make_shirt(message='Hello World', size='small')
make_shirt()
make_shirt('medium')
make_shirt(message='Hey there')

def city_country(city, country):
  return city.title() + ', ' + country.title()
print(city_country('santiago', 'chile'))
print(city_country('new jersey', 'united states'))
print(city_country('london', 'england'))

def make_album(artist, title, num_tracks=''):
  album = {}
  if num_tracks:
    album = {'artist': artist.title(), 'title': title, 'tracks': num_tracks}
  else:
    album = {'artist': artist.title(), 'title': title}
  return album
print(make_album('taylor swift', '1989'))
print(make_album('taylor swift', 'Red', 13))

while True:
  print("(enter 'q' at any time to quit)")

  artist = input('Enter artist name: ')
  if artist == 'q':
    break

  title = input('Enter album title: ')
  if title == 'q':
    break

  tracks_valid = False
  while tracks_valid != True:
    try:
      tracks = input('Enter number of tracks (optional): ')
      if tracks == 'q':
        break
      if tracks != '':
        tracks = int(tracks)
      tracks_valid = True
    except:
      print('Enter a valid int!')

  album = make_album(artist, title, tracks)
  print(album)
