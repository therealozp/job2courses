from playwright.async_api import async_playwright
import asyncio

async def main(abbrev, number): 
    URL = f'https://usfonline.admin.usf.edu/pls/prod/wp_search_catalog_db?p_subj={abbrev}&p_crse={number}&p_term=202501'
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(URL)
        raw_html = await page.content()
        with open(f'{abbrev}_{number}.html', 'w') as f:
            f.write(raw_html)
        await browser.close()

if __name__ == '__main__':
    print('attempting to scrape...')
    asyncio.run(main('COP', '4530'))
    print('done')
