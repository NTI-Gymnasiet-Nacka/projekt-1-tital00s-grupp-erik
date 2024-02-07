
def harvard_format(d: dict) -> str:
    if d.get("category") == None:
        raise ValueError("Category is None")
    else:
        category = d.get("category")
    
    if d.get("title") == None:
        raise ValueError("Title is None")
    else:
        title = d.get("title")
    
    if d.get("d_o_p") == None:
        d_o_p = "d_o_p not available"
    else:
        d_o_p = d.get("d_o_p")
    
    if d.get("authors") == None:
        authors = "Authors unknown"
    else:
        authors = d.get("authors")
    
    if d.get("publisher") == None:
        publsiher = "Unknown publisher"
    else:
        publsiher = d.get("publisher")
        
    

if __name__ == "__main__":
    source_data = { 
    "catagory": "",
    "title":  "hej",
    "d_o_p":  "12-12-2012",
    "authors": "hejsan",
    "publisher":  "tja",
    "page_nums":  "21-22",
    "edition": "5",
    "url": "www.youtube.com",
    "access_date":  "12-11-2012"
}
    print(source_data)
    res = harvard_format(source_data)
    print(res)
   