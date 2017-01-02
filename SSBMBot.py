#Authored by TheArcticKitten/Noah O.
import praw
import time
reddit = praw.Reddit('bot1', user_agent='bot1 user agent')
print(reddit.user.me())
subreddit = reddit.subreddit("SSBM")
f = open("commented.txt", "r+")
counter = 0
while(True):
	for submission in subreddit.hot(limit=300):
		submission.comments.replace_more(limit=0)
		for comment in submission.comments.list():
			if comment.id not in open('commented.txt').read():
				comment.body = comment.body.lower()
				if ("!doraki" in comment.body) or ("!doraky" in comment.body):
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Doraki Instant Wall Jump**"
					"\n\nWalljumping is performed by touching a wall, and then tapping away from it. However, it is also possible to wall jump directly from the ledge."
					"\n\nThis technique is called the Ledge Walljump (or Doraki) and is performed as such."
					"\n\n1. Grab the ledge"
					"\n\n2. Drop from the ledge"
					"\n\n3. Double jump back to the ledge, making sure that you rub up against the wall as you do so."
					"\n\n4. While hanging from the ledge, tap away."
					"\n\n(Credits to /u/ djloreddit)"
					"\n\n[GIF](http://i.imgur.com/QxxmkgL.gif)"
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=Ut-D3c4HfIg)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					#already_commented.append(comment)
					open('commented.txt', 'a').write(comment.id + "\n")
				if ("!wavedash" in comment.body) or ("!wavedashing" in comment.body):
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Wavedash**"
					"\n\nA Wavedash is a technique that is performed by air dodging diagonally into the ground, causing the character to slide a short distance. It allows players to perform any ground action while moving horizontally on the ground."
					"\n\n[GIF](http://www.ssbwiki.com/images/c/c6/Wavedashbig.gif)"
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=_EcPgWGiEhk)"
					"\n\n[Wiki](http://www.ssbwiki.com/wavedash)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if "!waveshine" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Waveshine**"
					"\n\nA wavedash can be performed anytime a character is on the ground and can jump. The shine can be canceled by jumping shortly after it is initiated. Therefore, it is possible for Fox and Falco to jump out of a shine into a wavedash."
					"\n\nThis advanced technique is known as a waveshine and can be performed as such"
					"\n\n1. Shine"
					"\n\n2. Jump"
					"\n\n3. Airdodge into the stage"
					"\n\n[GIF](http://www.ssbwiki.com/File:Fox_Waveshine.gif)"
					"\n\n[Video Tutorial](https://www.youtube.com/watch?v=RnGe7Xur1L8)"
					"\n\n[Wiki](http://www.ssbwiki.com/Waveshine)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if ("!jcgrab" in comment.body) or ("!jumpcancelgrab" in comment.body):
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Jump-Canceled Grab**"
					"\n\nA jump-canceled grab is a technique where a character interrupts a dash or run with a jump, which itself is then jump-canceled with a grab during the jumpsquat animation. This results in the character using their standing grab while maintaining some momentum from their dash, the amount of which is based on their current speed and traction."
					"\n\n[GIF](https://www.ssbwiki.com/images/9/93/Jump-canceled_Grab_Mario_Melee.gif)"
					"\n\n[Video Tutorial](https://www.youtube.com/watch?v=ffUQu-lYanE)"
					"\n\n[Wiki](https://www.ssbwiki.com/Jump-canceled_grab)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if ("!lcancel" in comment.body) or ("!lcanceling" in comment.body):
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**L-canceling**"
					"\n\nL-canceling (an abbreviation of lag canceling or  is a technique that allows characters to act faster than usual when landing in the middle of an aerial attack."
					"\n\nTo perform an L-cancel, a shield button (L, R, or Z) needs to be pressed 7 frames before landing during an aerial attack"
					"\n\n[GIF](https://www.ssbwiki.com/images/9/94/Lcancelink.gif)"
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=WNuYq7_nwzY)"
					"\n\n[Wiki](https://www.ssbwiki.com/L-canceling)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if ("!dashdancing" in comment.body) or ("!dashdance" in comment.body):
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Dash-Dancing**"
					"\n\nDash-dancing is one of the most used techniques in Melee. While being one of the easiest to perform, it's one of the hardest to master. Dash-dancing is used to play spacing mindgames with the opponent, and to make openings that can punished."
					"\n\nPerformed by rapidly tapping the analog stick left and right while on the ground, it cancels out the character's initial dashing animation with another animation in the opposite direction, causing the character to quickly and repeatedly dash to the right and left in a short distance."
					"\n\n[GIF](http://www.ssbwiki.com/images/b/ba/Dashdance.gif)"
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=vG3hIEI-oAk)"
					"\n\n[Wiki](http://www.ssbwiki.com/Dash-dance)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if ("!di" in comment.body) or ("!directionalinfluence" in comment.body):
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Directional Influence**"
					"\n\nDirectional influence, abbreviated DI, is the control the receiver of an attack has over his or her trajectory. DI can be used to alter, but not completely change, the original trajectory the player was sent at by an attack."
					"\n\nThis change can be vital to surviving high-power attacks such as Fox's up smash, and for escaping combos such as Jigglypuff's up-throw to rest combo on fast-fallers."
					"\n\n[GIF](http://www.ssbwiki.com/images/7/71/DI-Melee.gif)"
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=XdTLRNTABpw)"
					"\n\n[Wiki](http://www.ssbwiki.com/Directional_influence)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if "!neutralgame" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Neutral Game**"
					"\n\nThe neutral game, or just neutral, is a phase during gameplay when no player has a situational advantage over the other. In this phase, either player's objective is to \"win the neutral game\", i.e. land a hit with possible follow-ups, or punish the enemy for a failed attempt to do so."
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=MCPC202uwR4)"
					"\n\n[Wiki](http://www.ssbwiki.com/Neutral_game)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if "!scarjump" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Scar Jump**"
					"\n\nThe Scar Jump is a variant of the Wall Jump in which a character wall jumps *without* using their midair jump from the ledge or stage."
					"\n\n[GIF](https://www.ssbwiki.com/images/8/84/Scar_Jump.gif)"
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=-C1sTQdVSRA)"
					"\n\n[Wiki](https://www.ssbwiki.com/Scar_Jump)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if ("!sdi" in comment.body) or ("!smashdi" in comment.body):
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Smash DI**"
					"\n\nSmash directional influence is a mechanic that allows players to slightly alter their position during the freeze frames of being hit by an attack. Tapping the control stick in any direction during freeze frames will slightly move their character in that direction, allowing them to potentially escape multi-hit moves or certain combos"
					"\n\n[GIF](http://www.ssbwiki.com/images/9/99/SDI_Snake_Brawl.gif)"
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=CO7YD9KqNhY)"
					"\n\n[Wiki](http://www.ssbwiki.com/Smash_directional_influence)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
				if ("!cc" in comment.body) or ("!crouchcanceling" in comment.body) or ("!ccing" in comment.body):
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Crouch Canceling**"
					"\n\nA crouch cancel (or CC) is a technique in the Super Smash Bros. series used to reduce the effect of an attack on the user. By crouching before getting hit by an attack, some aspect of the attack will be weakened."
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=72aidPrzScA)"
					"\n\n[Wiki](https://www.ssbwiki.com/Crouch_cancel)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if "!moonwalk" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Moonwalking**"
					"\n\nIn Super Smash Bros. Melee, the moonwalk is a technique that involves sliding backwards during in the initial dash animation"
					"\n\nMoonwalking is achieved by tilting the control stick backwards while dashing, but without passing through the neutral position. The only easy way to do this is to rotate the stick below the neutral position (as going above results in a jump), but just barely below as to prevent losing some distance from crouching."
					"\n\n[GIF]https://www.ssbwiki.com/images/b/b1/Moonwalking_Melee.gif)"
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=D_xDJM3jOYg)"
					"\n\n[Wiki](https://www.ssbwiki.com/Moonwalk)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if "!shinostall" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Shino Stalling**"
					"\n\nThe Shino stall grants the user total invincibility. This technique takes advantage of the invincibility caused by grabbing a ledge along with the invincibility caused by Sheik's Vanish move."
					"\n\n1. Grab a ledge"
					"\n\n2. Press away from the stage to let go"
					"\n\n3. The moment you are in the air, input up-b and then hold down "
					"\n\n4. Continue holding down until the pink explosion, at which point press nothing" 
					"\n\n5. You will then grab the ledge, and 7 frames later you can let go and repeat."
					"\n\n(Credits to /u/ djloreddit)"
					"\n\n[GIF](http://imgur.com/iabwbxq)"
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=K3DI4Zl6b1E)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if "!shielddrop" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Shield Dropping**"
					"\n\nShield platform dropping is an advanced technique in all four Super Smash Bros. games. It involves dropping through a soft platform while shielding by tilting the analog stick down."
					"\n\n[GIF](http://www.ssbwiki.com/images/5/58/Brawl-ShieldPlatformDrop.gif)"
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=_IQFgGm49aI)"
					"\n\n[Wiki](http://www.ssbwiki.com/Shield_platform_dropping)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if "!marthkiller" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Marth Killer**"
					"\n\nThe Marth Killer is a technique in Super Smash Bros. Melee that can be used to edge-hog a recovering Marth."
					"\n\nIt involves using the light shield on the edge of the stage, facing towards the center, and is most easily performed by rolling towards the ledge, holding Z, and pointing the shield downwards."
					"\n\n[GIF](http://imgur.com/6WrHuTl)"
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=XmlM3qkdva4)"
					"\n\n[Wiki](http://supersmashbros.wikia.com/wiki/Marth_Killer)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if ("!tech" in comment.body) or ("!teching" in comment.body):
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Teching**"
					"\n\nTeching allows the player to get back up after hitting a surface (such as a wall or floor) instead of lying on the ground until using a get-up action. This technique is great for survival as it can be used to survive combos, or walljump off the stage (wall-teching)"
					"\n\nTo perform, the player must press the shield button 20 frames before hitting the surface, but if pressed too early, the player can't tech again for another 40 frames."
					"\n\n[GIF](https://www.ssbwiki.com/images/8/8b/SSB4_Mega_Man_Tech.gif)"
					"\n\n[Video Tutorial](https://www.youtube.com/watch?v=P-ASMMMdiO4)"
					"\n\n[Wiki](https://www.ssbwiki.com/Tech)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if "!ecawk" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Edge-canceled Aerial Wizard Kicks**"
					"\n\nAn EcAWK is a technique in Project M for Ganondorf which allows for comboing, edgeguarding, and most importantly **STYLEEE**"
					"\n\nTo perform an EcAWK, aerial wizard kick onto a ledge and, if you're close enough, you'll slide off the ledge and cancel all the lag you would have experienced from landing on the ground."
					"\n\n[Source](https://smashboards.com/threads/ganon-strategies-and-gameplay-discussion.347166/page-6#post-16997998)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if "!haxdash" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Haxdash**"
					"\n\nA haxdash is a waveland done from the ledge, to the ledge again. It is often used to mix up opponents or bait them. It is mostly performed with Captain Falcon but can also be done by Marth, Fox, and Falco on specific stages"
					"\n\n[GIF](http://www.ssbwiki.com/images/c/cd/CF_Ledgedashstall_no_ff_17ms_with_input_display.gif)"
					"\n\n[Video Tutorial](https://www.youtube.com/watch?v=lxg05IN9ncw)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
				if "!multishine" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Multishine**"
					"\n\nA multishine is a technique which involves shining (Fox and Falco's down-b) multiple times. This moves is often used for shield pressure but is an extremely difficult technique to pull of consistently."
					"\n\nA multishine is performed by jump-cancelling a shine and using another shine right after leaving the ground. If timed correctly this can be chained into multiple shines very quickly."
					"\n\n[GIF](https://www.ssbwiki.com/images/d/d6/MultiShine.gif)"
					"\n\n[Video Tutorial](https://www.youtube.com/watch?v=EAMoJ8ZpvjE)"
					"\n\n[Wiki](https://www.ssbwiki.com/Double_shine)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
				if "!thunderscombo" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Thunder's Combo**"
					"\n\nAt it's core, Thunder's combo consists of wavedashing out of the Shine in order to Jab Reset the opponent. However, more attacks (such as drill or falling uair) can be added to the beginning and end of this combo to make it truly devastating."
					"\n\nThis combo only works on characters who fall to the ground after being Shined(Falco, Fox, Kirby, YL, Pichu, Pikachu, Jigglypuff, Mewtwo, GW, and Roy). For it to work on the rest of the cast a waveshine must be performed."
					"\n\n(Credits to /u/ djloreddit)"
					"\n\n[GIF](http://imgur.com/fl9Uov4)"
					"\n\n[Source](https://smashboards.com/threads/thunders-combo-udated-again-9-27-06.81139/)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
				if "!pcdrop" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**PC Drop**"
					"\n\nA PC drop is a ledge-grab mixup technique not often used but extremely useful. It is performed by fast walking to the ledge and turning around right before approaching the ledge. Every character in the cast can do this"
					"\n\n[Video tutorial](https://www.youtube.com/watch?v=yw9pfO9UORU)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
				if "!samistall" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Samistall**"
					"\n\nA samistall is a stalling method that shiek can use at the ledge in which she is completely invicible."
					"\n\nSamistalling is performed by letting go of ledge and using up-b back to it at an angle to regrab it."
					"\n\n[GIF](https://gfycat.com/ThisEachBellfrog)"
					"\n\n[SSBM Tutorials Video](https://www.youtube.com/watch?v=01GZwcJfI_o)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
				if "!gentleman" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Gentleman**"
					"\n\nThe Gentleman is a nickname that refers to the third hit of Captain Falcon's standing neutral attack combo, when it is not followed by rapid punches. It inflicts a great deal of knockback."
					"\n\nThere are several methods to perform the Gentleman. The player can perform the third neutral attack input by pressing any button in conjunction with the neutral attack. S2J discovered that one can hold down on the control stick after the initial jab and continue the rest of the combo to do the Gentleman."
					"\n\n[GIF](https://i.imgur.com/ZLvhNj5.jpg)"
					"\n\n[Video Tutorial](https://www.youtube.com/watch?v=atcUA-lH4Bs)"
					"\n\n[Wiki](http://www.ssbwiki.com/Gentleman)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
				if "!jabreset" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply(
					"**Jab Reset**"
					"\n\nA jab reset is a technique in that is performed by jabbing an opponent while they are knocked down.It results with the opponent being forced to get up automatically. The player can then follow up with any move they desire, which is usually utilised to land a KO Move."
					"\n\nIt should be noted that this can also be performed with weak moves such as Fox's drill."
					"\n\n[GIF](http://www.ssbwiki.com/images/0/09/Jabreset.gif)"
					"\n\n[Video Tutorial](https://www.youtube.com/watch?v=cy2q1Q_vg8w)"
					"\n\n[Wiki](http://www.ssbwiki.com/jab_reset)"
					"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					open('commented.txt', 'a').write(comment.id + "\n")
				if "!dustscooting" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply("!wavedash")
					open('commented.txt', 'a').write(comment.id + "\n")
				if "!funcanceling" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply("!lcanceling")
					open('commented.txt', 'a').write(comment.id + "\n")
				if "!20xx" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply("The year is **20XX**. Everyone plays Fox at TAS levels of perfection. Because of this, the winner of a match depends solely on port priority. The RPS metagame has evolved to ridiculous levels due to it being the only remaining factor to decide matches.")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if "!jigglypuff" in comment.body:
					print("Replied to comment ID:" + comment.id)
					comment.reply("[Hey there](https://www.youtube.com/watch?v=wHn3FL9Drps)")
					open('commented.txt', 'a').write(comment.id + "\n")
					#already_commented.append(comment)
				if ("!ics" in comment.body) or ("!sad2king" in comment.body):
					print("Replied to comment ID:" + comment.id)
					comment.reply("[:c](https://youtu.be/1v2Nz9-iJ6g?t=71)")
					open('commented.txt', 'a').write(comment.id + "\n")
	time.sleep(45)
					#already_commented.append(comment)
				#if "" in comment.body:
					#print("Replied to comment ID:" + comment.id)
					#comment.reply(
					#"****"
					#"\n\n"
					#"\n\n[GIF]()"
					#"\n\n[SSBM Tutorials Video]()"
					#"\n\n[Wiki]()"
					#"\n\n[Github for bot](https://github.com/TheArcticKitten/SSBMBot)"
					#"\n\nAny problems or want to provide higher quality GIFs, summaries, or tutorials? Message /u/ thearctickitten on reddit!")
					#open('commented.txt', 'a').write(comment.id + "\n")