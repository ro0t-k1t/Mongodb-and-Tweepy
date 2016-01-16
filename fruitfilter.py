__author__ = 'ronanpiercehiggins'


def remove_rotten(bag_of_fruits):


  my_arr = []

  for word in bag_of_fruits:
      if "rotten" not in word:
          my_arr.append(word)


  return my_arr

arr = ["rottenApple","rottenBanana","rottenApple","rottenPineapple","rottenKiwi", "apple","banana","apple","pineapple","kiwi"]

print remove_rotten(arr)


