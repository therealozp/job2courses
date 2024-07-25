from playwright.async_api import async_playwright
from utils.proxies import get_random_proxy
import asyncio

async def scrape_raw_html(url): 
    try: 
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url)
            await page.wait_for_timeout(5000)
            raw_html = await page.content()
            await browser.close()
            return raw_html
    except Exception as e:
        print('While running, an exception occurred:', e)
        raise e

if __name__ == '__main__':
    print('attempting to scrape...')
    asyncio.run(scrape_raw_html('COP', '4530'))
    print('done')
