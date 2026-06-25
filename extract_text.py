import requests
import json
from bs4 import BeautifulSoup

pages = []

with open("urls.txt","r",encoding="utf-8") as f:
    urls = f.readlines()
    
for url in urls[:10]:
    
    url = url.strip()
    
    try:
        response = requests.get(url)
        
        soup = BeautifulSoup(response.text,"html.parser")
        
        text = soup.get_text()
        
        pages.append({
    "url": url,
    "content": text
       })
        
        print("\nURL:",url)
        print(text[:500]) 
        print("-"*50)
        
    except Exception as e:
        print("Error: ",e) 
        
print("Pages collected:", len(pages))              
        
with open("pages.json","w",encoding="utf-8") as f:
    json.dump(pages,f,indent=4)  
    
print("pages.json created successfully")          