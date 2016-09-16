import requests
import json

def create_posts():
    link = "http://localhost:3000/posts"
    posts = [{
        "title":"Google",
        "link":"http://www.google.com"
    },
    { "title":"Reddit",
      "link":"http://www.reddit.com"}
    ]
    for post in posts:
        r = requests.post(link, json=post)

create_posts()
print "Seeded"
