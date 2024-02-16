def author_format(names: list) -> str:
    formated_auhtors_list = []
    for name in names:
        formated_name_list = []
        formated_name = ""
        name_split = name.split(" ")
        n = -1
        
        for x in range(len(name_split)):
            formated_name_list.append(name_split[n])
            n += 1
            
        for x in range(1, len(formated_name_list)):
            formated_name_list[x] = ([*formated_name_list[x]][0]).upper()
            
        formated_name = f"{formated_name_list[0]}, "
        for initial in range(1, len(formated_name_list)):
            formated_name += (formated_name_list[initial] + ".")
            
        formated_auhtors_list.append(formated_name)
    
    if len(formated_auhtors_list) > 1:
        authors = ""
        for x in range(len(formated_auhtors_list)-1):
            authors += f"{formated_auhtors_list[x]}, "
        
        authors = authors[:-2]
        authors += f" & {formated_auhtors_list[-1]}"
            
        return authors
    
    else:
        return formated_auhtors_list[0]
            

def harvard_format_book(d: dict) -> str:
 
    if d.get("title") == None:
        raise ValueError("Title is None")
    else:
        title = d.get("title")
    
    if d.get("d_o_p") == None:
        raise ValueError("d_o_p is None")
    else:
        d_o_p = d.get("d_o_p")
    
    if d.get("authors") == None:
        raise ValueError("Author is None")
    else:
        authors = author_format(d.get("authors"))
    
    if d.get("publisher") == None:
        raise ValueError("Publisher is None")
    else:
        publsiher = d.get("publisher")
        
    if d.get("edition") == None:
        raise ValueError("Edition is None")
    else:
        edition = d.get("edition")
       
    y_o_p = d_o_p.split("-")[-1]
    
    if d.get("page_nums") != None:
        page_nums = d.get("page_nums")
        return f"<p>{authors} ({y_o_p}). <i>{title}</i>. {edition}. edition. {publsiher}, {page_nums}.</p>"
    else:
        return f"<p>{authors} ({y_o_p}). <i>{title}</i>. {edition}. edition. {publsiher}.</p>"
    

def harvard_format_article(d:dict) -> str:
    if d.get("title") == None:
        raise ValueError("Title is None")
    else:
        title = d.get("title")
    
    if d.get("d_o_p") == None:
        raise ValueError("d_o_p is None")
    else:
        d_o_p = d.get("d_o_p")
    
    if d.get("authors") == None:
        raise ValueError("Author is None")
    else:
        authors = author_format(d.get("authors"))
    
    if d.get("publisher") == None:
        raise ValueError("Publisher is None")
    else:
        publsiher = d.get("publisher")
    
    if d.get("url") == None:
        raise ValueError("url is None")
    else:
        url = d.get("url")
        
    if d.get("access_date") == None:
        raise ValueError("Access_date is None")
    else:
        access_date = d.get("access_date")
    
    y_o_p = d_o_p.split("-")[0]
    d_m = d_o_p.split("-")[-1] + "-" + d_o_p.split("-")[1]
    
    return f"<p>{authors} ({y_o_p}). {title}. <i>{publsiher}</i>. {d_m}. {url} (Accessed {access_date}).</p>"
    
  
def build_export_string(source_data:dict) -> str:
    if source_data.get("category") == None:
        raise ValueError("Category is None")
    else:
        category = source_data.get("category")
    
    if category == "book":
        res = harvard_format_book(source_data)
        return res
    
    elif category == "article":
        res = harvard_format_article(source_data)
        return res

            
if __name__ == "__main__":
    source_data = { 
    "category": "article",
    "title":  "500 skämt om papperssortering",
    "d_o_p":  "2012-11-15",
    "authors": ["Vidar Silas Mörk", "Eddie Ekbacke", "William Carl Svensson"],
    "publisher":  "Bonnier",
    "page_nums":  "21-22",
    "edition": "5",
    "url": "www.youtube.com/video",
    "access_date": "2012-11-21"
}
    res = build_export_string(source_data)
    print(res)
    
   