# health-checker
A simple health checker app for websites

# How it works?
It works by getting the urls you put in the json file and checking the status code for them.
Then, by your telegram bot code, you can get the output in your mobile device.

# How to run it ?
You have to set your enviroment variables by creaitng a new file named **.env** and correctly match your Bot token and Chat Id.

 ### How to obtain your Bot token ?
 1. Open telegram on your mobile device
 2. Contact @BotFather by using the **/newbot** command 
 3. @BotFather will ask you for your name, username and will give you your token  

## Url setup
You have the download **domains.json** file. After opening, you will see an example url. Change that with the url you want to check. Dont forget that you can do more than one url.

## Instalation
After opening your studio, you have to write these into your **Terminal**.
- `pip install -r requirements.txt `

## Start
Run the code by writing `python main.py`



