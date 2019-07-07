#  __    __  ____    __    ____    ______  
# |  |  |  | \   \  /  \  /   /   |____  | 
# |  |__|  |  \   \/    \/   / ______ / /  
# |   __   |   \            / |______/ /   
# |  |  |  |    \    /\    /        / /    
# |__|  |__|     \__/  \__/        /_/    

# Song Dictionary
Song = {
  # Song's title
  "title"         : "All the small things",
  # Song's album
  "album"         : "Enema of the State",
  # Song's artist
  "artist"        : "Blink-182",
  # Song's record label
  "label"         : "MCA Records",
  # Song'genre
  "genre"         : "IPunk rock",
  # Song's duration in minutes
  "durationInMin" : 2.8,
  # Album's yaer
  "year"          : 1999,
  # Track number in album
  "trackNum"      : 8
}

# return parsed value of second argument based on first argument data type
def typeParse(oType, strValue):
  t = type(oType)
  if t is int:
    return int(strValue)
  if t is float:
    return float(strValue)
  if t is bool:
    return bool(strValue)
  if t is str:
    return strValue
  return None

# Check if key value pair is in the Sogng dictionary
def guessKV(key, value):
  if key in Song:
    return Song[key] == typeParse(Song[key],value)
  return False


# Start the game to guess the keys and values combinations
def playTheGame():
  while (True): # True==True
    inKey = input("Enter the key:\n")
    inVal = input("Enter the value:\n")
    if guessKV(inKey, inVal):
      print("You are right!")
    else:
      print("oops.. wrong key value pair")


# Print all keys in Song dictionary
def printSong():
  for k in Song:
    if k == 'title':
      print("--------------------------")
    print(k, ":", Song[k])
    if k == 'title':
      print("--------------------------")
  print("--------------------------")  

# print 
printSong()
# print()
print("Time to play!")
playTheGame()
