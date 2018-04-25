import csv
#import codecs
import random
from compiler.syntax import check

class Item:
    name = ""
    colour = ""

class Quadruple:
    target = Item()
    competitor = Item()
    distractor1 = Item()
    distractor2 = Item()
    condition = ""

class Row:
    pair = Quadruple()
    condition = ""
    target_side = ""

# Read in the data
targets_nf = []
targets_af = []
targets_anf = []
competitors_nf = []
competitors_af = []
competitors_anf = []
distractors = []

with open("input/targets_nf.csv", "rU") as csvfile:
  data_reader = csv.reader(csvfile, delimiter=";", dialect=csv.excel)
  for row in data_reader:
    new_item = Item()
    new_item.name = row[0]
    new_item.colour = row[1]
    targets_nf.append(new_item)

with open("input/targets_af.csv", "rU") as csvfile:
  data_reader = csv.reader(csvfile, delimiter=";", dialect=csv.excel)
  for row in data_reader:
    new_item = Item()
    new_item.name = row[0]
    new_item.colour = row[1]
    targets_af.append(new_item)
    
with open("input/targets_anf.csv", "rU") as csvfile:
  data_reader = csv.reader(csvfile, delimiter=";", dialect=csv.excel)
  for row in data_reader:
    new_item = Item()
    new_item.name = row[0]
    new_item.colour = row[1]
    targets_anf.append(new_item)

with open("input/competitors_nf.csv", "rU") as csvfile:
  data_reader = csv.reader(csvfile, delimiter=";", dialect=csv.excel)
  for row in data_reader:
    new_item = Item()
    new_item.name = row[0]
    new_item.colour = row[1]
    competitors_nf.append(new_item)

with open("input/competitors_af.csv", "rU") as csvfile:
  data_reader = csv.reader(csvfile, delimiter=";", dialect=csv.excel)
  for row in data_reader:
    new_item = Item()
    new_item.name = row[0]
    new_item.colour = row[1]
    competitors_af.append(new_item)
    
with open("input/competitors_anf.csv", "rU") as csvfile:
  data_reader = csv.reader(csvfile, delimiter=";", dialect=csv.excel)
  for row in data_reader:
    new_item = Item()
    new_item.name = row[0]
    new_item.colour = row[1]
    competitors_anf.append(new_item)
    
with open("input/distractors.csv", "rU") as csvfile:
  data_reader = csv.reader(csvfile, delimiter=";", dialect=csv.excel)
  for row in data_reader:
    new_item = Item()
    new_item.name = row[0]
    new_item.colour = row[1]
    distractors.append(new_item)

def randomise(a_list):
  counter = len(a_list) - 1
  while (counter > -1):
    # Draw random number and swap with element at counter
    random_number = random.randrange(0, len(a_list) - 1)
    temp = a_list[counter]
    a_list[counter] = a_list[random_number];
    a_list[random_number] = temp;
    counter -= 1
  return a_list

def find_matching_tripple_noun(targets, distractors1, distractors2, competitors):
  noun_contrast = []
  used_competitors = []
  used_twice_competitors = []
  used_thrice_competitors = []
  used_distractors1 = []
  used_distractors2 = []
  for target in targets:    
    for i in range(0, len(competitors)):
      competitor = competitors[i]
      new_quadruple = None
      if (target.colour == competitor.colour
          and target.name != competitor.name
          and not competitor in used_competitors):
        new_quadruple = find_distractors(target, competitor, distractors1, distractors2, used_distractors1, used_distractors2)
      # when no competitor can be found, go through used competitors
      if (new_quadruple == None and i == len(competitors) - 1):
        for used_competitor in used_competitors:
          if (target.colour == used_competitor.colour
              and target.name != used_competitor.name
              and not used_competitor in used_thrice_competitors):
            new_quadruple = find_distractors(target, used_competitor, distractors1, distractors2, used_distractors1, used_distractors2)
            if (competitor in used_twice_competitors):
              used_thrice_competitors.append(used_competitor)
            else:
              used_twice_competitors.append(used_competitor)
      # if a nice quadruple can finally be found
      if (new_quadruple != None):
        used_competitors.append(new_quadruple.competitor)
        used_distractors1.append(new_quadruple.distractor1)
        used_distractors2.append(new_quadruple.distractor2)
        new_quadruple.condition = "NF"
        noun_contrast.append(new_quadruple)
        break
  return noun_contrast

def find_matching_tripple_adj(targets, distractors1, distractors2, competitors):
  noun_contrast = []
  used_competitors = []
  used_twice_competitors = []
  used_thrice_competitors = []
  used_distractors1 = []
  used_distractors2 = []
  for target in targets:
    for i in range(0, len(competitors)):
      competitor = competitors[i]
      new_quadruple = None
      if (target.colour != competitor.colour
          and target.name == competitor.name
          and not competitor in used_competitors):
        new_quadruple = find_distractors(target, competitor, distractors1, distractors2, used_distractors1, used_distractors2)
      # when no competitor can be found, go through used competitors
      if (new_quadruple == None and i == len(competitors)-1):
        for used_competitor in used_competitors:
          if (target.colour != used_competitor.colour
              and target.name == used_competitor.name
              and not used_competitor in used_thrice_competitors):
            new_quadruple = find_distractors(target, used_competitor, distractors1, distractors2, used_distractors1, used_distractors2)
            used_thrice_competitors.append(used_competitor)
          if (competitor in used_twice_competitors):
            used_thrice_competitors.append(used_competitor)
          else:
            used_twice_competitors.append(used_competitor)
      # if a nice quadruple can finally be found
      if (new_quadruple != None):
        used_competitors.append(new_quadruple.competitor)
        used_distractors1.append(new_quadruple.distractor1)
        used_distractors2.append(new_quadruple.distractor2)
        new_quadruple.condition = "AF"
        noun_contrast.append(new_quadruple)
        break
  return noun_contrast

def find_matching_tripple_adjnoun(targets, distractors1, distractors2, competitors):
  noun_contrast = []
  used_competitors = []
  used_twice_competitors = []
  used_thrice_competitors = []
  used_distractors1 = []
  used_distractors2 = []
  for target in targets:    
    for i in range(0, len(competitors)):
      competitor = competitors[i]
      new_quadruple = None
      if (target.colour != competitor.colour
          and target.name != competitor.name
          and not competitor in used_competitors):
        new_quadruple = find_distractors(target, competitor, distractors1, distractors2, used_distractors1, used_distractors2)
      # when no competitor can be found, go through used competitors
      if (new_quadruple == None and i == len(competitors)-1):
        for used_competitor in used_competitors:
          if (target.colour != used_competitor.colour
              and target.name != used_competitor.name
              and not used_competitor in used_thrice_competitors):
            new_quadruple = find_distractors(target, used_competitor, distractors1, distractors2, used_distractors1, used_distractors2)
            used_thrice_competitors.append(used_competitor)
          if (competitor in used_twice_competitors):
            used_thrice_competitors.append(used_competitor)
          else:
            used_twice_competitors.append(used_competitor)
      # if a nice quadruple can finally be found
      if (new_quadruple != None):
        used_competitors.append(new_quadruple.competitor)
        used_distractors1.append(new_quadruple.distractor1)
        used_distractors2.append(new_quadruple.distractor2)
        new_quadruple.condition = "ANF"
        noun_contrast.append(new_quadruple)
        break
  return noun_contrast

def find_distractors(target, competitor, distractors1, distractors2, used_distractors1, used_distractors2):
  # go through all possible distractors to find 1st match
  for j in range(0, len(distractors1)):
    distractor1 = distractors1[j]
    if (target.colour != distractor1.colour 
        and target.name != distractor1.name
        and competitor.name != distractor1.name
        and competitor.colour != distractor1.colour
        and not distractor1 in used_distractors1):
      # go trough all possible distractors to find 2nd match
      for k in range(0, len(distractors2)):
        distractor2 = distractors2[k]
        if (target.colour != distractor2.colour 
            and target.name != distractor2.name
            and competitor.name != distractor2.name 
            and competitor.colour != distractor2.colour
            and not distractor2 in used_distractors2
            and not (distractor1.name == distractor2.name 
                     and distractor1.colour == distractor2.colour)):
          new_quadruple = Quadruple()
          new_quadruple.target = target
          new_quadruple.competitor = competitor
          new_quadruple.distractor1 = distractor1
          new_quadruple.distractor2 = distractor2       
          return new_quadruple

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
    colour_counts[colour] = colours.count(colour)
  return colour_counts

def check_randomisation(a_list):
  adjacent_conditions = 0
  for i in range(0, len(a_list) - 2):    
    
    # target color must not equal next competitor color
    if (a_list[i].target.colour == a_list[i+1].competitor.colour):
      return "bad"
    
    # target name must not equal next competitor name
    if (a_list[i].target.name == a_list[i+1].competitor.name):
      return "bad"
    
    # no three adjacent conditions
    if (i < (len(a_list) - 2)):
      if ((a_list[i].condition == a_list[i+1].condition) and (a_list[i].condition == a_list[i+2].condition)):
        return "bad"

    # count how many adjacent conditions exists
    if (a_list[i].condition == a_list[i+1].condition):
      adjacent_conditions += 1

  # only allow adjacent conditions in 12% of cases
  if (adjacent_conditions > len(a_list) * 0.12):
    return "bad"
  
  return "good"

list_counter = 0

for y in range(1, 31):
  found = False
  while (found == False):
    
    # Data structures for noun contrast
    all_items_n = randomise(targets_nf)
    competitors_n = randomise(competitors_nf)
    distractors1_n = randomise(distractors)
    distractors2_n = randomise(distractors)
    
    # Data structures for adjective contrast
    all_items_a = randomise(targets_af)
    competitors_a = randomise(competitors_af)
    distractors1_a = randomise(distractors)
    distractors2_a = randomise(distractors)

    # Data structures for adjective-noun contrast
    all_items_an = randomise(targets_anf)
    competitors_an = randomise(competitors_anf)
    distractors1_an = randomise(distractors)
    distractors2_an = randomise(distractors)
    
    noun_contrast = find_matching_tripple_noun(all_items_n, distractors1_n, distractors2_n, competitors_n)
    adj_contrast = find_matching_tripple_adj(all_items_a, distractors1_a, distractors2_a, competitors_a)
    adjnoun_contrast = find_matching_tripple_adjnoun(all_items_an, distractors1_an, distractors2_an, competitors_an)
    
    all_lists = noun_contrast + adj_contrast + adjnoun_contrast
    colour_counts = count_colours(all_lists)
    
    sum_of_colour_counts = 0
    for colour in colour_counts:
      sum_of_colour_counts = sum_of_colour_counts + colour_counts[colour]
    mean_of_colour_counts = sum_of_colour_counts / len(colour_counts)
       
    if (len(noun_contrast) == 15 and len(adj_contrast) == 10 and len(adjnoun_contrast) == 10): 
      found = True
      for colour in colour_counts:
        if (colour_counts[colour] == mean_of_colour_counts):
          found = False

      if (found == True):
        complete_list_randomised = noun_contrast + adj_contrast + adjnoun_contrast
        found = False
        while (found == False):
          complete_list_randomised = randomise(complete_list_randomised)
          if (check_randomisation(complete_list_randomised) == "good"):
            repetition_list = complete_list_randomised
            c = 0
            while (found == False and c < len(complete_list_randomised) - 1):
              if (check_randomisation(complete_list_randomised + repetition_list) == "bad"):
                repetition_list[c], repetition_list[c+1] = repetition_list[c+1], repetition_list[c]
              elif (check_randomisation(complete_list_randomised + repetition_list) == "good"):
                found = True
                complete_list_randomised = complete_list_randomised + repetition_list
              c = c + 1
 
  list_counter = list_counter + 1
  
  with open('output/' + str(list_counter)  + '.csv', 'wb') as csvfile:
    listwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    listwriter.writerow(['condition', 'target_name' , 'target_colour', 'competitor_name', 'competitor_colour', 'distractor1_name', 'distractor1_colour', 'distractor2_name', 'distractor2_colour'])
    for quad in complete_list_randomised:
      listwriter.writerow([quad.condition, quad.target.name, quad.target.colour, quad.competitor.name, quad.competitor.colour, quad.distractor1.name, quad.distractor1.colour, quad.distractor2.name, quad.distractor2.colour])
      