import requests
from bs4 import BeautifulSoup
import time
import csv
#####MOLIM SVE KOJI BUDU GLEDALI DA ZAZMURE NA NAZIVE PROMJENJIVIH I TO STO NISAM PRAVIO FUNKCIJE
url = "https://www.udg.edu.me/fakulteti/"
response = requests.get(url)
data = BeautifulSoup(response.text, "html.parser")

# Step 1: Get faculty URLs
all_divs = data.find_all("div", class_="f-item-text-box")
hrefs = [div.find("a").get("href") for div in all_divs]

urls = ["https://www.udg.edu.me/" + href[1:] for href in hrefs]


responses = []
for url in urls:
    res = requests.get(url)
    uni = BeautifulSoup(res.text, "html.parser")
    small = uni.find("small")
    
    if small:
        link = small.text.strip()
        if link[-1] == "/":
            link += "predavaci"
        else:
            link += "/predavaci"
        responses.append(link)
    # time.sleep(1) 

responses.pop() 

# print(responses)
all_prof = []
name_divs = []
for res in responses:
    all_data = requests.get(res)
    name_div = BeautifulSoup(all_data.text, "html.parser")
    name_divs.append(name_div)

universities = ["fmefb", "fkt", "fist", "politehnika", "fpn", "hs", "fu", "fptbhe", "fsm", "fdm", "ff", "fprn"]
full_data = []
i = 0
for name_div in name_divs:
    #namediv contains full html of each page
    profa_tag = name_div.find_all("a", class_="teacher-name") 
    #profa tag contains all profesor a page
    for tag in profa_tag:
        #for each page, get all names and store them in all_prof
        all_prof.append(tag.text.strip())
    full_data.append({universities[i] : all_prof})
    #full_data is a list of dictionaries where each key is in format
    all_prof = []
    i+=1

        
# print(full_data)

titule = ["Prof", "Mr", "Dr", "Doc. Dr", "Prof. Dr", "Doc. Mr" ]
i = 0
with open("title_counts.csv", "w", newline="", encoding="utf-8") as file:
  writer = csv.writer(file)
  for faks in full_data:
      titules = []
      name_uni = list(faks.keys())[0]  #university name
      names_prof = faks[name_uni]  #a list of profesors in that university
      for each_name in names_prof:
          # print("Prof. Dr".upper(), each_name.upper())
          # print("Prof. Dr".upper() in each_name.upper())
          if "Prof. dr ".upper() in each_name.upper():
            titules.append("Prof. dr".upper())
          elif "Prof ".upper() in each_name.upper():
              titules.append("Prof".upper())
          elif "Doc. Dr ".upper() in each_name.upper():
            titules.append("Doc. Dr".upper())
          elif "Mr ".upper() in each_name.upper():    
              titules.append("Mr".upper())
          elif "Dr ".upper() in each_name.upper():   
              titules.append("Dr".upper())
          elif "Doc. Mr ".upper() in each_name.upper():   
              titules.append("Doc. Mr".upper())
          else:
              titules.append("No titule")
      dict_titules = {"Prof" : titules.count("Prof".upper()),
                      "Dr" : titules.count("Dr".upper()),
                      "Mr" : titules.count("Mr".upper()),
                      "Doc. Dr" : titules.count("Doc. Dr".upper()),
                      "Prof. Dr" : titules.count("Prof. Dr".upper()),
                      "Doc. Mr" : titules.count("Doc. Mr".upper()),
                      "No titule" : titules.count("No titule")}
      writer.writerow([name_uni, dict_titules])
      
print("DONE")
