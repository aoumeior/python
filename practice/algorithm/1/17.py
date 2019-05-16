
# Extracting a Subset of a Dictionary
prices = {'ACME': 45.23,
          'AAPL': 612.78,
          'IBM': 205.55,
          'HPQ': 37.20,
          'FB': 10.75}
# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}


# Much of what can be accomplished with a dictionary comprehension might also be done by creating a sequence of tuples and passing them to the dict() function.
p3 = dict((key, value) for key, value in prices.items() if value > 200)
