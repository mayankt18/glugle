# WEB CRAWLER

The word “crawler” itself can be intimidating to many people but it is basically a script having a few lines of code. 

A web crawler, spider, or search engine bot downloads and indexes content from all over the Internet. They're called "web crawlers" because crawling is the technical term for automatically accessing a website and obtaining data via a software program.
The crawler goes from page to page and stores the data fetched from it in the database, so that the information can be retrieved when it's needed.
## APPROACH TO BUILD THE CRAWLER
- We are going to use the following python libraries to achieve the task
    - “requests” library to fetch the pages.
    - “beautifulsoup4”  to parse the response received from the response object.
    - “pymongo” to connect to mongodb where we are going to store the data.
    - Yes that’s it, that’s all we need.
- We will build a python class named “Crawler” inside the crawler.py file.
- The first thing we want to do is to make a connection with our database using “pymongo” library.
- After the connection is made we are going to define two methods inside the class “Crawler” named “start_crawling” and “crawl”. 
- Both of the methods mentioned above are going to take two arguments:
    - “url” (string containing the url to the page we want to parse)
    - “depth” (integer parameter to control the number of pages your program crawls)
  
      <img src="diagrams/crawler.png" width="50%">

### THE “start_crawl” FUNCTION
This function starts the process of crawling. It performs the task of collecting the links in robots.txt and storing them in a list named “disallowed_links”. 
The “url”, “depth” and “disallowed_links” are then passed to the crawl function where the actual process of crawling begins.
**Note that some urls may not have any robots.txt file so, use a try except block while looking for robots.**

## THE “crawl” FUNCTION
This is the function where most of the things are done. First we define it with the parameters “url”, “depth” and “disallowed_links”. Then inside the function the following takes place.
- It tries to connect to the provided url using the “requests” library.
- If request returns a response it parses the content returned from the first step using the “Beautifulsoup” library and looks for <title> tags and <p> tags which it saves in the title and description variables respectively.
- After completion of all the above steps it creates a dictionary named “query”with url, title and description in it which will be saved in the database.
```
    query = {
        	‘url’ : url,
        	‘title’ : title,
        	‘description’ : description
        }
```
- This query is saved in the database using ```insert_one()``` method for mongodb.
- Next it checks if “depth” is equal to zero or not. If it is zero the functions stops, else it collects all the links present in the page using “Beautifulsoup” and stores them in a list named “links”
- It then loops through all the links and for each link it calls the crawl with the depth variable decremented by one  like this:
```
    self.crawl(link, depth-1)
```
- Atlast it closes the connection it made with the database.


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
   my_crawler.start(url,depth) 

```

### Packages used in making the crawler

The packages can be installed using  ```pip install package-name```
The packages used are  **BeautifulSoup, urllib, request and  pymongo.**

[Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

[urllib python documentation](https://docs.python.org/3/library/urllib.html)

[Request python documentation](https://docs.python-requests.org/en/latest/)

[Pymongo python documentation](https://pymongo.readthedocs.io/en/stable/)

Use **mongodb atlas** to store data retrieved from the crawler.
