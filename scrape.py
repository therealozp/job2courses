from playwright.async_api import async_playwright
from utils.proxies import get_random_proxy
import asyncio

async def scrape_raw_html(url): 
    async with async_playwright() as p:
        prox = get_random_proxy()
        print('running on proxy:', 'http://' + prox)
        browser = await p.chromium.launch(
            proxy={
                'server': prox,
            }
        )
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_timeout(5000)
        raw_html = await page.content()
        with open('errored_html.html', 'w') as f:
            f.write(raw_html)
        await browser.close()


if __name__ == '__main__':
    print('attempting to scrape...')
    asyncio.run(scrape_raw_html('COP', '4530'))
    print('done')
