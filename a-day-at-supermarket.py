#!/opt/bin/python
import sys
print "Spend calculator for a @ Super Market"

#Code start from here

#shopping_list = ["banana", "orange", "apple", "pear"]
#shopping_list = str(sys.argv[1]).split(',')
stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
if len(str(sys.argv[1])) > 0:
  shopping_list = str(sys.argv[1]).split(',')
  def compute_bill(food):
    total = 0
    for item in food:
      if stock[item] > 0:
        total += prices[item]
        stock[item] = stock[item] - 1
    return total
else:
  print "No Item selected for shopping"

print "Total order cost %s" % compute_bill(shopping_list)

