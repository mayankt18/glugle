# Search engine made using python and flask

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

