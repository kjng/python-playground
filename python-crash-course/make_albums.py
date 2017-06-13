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
