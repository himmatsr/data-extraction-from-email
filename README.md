# Information Extraction from Email

# About
The project is to extract useful information from the email, send by the clients and automatically fill the Gmail Add-on and place order after verification

# Technology Used:
*  Natural language processing
*  python
*  Google AppScript
*  Platform :
    *  Flask Framework
    *  heroku Server

# Process:
*  Opening Gmail message and then Gmail Add-on
*  Gmail add-on will take out the body, username of sender, and email ID of sender from Gmail message and make a HTTP POST request to Heroku server, passing the body as the argument 
*  The Heroku server will run the python code uploaded on it and process the data to extract the useful information like- pickup Address, Drop Address, Contact No., date
*  Now this all will be arrange Order wise and finally a json file will be returned
*  This json will be used to dynamically create and fill the Gmail Add-on
*  The verification and manipulation in the Addon will be done by the admin
*  Then on clicking Place Order button one more verification will be done to check whether any of the following text box is empty or not, if empty then it will pop up a notification else it will place order successfully
<br>
[Project Model Image](https://imgur.com/rT2Z1Ej)
<br>
<br>
<br>
[Project FlowChart Image](https://imgur.com/p11vru1)
<br>

# Tool Used:
*  Visual Studio
*  Google Script Editor

# How to Proceed:
*  write python code
*  test python code
*  write Code for Addon in Google App Script
*  Synchronize python and App Script code using mocky.io
*  Write flask code and tested it on local machine
*  Put python code on Heroku server 
*  Test and debug code
*  Publish it on G Suite Marketplace SDK

# How to Install Product:

## PreRequiste: Gmail Account
## Steps to install
*	Open Gmail
*	Click on Settings icon
*	Click on Get Add-ons
*	Search for PlaceIT 
*	Click on Add-on named PlaceIT
*	Click on Install
*	Give Permissions
*	After installation completes a Add-on appears on right side with icon 

# How to Use:
*	Login to Gmail
*	Open the message 
*	Click on Add-on appearing on the right
*	Verify details and manipulate accordingly and click on place order

# Detailed Description of Project:
## Python code:
### Import few libraries
to import regular expression
<br>
`import re`
<br>
to import complete NLP related files
<br>
`import nltk`<br>
`from nltk.tokenize import word_tokenize` <br>
`from nltk.tokenize import RegexpTokenizer` <br>
`from nltk.corpus import stopwords` <br>
`from nltk.tag import pos_tag` <br>
`from nltk.chunk import ne_chunk` <br>
`from nltk.tree import Tree`<br>

to make https request<br>
`import requests`
<br>
to work with json file
<br>
`import json` <br>
to access todays date <br>
`import datetime` <br>
`from datetime import date` <br>
these are the two most important libraries <br>
 <br>
 ## Approach for drop locations:
 <br>
 Tokenize the string and give tags to each word, A grammar is created by studying the pattern of the mail for Drop Address, <br> then chunking is performed for creating a chunking tree which have drop location separated out
 <br>
 From there we fetched out drop location and store it in a list
 
 ## Approach for pickup locations:
 
 ` grammar4 = r'\bdost|bolero|tata\sace|tata\ssuper\sace|canter\s14|14ft|14\sft|canter\s17|17ft|17\sft|canter\s19|19ft|19\sft|20ft|20\sft|canter\s20|tata\s407|bolero|dost\b'`
 <br>
 `vehicle_type= re.findall(grammar4,stringlower)`
 <br>
 
 Since the number of vehicles were fixed so all possible ways by which people can call them is written in the grammar and these are the two lines used for finding the vehicle <br>and storing it into list
 
 ## Approach for Contact:
 
 A grammar is created for Contact number and regular expression is used for finding and storing Contact numbers
 <br>
 `r = re.compile(r'(\d{3,4}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')`
 <br>
 `phone_numbers = r.findall(string)`
 
 ## Approach for date:
 
 A grammar is created for Date and regular expression is used for finding and storing the date, if no date format is found then it will search for keyword tomorrow to set<br> tomorrow’s day and if it is also then by default today’s date
 <br>
 `dates=re.findall("(\d+/?-?\.\d+/?-?\.\d+)",string )`<br>
 `        # print(date)`<br>
 `       if len(dates)==0:`<br>
 `           today=date.today()`<br>
 `          today = today.strftime("%d/%m/%Y")`<br>
 `          if(stringlower.find("tomorrow")!=-1):`<br>
 `              tomorrow=datetime.date.today() + datetime.timedelta(days=1)`<br>
 `              tomorrow =tomorrow.strftime("%d/%m/%Y")`<br>
 `              dates.append(tomorrow)`<br>
 `          else:`<br>
 `              dates.append(today)`<br>
 
 ## Approach of differentiating the orders:
 All the information is with us, now the only thing left is arranging them order wise. Index of each element plays vital role in it<br>
The index of all the pickups, drop, and vehicle are stored into different list and then nested for loop is used to differentiate the orders, the trick is since vehicle of a<br> particular order will come ahead of all pickup locations and all pickup locations will come ahead of all drop location for a particular order , if still some elements are left in list then they are part of next order
<br>
<br>

Structure of data returned by Python:
<br><br>

`{`<br>
` “main”:[ `<br>
`    { `<br>
`     “pickup”:[],`<br>
`      “drop”:[],`<br>
`      “vehicle”:[]`<br>
`    },`<br>
`    {`<br>
`      “pickup”:[],`<br>
`      “drop”:[],`<br>
`      “vehicle”:[]`<br>
`    }`<br>
`  ],`<br>
`“date”:[],`<br>
`“mobile”:[]`<br>
`}`<br>

# Flask Framework:

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction<br> layer, form validation, or any other components where pre-existing third-party libraries provide common functions

## Flask Code:

`from flask import Flask`<br>
`app=Flask(__name__)`<br>
`#all import and download statement here`<br>
`#all other helping function here `<br>
`@app.route(“/post”, methods =[‘POST’, ’GET’])`<br>
`def gmail_addon():`<br>
`    if request.method=='POST':`<br>
`#write you main function of python code here`<br>
`if __name__ == "__main__":`<br>
`app.run()`<br>

# Heroku Server:
Heroku is a cloud platform as a service (PaaS) supporting several programming languages. Heroku, one of the first cloud platforms, has been in development since June 2007,<br> when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.
## How to use:

*	Register on Heroku
*	Download and install Heroku CLI
*	Download and install git
*	Copy your script or project to this repository's folder
*	Replace "script.py" with the path to your main executable file in <b>Procfile</b><br>
                       `web: gunicorn gmail_addon_nlp:app`
*   You may select your python version and runtime using runtime.txt
*   If you are using any not built-in modules, you must add them to your <b>requirements.txt</b>. To check which version of the module you have, run pip freeze in the terminal.<br> You will get lines with information about installed modules and their versions in the format like <b>MODULE_NAME==MODULE_VERSION</b>. Add lines with required modules and <br>their versions to your <b>requirements.txt</b>. Don't keep unused modules in <b>requirements.txt</b>. This file should contain every module your application needs. Heroku will<br> install modules from this file automatically.
*   Open terminal (or do it another way, but I will explain how to do it in the terminal on Ubuntu) and create a git repository.
*   Initiate git repository<br>`git init`
*   Create heroku application<br>`heroku create`
*   Add, commit and push your code into branch master of the remote heroku.<br>
`git add .`<br>
`git commit -m "initial commit"`<br>
`git push heroku master`
*	Specify the amount of worker that will run your application<br>
`heroku ps:scale worker=1`
*	Now everything should be working. You can check your logs with this command<br>
`heroku logs --tail`
*	You can open the URL where the script is deployed using the below command (if you are deploying web application)<br>
`heroku open`
*	From now on you can use usual git commands (push, add, commit, etc.) to update your app. Every time you push heroku master your app gets redeployed with updated source code
*	To stop your application scale down the amount of workers with like this<br>
`heroku ps:scale worker=0`


# Gmail Add-on
## Google Apps Script code:
This is the language used for building the Add-on <br>
Two Files:
*	appsscript.json
*	Code.gs

### appsscript.json
This file contains permissions which are required or authorization, things which will be constant throughout Add-on like colour etc and name of function<br> which will be triggered on opening Add-on
<br>

### Code.gs
This file has all the functions, elements and logics which make out the Add-on<br>
Two lines for accessing message from email-<br> 
`var accessToken = e.messageMetadata.accessToken;`<br>
  `GmailApp.setCurrentMessageAccessToken(accessToken);`<br>
Code for fetching the body and from ID <br>
  `var messageId = e.messageMetadata.messageId;`<br>
  `var message = GmailApp.getMessageById(messageId);`<br>
  `var sender = message.getFrom();`<br>
  
<br>
Eight functions :

*	buildAddOn():first function that will be triggered, it will check for cache and depending on cache it will generate the initial card
*	signin(): it will hit the API with username and password and depending upon it will allow user to fetch details
*	SignoutFunction(): it will help user to sign out
*	buildFunction() - this function will print all the information on addon
*	addpickup() - this function is bind with `+Pickup` Button to add an extra Pickup textbox in particular order
*	removepickup() - It is bind with `-Pickup` Button to remove one pickup location per click in particular order
*	adddrop() - It is bind with `+Drop` Button to add an extra Drop textbox in particular order
*	removedrop() - It is bind with `-Drop` Button to remove one drop location per click in particular order
*	addvehicle() - function is bind with `+vehicle` Button to add an extra vehicle dropdown  in a particular order
*	removepickup() - it is bind with `-vehicle` Button to remove one vehicle dropdown menu  in particular order
*	placeorder() - It is associated with `Place Order` Button for final verification and placing order
*   addOrder() - It is associated with `+Order` Button for adding a new Order having single pickup, drop and vehicle type

The key here is the <b>e object</b> that we pass to every function because that e object has a json file having all key value pair of all the where the key is the unique field<br> name given to every element and value is the text or value it contains. 
`updated_data=e.formInput;`<br>
`var parameter = e.parameters;`<br>
Every time we hit a function this <b>e object</b> is passed to the function with latest updated data which is further used in every function to recreate the card<br>
And at last every function will update the card<br>
`return CardService.newNavigation().updateCard(card.build());`<br>
Why Add-on is recreated in every function: - because Google Apps Script is a <b>server-side Scripting language and DOM Manipulation</b> is not possible in it, so to add the any<br> element we have to recreate the card again and update the card
<br>

# Steps to publish Add-on

*	Create a version deployment
    *	Go to your project
    *	Click on `publish->deploy from manifest..`
    *	Click on `Create`
    *	Fill details and `click save`
	*   Click on `get ID` and copy the `Deployment ID` (it will be used later)
	*   Click `close`
*	Make a new project on Cloud platform and change your default GCP to Standard Google cloud Platform
    *	Go to `https://console.cloud.google.com`
    *   Create a `new project` 
	*   Go to dashboard and copy the `project number`
	*   Go to your add-on code
	*   Click on `resources->cloud Platform Project`
	*   Paste the `project number` and `click set project`
*	Configure the OAuth consent screen
    *	Open your add-on's Cloud Platform project by going to `https://console.cloud.google.com`
	*   In the console's left navigation, select `APIs & services` to open the `API dashboard`.
	*   In the left nav, select `Credentials` to open the credentials control panel.
	*   In the credential control panel, select the `OAuth consent screen tab.`
	*   Fill in the consent screen form using the corresponding assets (name and logos etc.) you collected. Some of the form elements are optional, but providing them can improve your add-on's user experience.
	*   Click `Save` to record your selections

*	Request review for <b>public</b> add-ons <b>else you may skip this step</b>
    *	[Fill out this review request form](https://goo.gl/forms/gAOLHBTnSq8yKaQ53) using the [assets](https://developers.google.com/gsuite/add-ons/how-tos/publishing-gmail-addons#marketplace_listing_asset_requirements) you assembled. This starts the [add-on review process](https://developers.google.com/gsuite/add-ons/how-tos/publishing-gmail-addons#add-on_review).
    *	Once the review process is complete and you have received the review team's approval, they whitelist your add-on for publication. This allows you to select Public visibility for the add-on when you configure its G Suite Marketplace store listing
    *	[Request OAuth verification for your add-on script project](https://developers.google.com/apps-script/guides/client-verification#requesting_verification). This requires that you show ownership of a domain and that you have a privacy policy hosted within that domain. The verification process can take up to 72 hours to complete. Be sure request verification only after the add-on review process is finished, as otherwise you may be required to repeat the verification procedure
*	Enable the Marketplace SDK
    *	If you have not done so already, open your add-on's Cloud Platform project.
    *	In the console's left navigation, select `APIs & services` to open the API dashboard.
    *	In the API dashboard, select the `Enable APIs and Services` button.
    *	In the Search for APIs & services search bar, type "`G Suite Marketplace SDK`".  Select this API.
    *	In the API listing that opens, click the `Enable` button. After a moment the SDK overview control panel opens
*	configure the Marketplace SDK
    *	The [G Suite Marketplace SDK](https://developers.google.com/gsuite/marketplace/sdk) settings page has four panels: `Overview, Configuration, Publish,` and `Usage`. To define your add-on's listing and start a publication request, you must do the following:
    *	If it isn't open already, [open the Marketplace SDK control panel](https://developers.google.com/gsuite/add-ons/how-tos/manage-gmail-addons#open_the_marketplace_sdk_control_panel). Select the `Configuration` panel. This panel contains a form where you provide information about your add-on
    *	Fill in the configuration form using the corresponding assets you collected. Some of the form elements are optional, but providing them can improve your add-on's user experience. Do the following as you are completing the form:
        *	Where indicated, provide [localized](https://developers.google.com/gsuite/marketplace/sdk#localization) assets for each language you intend to publish the add-on in
        *	Check the `Enable individual install` checkbox if you want to allow [individual installs](https://developers.google.com/gsuite/add-ons/how-tos/publishing-gmail-addons#individual_installs)
        *	Where indicated, include every [scope](https://developers.google.com/gsuite/add-ons/concepts/scopes) listed in your add-on project's [manifest](https://developers.google.com/gsuite/add-ons/concepts/manifests).
        *	In the `Extensions` section, only check the `Gmail add-on extension` checkbox. This causes a text field to appear. In this textbox, enter the deployment ID for the versioned deployment you created
        *	If your are publishing from a domain account, select your add-on's [visibility](https://developers.google.com/gsuite/add-ons/how-tos/publishing-gmail-addons#visibility) where indicated. Selecting My Domain makes your add-on a private add-on. Warning: Once you choose a visibility option and save, you can't change your selection later
    *	Verify that the information you have entered in the form is correct, then click `Save changes`
    *	Select the `Publish` panel, and fill out form there using the corresponding [assets](https://developers.google.com/gsuite/add-ons/how-tos/publishing-gmail-addons#marketplace_listing_asset_requirements) you collected. Some of the form elements are optional, but providing them can improve your add-on's user experience. Do the following as you are completing the form
        *	Where indicated, provide localized assets for each language you intend to publish the add-on in
        *	In the `Reach` section, select an appropriate category for your add-on to help upers locate it in the Marketplace. Also select the regions and countries where you want Marketplace to present your add-on. It's best practice to provide localized assets for each language used in the regions you select
    *	Review the information you have entered into the `Publish` panel. If it is all correct, click `Publish`

## Updating the Add-on

*	Make the changes you want in the add-on's script project.
*	If you made changes that added or removed [scopes](https://developers.google.com/gsuite/add-ons/concepts/scopes) to the script project, you must update the scopes listed to in the [G Suite Marketplace SDK](https://developers.google.com/gsuite/add-ons/how-tos/manage-gmail-addons#update_a_marketplace_listing) select the `Configuration` panel to exactly match the scopes listed in the add-on's project [manifest](https://developers.google.com/gsuite/add-ons/concepts/manifests).
*	If a code update changes the scopes used by the add-on after publication, you must file a new [request for OAuth verification](https://support.google.com/code/contact/oauth_app_verification). Once re-verification is complete, make sure the OAuth scopes listed in the add-on manifest and in the G Suite Marketplace listing match the newly verified scope list. Failing to do so results in an [unverified app](https://developers.google.com/apps-script/guides/client-verification) warning being displayed to your users.
*	Using a [head deployment](https://developers.google.com/apps-script/concepts/deployments#head_deployments), verify that the changes you made are working as intended by testing the add-on. [You can install the new, unpublished version](https://developers.google.com/gsuite/add-ons/how-tos/testing-gmail-addons#install_an_unpublished_add-on) to test it.
*	Once you are certain the updated add-on is functioning correctly, create a new script project [version](https://developers.google.com/apps-script/guides/versions#creating_a_version) to correspond to this update.
    *	Select `File -> Manage Versions..`
    *	Provide a description for the version and then click `Save New Version` to save the current script as a new version
*	In the Apps Script editor, [update the versioned deployment](https://developers.google.com/apps-script/concepts/deployments#editing_a_versioned_deployment) to use the new script project version you just created.
    *	In the script editor, select the `Publish -> Deploy from manifest...` menu item
    *	Find the deployment in the deployment list
    *	Click on the `Edit` link for the deployment
    *	Modify the deployment name, version, or manifest
    *	Click `Save`
*	Once the deployment is saved, the new version replaces the previous one. It may take some time before the change registers for a given user.


## Format of finalPara
`{`<br>
`access_token: ” ”,`<br>
`date:” ”,`<br>
`mobile:[“ ”, “ ”],`<br>
`organisation:” ”,`<br>
`email:“ ”,`<br>
`username:””,`<br>
`order:`<br>
`[`<br>
	`{`<br>
		`pickup:[“ ”, “ ”],`<br>
		`drop:[“ ”,” ”],`<br>
		`vehicle:[“ ”,” ”]`<br>
`}`<br>
			`{`<br>
		`pickup:[“ ”, “ ”],`<br>
		`drop:[“ ”,” ”],`<br>
		`vehicle:[“ ”,” ”]`<br>
`}`<br>

`]`<br>
`}`<br>

## Important Measures:
*	Don’t forget to whitelist the URL, else it will show error:
*	To white list the URL 
*	Go to `appsscript.json`
*	Search for `urlFetchWhitelist`
*	Paste URL here
*	Save file



