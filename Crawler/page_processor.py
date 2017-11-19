"""

  page_processor.py
  Matthew Carlin
  November 2017

  Processes one page of openeats.org into a training case for the DeepChef hidden markov model.
  This training case just contains untokenized text in the following format:

  title
  -----
  blurb
  -----
  ingredients
  -----
  directions

"""
import BeautifulSoup

def process(url, page_source):
  try:
    soup = BeautifulSoup.BeautifulSoup(page_source)

    file_name_root = url[(url.index("recipe/") + 7):].replace("-","_").replace("/","")
    #print file_name_root

    title = soup.findAll("div", { "class" : "page-header" })[0].text
    #print title

    blurb = soup.findAll("ul", { "class" : "recipe-groups" })[0].parent.findAll("p")[-1].text.encode("ascii", "ignore")
    #print blurb

    if "http" in blurb or len(blurb) < 50:
      blurb = ""

    ingredient_elements = soup.findAll("div", { "class": "panel panel-default" })[0].findAll("li", { "class": "list-group-item" })
    #print ingredient_list
    ingredients = [" ".join(item.text.encode("ascii", "ignore").split()) for item in ingredient_elements]
    #print ingredients

    directions = []
    directions_elements = None
    direction_root = soup.findAll("ol", { "class": "expanded" })
    if not direction_root:
      direction_root = soup.findAll("ol", { "class": "list-numbers recipe-directions__list" })
    if direction_root:
      directions_elements = direction_root[0].findAll("li")
    else:
      direction_root = soup.findAll("div", { "class": "panel-body" })
      directions_elements = direction_root[0].findAll("p")
      if not directions_elements:
        directions_elements = direction_root[0].findAll("ul")
        if directions_elements:
          directions_elements = directions_elements[0].findAll("li")
      if not directions_elements:
        directions_elements = direction_root[0].findAll("ol")
        if directions_elements:
          directions_elements = directions_elements[0].findAll("li")
    if directions_elements:
      directions = [" ".join(item.text.encode("ascii", "ignore").split()) for item in directions_elements]
    #print directions

    with open("../Training/" + file_name_root + ".txt", "w") as outfile:
      outfile.write(title + "\n")
      outfile.write("-----" + "\n")
      outfile.write(blurb + "\n")
      outfile.write("-----" + "\n")
      outfile.write("\n---\n".join(ingredients) + "\n")
      outfile.write("-----" + "\n")
      outfile.write("\n---\n".join(directions) + "\n")
  except:
    pass



