# discordbot

Kartbot is a simple discord bot implementation with python (django) using discord.py API and Cloud MongoDB for storage purposes.

Steps to be followed for deployment :

1. Create ".env" file in the same directory as "bot.py" which contains following variables:
-DISCORD_TOKEN : This token can be found in developer section of your Bot Application on the Discord Dashboard.
-DB_USER : This is MongoDB Username
-DB_PASSWORD : This is your MongoDB password (To save alphanumeric passwords don't forget to URL encode it ; like this : urllib.parse.quote("your_password")
-DB_NAME : Your MongoDB Databse Name
-CLUSTER_NAME : Your MongoDB Cluster name.
-SE_ID : Your Custom programmable Search Engine ID (it can be found from cloud instance)
-G_API_KEY : Your Google API Key

Note: Above Env variables are specific for Chatbot implementation with Cloud MongoDB Database & Google Cloud. 
Variables can be different according to the deployment of different databases and servers.

2. Go to requirements.txt direcoty and Run following command to install requiremments (preferably in a vitualenv). 
$ pip install -r requirements.txt  

3. To Run project on dev mode locally run command:
$ python manage.py runserver

4. One can use any WSGI server or DJango WSGI to deploy it on any server( Like Heroku, AWS, GCP etc.)

5. Once the Kartbot App is up and running go to your guild where you want to integrate this bot, use the specific Disscord App Token and you are good to go :P




