# data-extraction-from-email

About: The project is to extract useful information from the email, send by the clients and automatically fill the Gmail Add-on and placing order after verification

Technology Used:
•	Natural Language Processing
•	Python
•	Google AppScript
•	Flask Framework
•	Heroku server

Process:
•	Opening Gmail message and then Gmail Add-on
•	Gmail add-on will take out the body, username of sender, and email ID of sender from Gmail message and make a HTTP POST request to Heroku server, passing the body as the argument 
•	The Heroku server will run the python code uploaded on it and process the data to extract the useful information like- pickup Address, Drop Address, Contact No., date
•	Now this all will be arrange Order wise and finally a json file will be returned
•	This json will be used to dynamically create and fill the Gmail Add-on
•	The verification and manipulation in the Addon will be done by the admin
•	Then on clicking Place Order button one more verification will be done to check whether any of the following text box is empty or not, if empty then it will pop up a notification else it will place order successfully

Detailed Description of Project:
Python code:
Import few libraries
to import regular expression
import re
to import complete NLP related files
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.tree import Tree
to make https request
import requests
to work with json file
import json
to access todays date
import datetime
from datetime import date
these are the two most important libraries
Approach for drop locations:
Tokenize the string and give tags to each word, A grammar is created by studying the pattern of the mail for Drop Address, then chunking is performed for creating a chunking tree which have drop location separated out.
From there we fetched out drop location and store it in a list

Approach for pickup locations:
Again, grammar is the key, A grammar is created for pickup locations then regular expression are used to find the pickup locations and storing into the list
Approach for vehicle:
 grammar4 = r'\bdost|bolero|tata\sace|tata\ssuper\sace|canter\s14|14ft|14\sft|canter\s17|17ft|17\sft|canter\s19|19ft|19\sft|20ft|20\sft|canter\s20|tata\s407|bolero|dost\b'
vehicle_type= re.findall(grammar4,stringlower)

Since the number of vehicles were fixed so all possible ways by which people can call them is written in the grammar and these are the two lines used for finding the vehicle and storing it into list
Approach for Contact:
A grammar is created for Contact number and regular expression is used for finding and storing Contact numbers
r = re.compile(r'(\d{3,4}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)

Approach for date:
A grammar is created for Date and regular expression is used for finding and storing the date, if no date format is found then it will search for keyword tomorrow to set tomorrow’s day and if it is also then by default today’s date
dates=re.findall("(\d+/?-?\.\d+/?-?\.\d+)",string )
        # print(date)
        if len(dates)==0:
            today=date.today()
            today = today.strftime("%d/%m/%Y")
            if(stringlower.find("tomorrow")!=-1):
                tomorrow=datetime.date.today() + datetime.timedelta(days=1)
                tomorrow =tomorrow.strftime("%d/%m/%Y")
                dates.append(tomorrow)
            else:
                dates.append(today)

Approach of differentiating the orders:
All the information is with us, now the only thing left is arranging them order wise. Index of each element plays vital role in it
The index of all the pickups, drop, and vehicle are stored into different list and then nested for loop is used to differentiate the orders, the trick is since vehicle of a particular order will come ahead of all pickup locations and all pickup locations will come ahead of all drop location for a particular order , if still some elements are left in list then they are part of next order
Structure of data returned by Python:
{
“main”:[
    {
      “pickup”:[],
      “drop”:[],
      “vehicle”:[]
    },
    {
      “pickup”:[],
      “drop”:[],
      “vehicle”:[]
    }
  ],
“date”:[],
“mobile”:[]
}





Flask Framework:
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions
Flask Code:
from flask import Flask
app=Flask(__name__)
#all import and download statement here
#all other helping function here 
@app.route(“/post”, methods =[‘POST’, ’GET’])
def gmail_addon():
    if request.method=='POST':
#write you main function of python code here
if __name__ == "__main__":
app.run()




Heroku Server:
Heroku is a cloud platform as a service (PaaS) supporting several programming languages. Heroku, one of the first cloud platforms, has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.
How to use:
•	Register on Heroku
•	Download and install Heroku CLI
•	Download and install git
•	Copy your script or project to this repository's folder
•	Replace "script.py" with the path to your main executable file in Procfile
web: gunicorn gmail_addon_nlp:app

•	You may select your python version and runtime using runtime.txt

•	If you are using any not built-in modules, you must add them to your requirements.txt. To check which version of the module you have, run pip freeze in the terminal. You will get lines with information about installed modules and their versions in the format like MODULE_NAME==MODULE_VERSION. Add lines with required modules and their versions to your requirements.txt. Don't keep unused modules in requirements.txt. This file should contain every module your application needs. Heroku will install modules from this file automatically.

•	Open terminal (or do it another way, but I will explain how to do it in the terminal on Ubuntu) and create a git repository.
•	Initiate git repository
git init
•	Create heroku application
heroku create
•	Add, commit and push your code into branch master of the remote heroku.
git add .
git commit -m "initial commit"
git push heroku master
•	Specify the amount of worker that will run your application
heroku ps:scale worker=1
•	Now everything should be working. You can check your logs with this command
heroku logs --tail
•	You can open the URL where the script is deployed using the below command (if you are deploying web application)
heroku open
•	From now on you can use usual git commands (push, add, commit, etc.) to update your app. Every time you push heroku master your app gets redeployed with updated source code
•	To stop your application scale down the amount of workers with like this
heroku ps:scale worker=0






Gmail Add-on
Google Apps Script code:
This is the language used for building the Add-on 
Two Files:
•	appsscript.json
•	Code.gs
appsscript.json
This file contains permissions which are required or authorization, things which will be constant throughout Add-on like colour etc and name of function which will be triggered on opening Add-on
Code.gs
This file has all the functions, elements and logics which make out the Add-on
Two lines for accessing message from email- 
var accessToken = e.messageMetadata.accessToken;
  GmailApp.setCurrentMessageAccessToken(accessToken);
Code for fetching the body and from ID 
  var messageId = e.messageMetadata.messageId;
  var message = GmailApp.getMessageById(messageId);
  var sender = message.getFrom();
Eight functions: -
•	buildAddOn() - this function gives initials which will appear on the addon
•	addpickup() - this function is bind with +Pickup Button to add an extra Pickup textbox in particular order
•	removepickup() - It is bind with -Pickup Button to remove one pickup location per click in particular order
•	adddrop() - It is bind with +Drop Button to add an extra Drop textbox in particular order
•	removedrop() - It is bind with -Drop Button to remove one drop location per click in particular order
•	addvehicle() - function is bind with +vehicle Button to add an extra vehicle dropdown  in a particular order
•	removepickup() - it is bind with -vehicle Button to remove one vehicle dropdown menu  in particular order
•	placeorder() - It is associated with Place Order Button for final verification and placing order
The key here is the e object that we pass to every function because that e object has a json file having all key value pair of all the where the key is the unique field name given to every element and value is the text or value it contains. 
updated_data=e.formInput;
var parameter = e.parameters;
Every time we hit a function this e object is passed to the function with latest updated data which is further used in every function to recreate the card
And at last every function will update the card
return CardService.newNavigation().updateCard(card.build());
Why Add-on is recreated in every function: - because Google Apps Script is a server-side Scripting language and DOM Manipulation is not possible in it, so to add the any element we have to recreate the card again and update the card.

