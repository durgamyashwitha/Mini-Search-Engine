import requests
from bs4 import BeautifulSoup
from collections import deque
from urllib.parse import urljoin

start_url = "https://quotes.toscrape.com"

queue = deque()
visited = set()
count =0
MAX_PAGES = 10

queue.append(start_url)
visited.add(start_url)

while queue and count <MAX_PAGES:
    url = queue.popleft()
    
    print("visiting :",url)
    
    try:
        response = requests.get(url)
        
        print(response.status_code)
        print(response.text[:500])
        
        soup = BeautifulSoup(response.text,"html.parser")
        
        links = soup.find_all("a")
        
        for link in links:
            
            href = link.get("href")
            
            if not href:
                continue
            full_url = urljoin(url,href)
            
            if full_url not in visited:
                visited.add(full_url)
                queue.append(full_url)
                print("Added :",full_url)
                
        count+=1;        
    except Exception as e:
        print("Error : ",e)
        
        
print("\nTotal no:",count)        
print("\nTotal pages discoverd : ",len(visited))    
print("\nWaiting :",len(queue))


with open("urls.txt", "w", encoding="utf-8") as f:
    for url in visited:
        f.write(url + "\n")

print("URLs saved to urls.txt")       
        