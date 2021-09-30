<!-- # **WEB CRAWLER**

A web crawler, spider, or search engine bot downloads and indexes content from all over the Internet. They're called "web crawlers" because crawling is the technical term for automatically accessing a website and obtaining data via a software program.

The bot learns what every webpage on the web is about, so that the information can be retrieved when it's needed.These bots are needed in search engines. 
### So , what exactly happens ?
- We pass the site URL to the crawl function  along with the depth.
- The  URL gets used as a method to check for robots.txt . Store the disallowed links in a list. Pass - the disallowed links ,depth, url  to the self crawl function.
- self crawl function performs http get requests and retrieves the title and description , url .
- Stores the search results including url, title , description in the database.
- Check for the depth if it's zero.
- Store all the reference anchor tags in a list and ignore the disallowed links. Then check for http in it to get the html links. 
- Decrease the depth and since self crawl is recursive , call self crawl again .

### Packages used in making the crawler

The packages can be installed using **pip install package-name**

The packages used are **BeautifulSoup , request and  pymongo.**

Use **mongodb atlas** to store data retrieved from the crawler. -->


# **WEB CRAWLER**

Now you have seen how search engines work , so let's start with putting the first stone of your search engine.

A web crawler, spider, or search engine bot downloads and indexes content from all over the Internet. They're called "web crawlers" because crawling is the technical term for automatically accessing a website and obtaining data via a software program.




# *The Bot*
 It learns what every web page on the web is about, so that the information can be retrieved when it's needed.These bots are needed in search engines. 

# *Import the libraries*

   We use ```pip install package-name``` to install the libraries . Then in the `spider.py` we *import* them.
   ```python
    from bs4 import BeautifulSoup
    import requests
    import pymongo
    import os
    import urllib.parse
   ```
    

### So , what exactly happens ?

- We pass the site URL to the start function  along with the depth.
- The  URL gets used as a method to check for robots.txt . Store the disallowed links in a list. Pass - the disallowed links ,depth, url  to the self crawl function.
- self crawl function performs http get requests and retrieves the title and description , url .
- Stores the search results including url, title , description in the database.
- Check for the depth if it's zero.
- Store all the reference anchor tags in a list and ignore the disallowed links. Then check for http in it to get the html links. 
- Decrease the depth and since self crawl is recursive , call self crawl again .

# *Program Structure*

### Define class and check for robots.txt

```python
  #we declare a class Crawler()
  class Crawler():
      #get client url from mongodb using pymongo lib 
      connect_url = os.getenv('MONGO_URL')
      #store the results in a db and declare a list to store url details
      searchresults = []
      #define function to start crawling through the given url and depth
      def start(self, url , depth):
         #use urllib lib to read the disallowed links in the robots.txt of the url
         disallowed_url = urllib.parse.urljoin(url,'/robots.txt')
         #uses BeautifulSoup lib to store all the paragraph text of the file 
         soup= BeautifulSoup(robots.txt , 'lxml')
         content = soup.find('p').text
         disallowed_links = []
         #we check for the url in the robots.txt path of the url and store it.
         disallowed_links.append(urllib.parse.urljoin(url, word))
```
### Crawl function

```python         
      def crawl(self,url, *disallowed_links):
         #we send http get request on the url and store the response
         response = requests.get(url)
         #we look for title and description in the url
         title = soup.find('title').text
         if #try to look for p tages 
            description = tag.text.strip().replace('\n', '')
         #Create a dictionary to store the required data fields
         query ={

         }
         searchresults= self.db.searchresults #searchresults is in the db
         #Insert the retrived data query in the table defined in the database
         searchresults.insert_one(query)
         #store the id of each data query in the db
         searchresults.create_index({
 
         })
         #If depth becomes 0 exit the function
         #Create a list to store all links in the url
         links = soup.findAll('a')
         #check for all the links except disallowedlinks & pass it to the crawl function
         self.crawl(link['href'], depth - 1)
         #close the db access
         self.client.close()
```

### Calling the function

```python
   #create an object to pass the function
   my_crawler = Crawler() 
   #send url and depth as parameters to start crawling
   crawler.start(url,depth) 

```

### Packages used in making the crawler

The packages can be installed using  ```pip install package-name```
The packages used are  **BeautifulSoup, urllib, request and  pymongo.**

[Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

[urllib python documentation](https://docs.python.org/3/library/urllib.html)

[Request python documentation](https://docs.python-requests.org/en/latest/)

[Pymongo python documentation](https://pymongo.readthedocs.io/en/stable/)

Use **mongodb atlas** to store data retrieved from the crawler.
  


