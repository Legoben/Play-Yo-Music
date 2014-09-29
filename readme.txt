Sonos Yo

Will move over to GitHub once everything is done.

Requires python libraries:
    Tornado
    SoCo (From git repo, not pypi)

Required other:
    https://ngrok.com/
   
 
1. Start Ngrok
2. Config Yo API to go to subdomain.ngrok.com/YO-USERNAME
3. Add usernames to conf.json (Don't worry about IDs)
4. Run config.py
5. Run main.py
6. Yo

Currently being weird:
    Controller metadata when playing tracks from music services (confirmed bug in SoCo library).