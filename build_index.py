import json
import re

with open("pages.json","r",encoding="utf-8") as f:
    pages = json.load(f)
       
    
index = {}

for page_id,page in enumerate(pages):
    
    content = page["content"].lower()
    
    words = re.findall(r'\w+',content)
    for word in words:
        
        if word not in index:
            index[word]=[]
            
        if page_id not in index[word]:
            index[word].append(page_id)
            
print("Total unique words :",len(index))
print()
print("love ->",index.get("love"))
print("romance ->",index.get("romance"))
print("dog ->",index.get("dog"))     

with open("index.json","w",encoding="utf-8") as f:
    json.dump(index,f,indent=4)        
                  