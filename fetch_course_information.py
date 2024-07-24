import requests
from dotenv import load_dotenv
import os

load_dotenv()
QUERY_URL = os.getenv('QUERY_URL')

def get_query_string(abbrev, number, school_term):
    return f"p_subj={abbrev}&p_crse={number}&p_term={school_term}"

def get_course_url(abbrev, number, school_term):
    return QUERY_URL + get_query_string(abbrev, number, school_term)

def get_course_information(abbrev, number, school_term):
    URL = QUERY_URL + get_query_string(abbrev, number, school_term)
    print(URL)
    response = requests.get(URL)
    return response

if __name__ == '__main__':
    print('attempting to fetch course information...')
    response = get_course_information('COP', '4530', '202501')
    print(response.text)
    print('done')