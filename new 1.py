def mars_news():

   # Visit the mars nasa news site
   url = 'https://redplanetscience.com/'
   browser.visit(url)

   # Optional delay for loading the page
   browser.is_element_present_by_css('div.list_text', wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = soup(html, 'html.parser')

   slide_elem = news_soup.select_one('div.list_text')
   slide_elem.find('div', class_='content_title')

   # Use the parent element to find the first <a> tag and save it as  `news_title`
   news_title = slide_elem.find('div', class_='content_title').get_text()
   news_title

   # Use the parent element to find the paragraph text
   news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
   news_p
   
def mars_news():

   # Visit the mars nasa news site
   url = 'https://redplanetscience.com/'
   browser.visit(url)

   # Optional delay for loading the page
   browser.is_element_present_by_css('div.list_text', wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = soup(html, 'html.parser')

   slide_elem = news_soup.select_one('div.list_text')

   # Use the parent element to find the first <a> tag and save it as `news_title`
   news_title = slide_elem.find('div', class_='content_title').get_text()

   # Use the parent element to find the paragraph text
   news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

   return news_title, news_p
   
   