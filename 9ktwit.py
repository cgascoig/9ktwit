import os
import sys
import json

#Vendorised packages
sys.path.append('./requests')
sys.path.append('./python-twitter')
sys.path.append('./requests-oauthlib')
sys.path.append('./oauthlib')
sys.path.append('/bootflash/scripts/9ktwit/requests')
sys.path.append('/bootflash/scripts/9ktwit/python-twitter')
sys.path.append('/bootflash/scripts/9ktwit/requests-oauthlib')
sys.path.append('/bootflash/scripts/9ktwit/oauthlib')


import twitter

try:
    with open('9ktwitconfig.json','r') as f:
        config=json.load(f)
except:
    with open('/bootflash/9ktwitconfig.json','r') as f:
        config=json.load(f)

try:
    os.environ['HTTP_PROXY']=config['proxy']
    os.environ['HTTPS_PROXY']=config['proxy']
except:
    pass

api=twitter.Api(consumer_key=config['consumer_key'],
                consumer_secret=config['consumer_secret'],
                access_token_key=config['access_token_key'], 
                access_token_secret=config['access_token_secret'])
                
print api.VerifyCredentials()

tweetmap = {
    "configured": "Someone just configured me. I hope they were gentle. "
}

try:
    if sys.argv[1]=="tweet":
        tweet=tweetmap[sys.argv[2]]
        api.PostUpdate(tweet)
except Exception as e:
    print e
    print """
Usage:
9ktwit.py tweet <status text>
    """

# status = api.PostUpdate('I can tweet!')
# print status.text