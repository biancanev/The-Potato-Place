def pokemon_journey():
  print "You just started a Poekmon Journey!"
  print "Before you start you must make sure to type everyhting in lowercase otherwise the game will crash!" .upper()
  print "
  "
  print "Do you choose Charmander, Squirtle, Bulbasaur, or Pikachu?"
  answer = raw_input("Type Charmander, Squirtle, Bulbasaur, or Pikachu and hit 'Enter'.")
  if answer == "charmander":
    print "
    Brock and Misty destroy you and your Charmander dies. :) YOu lose:)".upper()
  elif answer == "bulbasaur":
    print "
    Your started choice has no data on it because no one chose it.:)".upper()
  elif answer == "pikachu":
    print "
    FUCK OFF ASH YOU LOSE :)".upper()
  elif answer == "squirtle":
    print "
    You have an advantage against most gyms and become a Pokemon Master! You win, this is the shortest game ever!".upper()
  else:
    print "
    Choose a goddamn starter man! (or woman, gender equality) Get a Pokedex!".upper()
    
pokemon_journey()
