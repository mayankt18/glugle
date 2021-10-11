# **FLASK GUIDE**

In one line Flask is a **python web framework** that helps in creating web applications. Although flask is a vast topic, in this article we are going to learn the part of flask which we require for building our project.

## Installation

Install flask in your system using

```python
pip install flask
```

## A Minimal Flask app

A minimal Flask application looks something like this:

```python
# an object of WSGI application

from flask import Flask	
app = Flask(__name__) # Flask constructor

# A decorator used to tell the application
# which URL is associated function
@app.route('/')	
def hello():
	return 'HELLO'

if __name__=='__main__':
app.run()
```
The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.
 
## Running the App
Save the file as hello.py or something similar. Make sure to not call your application flask.py because this would conflict with Flask itself.
Run the application by flask run command.

## Routing

Nowadays, the web frameworks provide routing techniques so that users can remember the URLs. It is useful to access the web page directly without navigating from the Home page. It is done through the following route() decorator, to bind the URL to a function.

## Decorator to route URL
```python
@app.route(‘/hello’)
```

## Binding to the function of route
```python
def hello_world():	
 return ‘hello world’
```

If a user visits ```http://localhost:5000/hello``` URL, the output of the hello_world() function will be rendered in the browser. The ```add_url_rule()``` function of an application object can also be used to bind a URL with the function as in the above example.



# **The Web App**

We are going to make the web app using [flask library](https://www.youtube.com/watch?v=Z1RJmh_OqeA&ab_channel=freeCodeCamp.org) in python.
There will be two pages one the homepage and the other the search results page.

## Basic structure of the web application:
<img src="diagrams/webapp_workflow.png" width="90%">

<br/>

The application consists of two functions. 

- The entry_point function which is present at route “/” and it’s only purpose is to render the homepage template. The homepage template is a form with an input field and a submit button which redirects you to the search_results function with the input data.

- The search_results function performs most of the task of the application. The tasks it performs are listed below:
 
    1. It connects to mongodb where data collected by crawler is stored using pymongo and connection url.
        ```python
        client = pymongo.MongoClient(connection_url, connect=False)
        
        database = client.name_of_database
        ```
    
    2. It gets the search query in a variable named “search_string” from request.args
        ```python
        search_string = request.args.get('name_of_the_input_field_in_homepage')
        ```
    
    3. It then performs a search in [mongodb](https://docs.mongodb.com/manual/text-search/) for results matching the “search_string” and stores them in a variable named “query”.
    <br/>

    4. It may be possible that there are duplicate results in the list “query”. So we need to filter them out and store the other result in a new list “search_result” which we will pass to the template for displaying to the user. Hence all the results in the “query” variable are iterated over and if a result with same title and url is found to be already present in “search_result” we don’t add them to “search_result”.
        ```python
        for object in query_obtained_from_mongodb_search:
        exist = False
        for result in search_result:
            if result['title'] == object['title'] or result['url'] == object['url']:
                exist = True
                break

        if exist == False:
            search_result.append(doc)
        ```
    
    5. Ranking the “search_result” according to the search query is also done in the search_results function which is discussed later.
    <br/>
    6. Pagination of the results can be done using the [flask-paginate](https://pythonhosted.org/Flask-paginate/) library.
    <br/>
    7. Finally the list “search_result” is passed to the template “search.html” where it is displayed.
 

## The Templates:
The templates used in the project are written in jinja2 language. A quick guide to the language can be found [here](https://realpython.com/primer-on-jinja-templating/).
