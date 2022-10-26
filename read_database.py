import csv
import json
import pprint
###     class recipe(models.Model):
###         title = models.CharField(max_length=255)
###         directions = models.TextField
###         content = models.TextField()
###         ingredients = models.ForeignKey(ingredient,on_delete=models.CASCADE)
###         category = models.CharField(max_length=255)

###     class ingredient(models.Model):
###         name =  models.CharField(max_length=255)
###         quantity = models.CharField(max_length=20)
###         unit =  models.CharField(max_length=50)

#create model to hold stuff 
recipe ={}

#Input stuff into model
with open('recipes.csv', newline='') as f:
    #file stuff
    reader = csv.reader(f)
    #we dont care about the first row
    row_titles = next(reader)
    row = next(reader)
    #init recipe list
    rec_list = []
    one_ingredient = {}
    one_recipe ={}
    print(row)
    for item in reader:
        #print("item: ",item)
        #get recipe info
        one_recipe ["title"] = item[0]
        one_recipe ["directions"] = item[1]
        ing_list = []
        # get ingredients list
        for x in range(2,59, 3):
            if item[x] :
                print(item[x+2])
                one_ingredient ["name"]=item[x+2]
                one_ingredient ["quantity"]= item[x]
                one_ingredient ["unit"]= item[x+1]
            ing_list.append(one_ingredient)
        #add ingredients list to recipe
        one_recipe  ["ingredients"]= ing_list
        one_recipe  ["Category"]=  item[(19*3)+1] # this should be the last row
        #done reading line push to list
        rec_list.append(one_recipe)
        #reset one_recipe
        one_recipe ={}
        ing_list = []
        break

item = rec_list[0]
myJSON = json.dumps(item)

# Displaying the JSON format
print("JSON format = ",myJSON)
