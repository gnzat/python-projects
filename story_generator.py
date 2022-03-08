import random
when = ["Yesterday", "On New Year's eve", "Last October", "During Christmas", "A few years ago"]
who = ["a cat", "a hamster", "a teacher", "a hairdresser", "an ostrich"]
name = ["Alice", "Daniel", "Jamie", "Alex", "Denise"]
residence = ["Paris", "Toa Payoh", "Singapore", "Germany", "London"]
went = ["cinema", "school", "home", "mall", "concert"]
happened = ["eats popcorn", "changed his hairstyle", "found a secret pathway", "washes clothes", "exercises"]
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in '+ random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened) + '.')

