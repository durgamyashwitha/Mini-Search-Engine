import json
import re
import math

with open("pages.json","r",encoding="utf-8") as f:
    pages = json.load(f)
    
with open("index.json","r",encoding="utf-8") as f:
    index = json.load(f)
    
def search(query):
    query_words = query.lower().split()
    candidate_pages = None
    
    for word in query_words:
        if word not in index:
            return []
        
        pages_with_word = set(map(int,index[word]))
        
        if candidate_pages is None:
             candidate_pages = pages_with_word
        else:
            candidate_pages &= pages_with_word
            
    scores = {}
    N = len(pages)
    
    for page_id in candidate_pages:
        content = pages[page_id]["content"].lower()
        words = re.findall(r'\w+',content)
        
        total_score = 0
        
        for word in query_words:
            
            tf = words.count(word)
            df = len(index[word])
            idf = math.log((N + 1)/(df + 1)) + 1
            total_score += tf * idf
        scores[page_id] = total_score
            
    ranked_results = sorted(\
             scores.items(),
             key=lambda x: x[1],
             reverse = True
            )  
    results = []
        
    for page_id,score in ranked_results:
            
        results.append({
                "title": " ".join(pages[page_id]["content"].split()[:10]),
                "url" : pages[page_id]["url"],
                "score": round(score,3),
                "preview": pages[page_id]["content"][:250]+ "...."
            })      
            
    return results                          
