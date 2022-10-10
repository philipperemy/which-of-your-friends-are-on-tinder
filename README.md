# Which of your friends are on Tinder?

*Discover which of your friends are on Tinder. Don't forget to star or fork this repo if you appreciate the repo!*

<center>
<img src="coollogo_com-19375962.png"></img>
</center>

## Disclaimer
Please keep in mind that whenever someone creates a profile on Tinder, it will appear in this list forever. Even though this person no longer uses it. Use it just for fun experiments! Not for something too serious. Thanks!

The Tinder API is available here:
- https://gist.github.com/rtt/10403467

## Output of the program
```
Which of your friends are on Tinder?
----------
FB_ID = steve.jobs
FB_AUTH_TOKEN = EAAGm0PX4ZCpsBAG4Wme[truncated in this example]4ZD
TINDER_TOKEN = 4a0df5c2-3232-4365-fake-178a0fe9e1c9
----------
Successfully connected to Tinder servers.
--------------------------------------------------------------------------------
     First Name        Last Name           Gender              URL
           Mark       Zuckerberg             male  https://www.facebook.com/4
          Chris           Hughes             male  https://www.facebook.com/5
         Dustin        Moskovitz             male  https://www.facebook.com/6
           Arie            Hasit             male  https://www.facebook.com/7
         Marcel         Laverdet             male  https://www.facebook.com/10
          Chris           Putnam             male  https://www.facebook.com/13
 ```

## How does it work?
The methodology is explained here: https://www.quora.com/Do-my-Facebook-friends-know-I-am-on-Tinder/answer/Philippe-Remy-1?srid=BN2L

- The program uses the Tinder and Facebook Graph APIs.
- First we connect to Facebook servers by providing `FB_EMAIL_ADDRESS` and `FB_PASSWORD`. 
- We get a facebook token back. 
- From there, we request Tinder with this token and the `FB_ID`, in order to get a Tinder auth token. 
- When it's completed, we ask Tinder about our profile. We retrieve a list of friends IDs.
- For each friend ID, we demystify it with the Graph API to get the first name and last name of the friend.

## How to run the app
```
# If you don't use python3, use python and pip instead of python3 and pip3.
git clone https://github.com/philipperemy/which-of-your-friends-are-on-tinder.git
cd which-of-your-friends-are-on-tinder
sudo pip3 install -r requirements.txt # or use --user with virtualenv if you cannot use sudo.
mv credentials.json.example credentials.json
vim credentials.json # edit and fill the variables (explained in the next section: Configuration)
python3 main.py
```

If the configuration file is correct, you will see: `Successfully connected to Tinder servers.` and the list of your Facebook friends on Tinder.

## Configuration of credentials.json

- `FB_ID` : The id of your facebook. Your profile is available at https://www.facebook.com/FB_ID where FB_ID is your id.
- `FB_EMAIL_ADDRESS` : Your Facebook email address.
- `FB_PASSWORD` : Your Facebook password.

## Support

You can either open an `Issue` or send me a e-mail to premy.enseirb@gmail.com. Any contributions are welcomed!
