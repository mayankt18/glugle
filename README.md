[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)


# Quick Links

- [How to run the project](https://github.com/mayankt18/glugle#search-engine-made-using-python-and-flask)
    
    ### Documentation
    - [Introduction](https://github.com/mayankt18/glugle/blob/master/resources/1.I.search%20engine.md#search-engine-basics)
    - Setup ([Linux](https://github.com/mayankt18/glugle/blob/master/resources/1.II.setup.md#python-installation-guide) / [Windows](https://github.com/mayankt18/glugle/blob/master/resources/1.II.setup_win.md#project-setup-in-windows))
    - [Mongo DB setup](https://github.com/mayankt18/glugle/blob/master/resources/2.I.mongodb.md#mongodb-installation-linux-ubuntu)
    - [Crawler](https://github.com/mayankt18/glugle/blob/master/resources/2.II.crawler.md#web-crawler)
    - [Flask Guide](https://github.com/mayankt18/glugle/blob/master/resources/3.flask.md#flask-guide)
    - [Web application](https://github.com/mayankt18/glugle/blob/master/resources/4.web%20app.md#the-web-app)
    - [Query Processing](https://github.com/mayankt18/glugle/blob/master/resources/5.ranking.md#query-preprocessing)
    - [Ranking the searches](https://github.com/mayankt18/glugle/blob/master/resources/5.ranking.md#ranking-mechanism)  

# Search engine made using Python and flask

## Project Setup

1. Clone the git in a folder
2. Make a virtual environment in the folder

**For Windows**
```
pip install virtualenv
cd project_folder
virtualenv env
.\env\Scripts\activate
```

**For Linux**
```
pip install virtualenv #for version 2 and below 
pip3 install virtualenv #for version 3
cd project file
virtualenv env
source ./env/bin/activate
```

3. Install requirements
```
pip3 install -r requirements.txt
```

4. Start the crawler
```
python ./crawler/spider.py #for version 2 and below
python3 ./crawler/spider.py #for version 3
```

5. Start the application
```
python ./app/app.py #for version 2 and below
python3 ./app/app.py #for version 3
```

