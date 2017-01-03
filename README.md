# SSBMBot
A Reddit bot for /r/SSBM and /r/Smashbros to help the community out with learning different techniques from the very advanced game Super Smash Brothers Melee.
This bot was created as a little fun side project so I could learn some Python.

It's purpose is to respond to comments with queries such as "!doraki" in which the bot responds to with a full description on the
"doraki instant wall-jump" technique, inlcuding how to perform the technique, a GIF of it being performed, a video tutorial of it, and the wiki page for it.

I made this using the PRAW API for python, a JSON file to store all queries and responses (didn't do in initial commit), and a text file storing all the IDs of the comments it has replied to prevent replying to a single comment multiple times.
