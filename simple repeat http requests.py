import requests

def doRequest():
    responses = []
    for i in range(0,300):

        url = 'https://google.com'
        headers = {'User-Agent': 'python'}

        response = requests.get(url, headers=headers)

        print "request: " , i

doRequest()
