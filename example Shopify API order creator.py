import requests,json,random, time
from collections import Counter

username = ""
password = ""
products = []
count = 0


def ShopifyAPIrequest(url):

    reqUrl = "https://" + username + ":" + password + "@" + url

    r = requests.get(reqUrl)
    return json.loads(r.text)

def createOrder(url):

    reqUrl = "https://" + username + ":" + password + "@" + url
    params = {
  "order": {
    "email": "foo@example.com",
    "fulfillment_status": "fulfilled",
    "line_items": [
      {
        "variant_id": random.choice(products),
        "quantity": random.randint(1,20)
      }
    ]
  }
}

    r = requests.post(reqUrl,json = params)
    return json.loads(r.text)


for product in ShopifyAPIrequest('testystore.myshopify.com/admin/variants.json?fields=id')['variants']:
    products.append(product['id'])
    print product['id']

while True:
    createOrder('testymcteststoreface.myshopify.com/admin/orders.json')
    print "order ", count ," created"
    count += 1
    time.sleep(0.55)
