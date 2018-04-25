class Item:
    name = ""
    colour = ""

class Quadruple:
    target = Item()
    competitor = Item()
    distractor1 = Item()
    distractor2 = Item()

class Row:
    pair = Quadruple()
    condition = ""
    target_side = ""
 
def count_colours(quad_list):
  colours = []
  for quad in quad_list:
    colours.append(quad.target.colour)
    colours.append(quad.competitor.colour)
    colours.append(quad.distractor1.colour)
    colours.append(quad.distractor2.colour)
  colour_counts = {}  
  unique_colours = set(colours)
  for colour in unique_colours:
    print colour
    colour_counts[colour] = colours.count(colour)
  return colour_counts 

q1 = Quadruple()
q1.target.name = "book"
q1.target.colour = "green"
q1.competitor.name = "chair"
q1.competitor.colour = "blue"
q1.distractor1.name = "apple"
q1.distractor1.colour = "red"
q1.distractor2.name = "pear"
q1.distractor2.colour = "green"
my_list = []
my_list.append(q1)
colour_counts = count_colours(my_list)
print colour_counts