#Authored by TheArcticKitten/Noah O.
import praw
import time
import json
import re
reddit = praw.Reddit('bot1', user_agent='bot1 user agent')
subreddit = reddit.subreddit("Kitten_bots")
replies = 0
 
print(reddit.user.me())

with open("info.json") as f:
    info = json.load(f)

while True:
	for submission in subreddit.hot(limit=300):
		submission.comments.replace_more(limit=0)
		for comment in submission.comments.list():
			if comment.id not in open('commented.txt').read():
				for item in info:
					if re.search("!{0}".format(item), comment.body, flags=re.IGNORECASE):
						comment.reply("**{0}**\n\n{1}\n\n{2}\n\n{3}".format(
		                        info[item]['Name'],
		                        "\n\n".join(info[item]['Description']),
		                        "\n\n".join("[{0}]({1})".format(link, info[item]['Links'][link])
		                        for link in info[item]['Links']),
		                        "------\n[^SSBMBot](https://github.com/thearctickitten/SSBMBot) ^by ^[TheArcticKitten](/u/thearctickitten)"
		                    		))
						open("commented.txt", "a+").write(comment.id + "\n")
						replies += 1
						print("Replied to comment ID: {0} Count: {1}".format(comment.id, replies))