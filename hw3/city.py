"""I am looking for a city with the largest amount of Irish bars
   If there are many cities with the same amount of Irish bars I will choose the city with the lowest average check 
"""
import json

with open("cities.json","r") as f:
    data=json.load(f)

# Here we find all cities with at least one Irish bar, count of bars and average check 
best_cities={}    
for city in data:
    for bars in city["bars"]:
        if bars["chain"]=="Irish":
            if best_cities.get(city["city"]):
                avcheck=best_cities[city["city"]]["average_check"]
                nirish=best_cities[city["city"]]["number_of_irish_bars"]
                best_cities[city["city"]]["average_check"]=(avcheck*nirish+bars["check"])/(nirish+1)
                best_cities[city["city"]]["number_of_irish_bars"]+=1                
            else:
                best_cities[city["city"]]={"number_of_irish_bars":1,"average_check":bars["check"]}

# Now it's time to choose the best city
best_city=""
best_n_bars=0
best_check=1e6
for city,values in best_cities.items():
    if values["number_of_irish_bars"]>best_n_bars:
        best_n_bars=values["number_of_irish_bars"]
        best_city=city
        best_check=values["average_check"]
    elif values["number_of_irish_bars"]==best_n_bars:
        if values["average_check"]<best_check:
            best_city=city
            best_ckeck=values["average_check"]

print("The best city to live is",best_city,end="\n\n\n")
        
# task 2
companies={}
for city in data:
    for company in city["company"]:
        if companies.get(company["name"]) is None:
            companies[company["name"]]=[city["city"]]
        else:
            if companies[company["name"]][-1]==city["city"]:
                continue
            else:
                companies[company["name"]].append(city["city"])

if __name__=="__main__":
    print("Amazon has branches in the following cities",companies["Amazon"],sep="\n")