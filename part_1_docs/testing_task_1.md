### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
# class has not been initiated with def __init__ including variables.

  def check_for_ace(self, card):
    # below should be double equals. 
    if card.value = 1:
      return True
    # no colon below
    else
      return False
   
# def rather than dif. There is no comma between card1 and card2.
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    # "card" doesn't exist below, it should be "card1".
    return card 
  else:
    return card2
    # no case for if they are equal. 
  


def cards_total(self, cards):
  # total is not initiated as "= 0"
  total
  for card in cards:
    total += card.value
    # need to change total to a string to add it to the return statement below. Also, indentation for return should be in line with "for"
    return "You have a total of" + total
  
```
