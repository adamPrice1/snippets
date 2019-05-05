# github API graphQL call

import json
import requests
import re
from ratelimit import limits, sleep_and_retry

token = "" #TOKEN HERER
URL = "https://api.github.com/graphql"
comments = ""
# api-endpoint
@sleep_and_retry
@limits(calls=4500, period=3600)
def getIssues(endCursor):
    global URL

    cursor = ""
    if endCursor != "":
        cursor = """after: "%s" """ % (endCursor)     #Insert Repo Owner/name
    query = """

    {
     repository(owner:"",name:""){
      issues(states:CLOSED, first:50, %s){
        pageInfo {
          endCursor
          startCursor
        }
        	nodes{
            url
            number
            bodyText
            comments(first: 20){
              pageInfo {
                endCursor
                startCursor
              }
              nodes{
                bodyText
              }
            }
          }
    		}
    	}
        rateLimit {
            limit
            cost
            remaining
            resetAt
            }
    }

    """ % (cursor)
    data =""

    r = requests.post(url = URL, json={'query': query}, headers={
    "Authorization":"bearer "+token
    },timeout=20)
    data = r.json()
