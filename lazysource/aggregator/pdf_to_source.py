import pdfplumber

# keyword = 'Authors'

def extract_pdf(pdf_path):
    
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        font_groups = {}
        
       # Group characters by font size
        for obj in first_page.chars:
            font_size = obj['size']
            text = obj['text']
            font_groups.setdefault(font_size, []).append(text)
        
        # Find the group with the largest font size
        largest_font_group = max(font_groups.keys())
        title = ''.join(font_groups[largest_font_group])
        
        title = title.strip()
        
        return title
        
#        for page in pdf.pages[:3]:
#            text = page.extract_text()
#            
#            # Search for keyword
#            index = text.find(keyword) # Returns -1 if no result found
#            if index != -1:
#                # Find the next newline character after the keyword
#                newline_index = text.find('\n', index)
#                if newline_index != -1:
#                    # Extract the line after the keyword
#                    line = text[newline_index+1:].split('\n')[0].strip()
#                    return line
#    return None

if __name__ == "__main__":
    
    path = 'C:\\Users\\anton.maksymchuknet\\Desktop\\pdftest\\FULLTEXT01.pdf'
    print(extract_pdf(path))
