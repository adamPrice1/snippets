import requests

def doRequest():
    responses = []
    for i in range(0,300):

        url = 'https://testymcteststoreface.myshopify.com/'
        headers = {'User-Agent': 'TMS-Gauntlet-Bot'}

        response = requests.get(url, headers=headers)

        print "request: " , i

doRequest()
