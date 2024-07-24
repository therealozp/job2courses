import os
from dotenv import load_dotenv

from scrape import scrape_raw_html
from fetch_course_information import get_course_url
import asyncio


print('attempting to fetch course information...')
url = get_course_url('COP', '4530', '202501')
print('attempting to scrape...')
asyncio.run(scrape_raw_html(url))
print('done')