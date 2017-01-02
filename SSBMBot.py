#Authored by TheArcticKitten/Noah O.
import praw
from time import sleep
import json
import re
reddit = praw.Reddit('bot1', user_agent='bot1 user agent') #logs in to bot account from praw.ini
subreddit = reddit.subreddit("Kitten_bots")
replies = 0 #counter just to keep track of the replies

print(reddit.user.me()) #just confirming that it logs in correctly under the right user

with open("info.json") as f: #load in JSON file with all queries and responses
    info = json.load(f)

while True: #main loop to find command comments
	for submission in subreddit.hot(limit=300): #loop through first 300 submissions in subreddit
		submission.comments.replace_more(limit=0)
		for comment in submission.comments.list(): #loop through all comments in each submission
			if comment.id not in open('commented.txt').read(): #check if it has been replied to already by the bot
				for item in info: #loop thorugh all queries
					if re.search("!{0}".format(item), comment.body, flags=re.IGNORECASE): #check if any of the queries are in the comment body
						comment.reply("**{0}**\n\n{1}\n\n{2}\n\n{3}".format( #reply the correct response for that specific query
		                        info[item]['Name'],
		                        "\n\n".join(info[item]['Description']),
		                        "\n\n".join("[{0}]({1})".format(link, info[item]['Links'][link])
		                        for link in info[item]['Links']),
		                        "------\n[^SSBMBot](https://github.com/thearctickitten/SSBMBot) ^by ^[TheArcticKitten](/u/ thearctickitten)"
		                    		))
						open("commented.txt", "a+").write(comment.id + "\n") #append the comment id to the already commented txt file to prevent commenting on it again
						replies += 1 #increment counter
						print("Replied to comment ID: {0} Count: {1}".format(comment.id, replies)) #print out the id just as a log
	time.sleep(30) #sleep for 30 seconds