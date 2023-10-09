- Voice assistant capable of automating 12 tasks from searching Wikipedia and YouTube videos to sending emails, writing notes, and setting alarms. 

- For searching Wikipedia and YouTube, the app uses selenium. You have to download the Google Chrome browser and the accurate Chrome driver version (chromedriver.exe should be in the same folder as the app.py script). Versions must be the same. Check your Google Chrome version and for example, if your version is 114.0.5735.199 you should download Chrome driver version 114.0.5735. Install the exact version of selenium from the requirements.txt file. At the time you use this code, your Chrome version can be updated to a newer version from now so check it first.

- For sending email applications use sendgrid. Go to their page https://sendgrid.com/solutions/email-api/ sign in and get your API keys that you can use. After the voice assistant gets commands for sending emails it will prompt you with the email of the recipient. Enter the email and after that give voice commands for the Subject and Email content.

- For checking current time and weather the app is using openweathermap. Go to their page https://openweathermap.org/api sign in and get your API keys that you can use. 

- For checking daily top 3 hottest news go to https://newsapi.org and get your api keys.

- Create api.py in the same folder as your main app.py script and write 3 API key variables that are API keys that you got from previously mentioned sites or use other sites that you prefer. Also as a fourth variable add your email so it will be imported in the email.py script and used in SendGrid. 

**news_key = "********************************"**
**weather_key = "**********************************"**
**sendgrid_key = "*********************************"****
**sender_email = "*********************************"**

Enjoy!
