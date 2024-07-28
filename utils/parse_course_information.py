from bs4 import BeautifulSoup

def get_course_information_from_html(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    table_elements = soup.select('td > font')
    i = 0
    mapping = {}
    while i < len(table_elements):
        if i == 0: 
            # first element has 3 fields
            key = table_elements[i].getText().rstrip(":").lower()
            value = table_elements[i + 2].getText().replace('\n', '')
            i += 3
        else: 
            key = table_elements[i].getText().rstrip(":").lower()
            value = table_elements[i + 1].getText().replace('\n', '')
            i += 2
        mapping[key] = value
    
    return mapping

if __name__ == '__main__':
    with open('html/COP_4530.html') as f:
        raw_html = f.read()
        
    print(get_course_information_from_html(raw_html))