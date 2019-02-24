# PGCorpV-2.0
Faster, better, loaded with new features.<br>
More details to be added later.<br>
Something fascinating is coming.<br>

# The Following instructions will get the website running on your local machine

1. Install python on your machine from the website https://www.python.org/downloads/
2. Use Pip(python's package manager) to install virtualenv.
3. Open the command prompt and type in the following command
```
pip install virtualenv
```
4. Once virtualenv is installed, navigate to you preferred directory using command prompt and type the following command to create a new virual environment
```
virtualenv env
```
5. Once the virtual environment is installed, type the following command.
```
env\Scripts\activate
```
A virtual environment will be activated.<br>
6. Now download the zip, extract it, navigate to it using the command prompt and run.
```
pip install -r requirements.txt
```
This will install all the required packages.<br>
7. Now type the following command.
```
python manage.py runserver
```
A development server will start.<br>
8. To view the website, go to http://127.0.0.1:8000 using your choice of browser.
