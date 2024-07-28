import asyncio
from fetch_course_information import get_course_url
from scrape import scrape_raw_html
from utils.parse_course_information import get_course_information_from_html
import pandas as pd
import random
from tqdm import tqdm

import os
from dotenv import load_dotenv

load_dotenv()
QUERY_URL = os.getenv('QUERY_URL')

def get_truly_random_intervals():
    chance_sub_15 = 0.8
    chance_sub_40 = 0.9

    r = random.random()
    if r < chance_sub_15:
        return random.randint(3, 15)
    elif r < chance_sub_40:
        return random.randint(15, 20)
    else:
        return random.randint(20, 30)
    

async def greedy_scrape():
    df = pd.read_csv('data/course-inventory.csv')
    cache_df = pd.DataFrame()
    try: 
        for i, row in tqdm(df.iterrows(), total=df.shape[0]):
            course = row['Prefix']
            number = row['Number']
            url = get_course_url(course, number, '202501')
            print(f'attempting to scrape {course}{number}...')
            random_interval = get_truly_random_intervals()
            try:
                returned_html = await scrape_raw_html(url)
                returned_mapping = get_course_information_from_html(returned_html)
                assert len(returned_mapping) == 10
                course_mapping = pd.DataFrame([get_course_information_from_html(returned_html)])
                cache_df = pd.concat([cache_df, course_mapping], ignore_index=True)
                print(f'scraping complete, now sleeping for {random_interval} seconds')
            except Exception as e:
                print(f'error occurred while scraping {course}{number}. now sleeping the thread for {random_interval} seconds')
                with open('errored_columns_log.txt', 'a') as f:
                    f.write(f'parsing error encountered: {course}{number}\n')
                continue
            finally: 
                await asyncio.sleep(random_interval)
    except Exception as e:
        print('An error occurred:', e)
    finally:
        cache_df.to_csv('course-descriptions.csv', index=False)
        print('done')
    
if __name__ == '__main__':
    asyncio.run(greedy_scrape())