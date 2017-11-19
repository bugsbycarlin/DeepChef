# titles = []
# directions = []

# with open("pg11067.txt", "r") as infile:
#   for line in infile.readlines():
#     line = line.strip()
#     if not line:
#       continue
#     if len(line) < 70:
#       titles.append(line)
#     else:
#       directions.append(line)

# with open("titles_pg11067.txt","w") as outfile:
#   for title in titles:
#    outfile.write(title + "\n")

# with open("directions_pg11067.txt","w") as outfile:
#   for direction in directions:
#     outfile.write(direction + "\n\n")





# titles = []
# directions = []
# ingredients = []

# last_line = None
# with open("pg26323.txt", "r") as infile:
#   for line in infile.readlines():
#     full_line = line
#     line = line.strip()
#     if not line:
#       continue
#     if last_line == "------":
#       titles.append(line)
#     elif "          " in full_line:
#       ingredients.append(line)
#     elif line == "------":
#       last_line = line
#       continue
#     else:
#       directions.append(line)

#     last_line = line

# with open("titles_pg26323.txt","w") as outfile:
#   for title in titles:
#    outfile.write(title + "\n")

# with open("directions_pg26323.txt","w") as outfile:
#   for direction in directions:
#     outfile.write(direction + "\n")

# with open("ingredients_pg26323.txt","w") as outfile:
#   for ingredient in ingredients:
#     outfile.write(ingredient + "\n")




# titles = []
# directions = []
# ingredients = []

# last_line = None
# with open("pg31534.txt", "r") as infile:
#   for line in infile.readlines():
#     full_line = line
#     line = line.strip()
#     if not line:
#       continue
#     if line.isupper():
#       titles.append(line.lower())
#     elif "          " in full_line:
#       ingredients.append(line)
#     else:
#       directions.append(line)


# with open("titles_pg31534.txt","w") as outfile:
#   for title in titles:
#    outfile.write(title + "\n")

# with open("directions_pg31534.txt","w") as outfile:
#   for direction in directions:
#     outfile.write(direction + "\n")

# with open("ingredients_pg31534.txt","w") as outfile:
#   for ingredient in ingredients:
#     outfile.write(ingredient + "\n")




# titles = []
# directions = []

# with open("pg31102.txt", "r") as infile:
#   for line in infile.readlines():
#     line = line.strip()
#     if not line:
#       continue
#     if line.isupper():
#       titles.append(line.lower())
#     else:
#       directions.append(line)


# with open("titles_pg31102.txt","w") as outfile:
#   for title in titles:
#    outfile.write(title + "\n")

# with open("directions_pg31102.txt","w") as outfile:
#   for direction in directions:
#     outfile.write(direction + "\n")




titles = []
directions = []

with open("pg33246.txt", "r") as infile:
  for line in infile.readlines():
    line = line.strip()
    if not line:
      continue
    parts = line.split(".")
    if parts[0].isupper():
      titles.append(parts[0].lower())
      if len(parts) > 1:
        directions.append(parts[1].replace("--",""))
    else:
      directions.append(line)


with open("titles_pg33246.txt","w") as outfile:
  for title in titles:
   outfile.write(title + "\n")

with open("directions_pg33246.txt","w") as outfile:
  for direction in directions:
    outfile.write(direction + "\n")


