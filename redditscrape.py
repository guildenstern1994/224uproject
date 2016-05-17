#redditscrape.py
import praw
r = praw.Reddit(user_agent='224u_dez')
subreddit = r.get_subreddit('worldnews')
f = open('worldnewsdat_scored.txt', 'w')
g = open('worldnewsdat_unscored.txt', 'w')
comments = subreddit.get_comments(limit=None)
n = 0
for c in comments:
	n += 1
	# print c.body
	# print c.score
	# # print c.downvote
	# print c.mod_reports
	# print c.num_reports
	# print c.banned_by
	# print "BEEPBOOPBEEPBOOPBEEPBOOP"
	# if c.score < 0:
	# print c.score
	f.write("ID:"+str(n))
	g.write("ID:"+str(n))
	f.write("\n")
	g.write("\n")
	f.write("RedditScore:"+str(c.score)+"\n")
	f.write(c.body.encode('utf-8')+"\n")
	g.write(c.body.encode('utf-8')+"\n")
	f.write("~~~~~~\n\n")
	g.write("~~~~~~\n\n")
	# if c.mod_reports != []:
	# 	print "mod:"
	# 	print c.mod_reports
	# 	print c.body
	# 	print "~~~~~~~"
	# if c.num_reports != None:
	# 	print "general:"
	# 	print c.num_reports
	# 	print c.body
	# 	print "~~~~~~~~~"
	# if c.banned_by != None:
	# 	print "banned"
	# 	print c.num_reports
	# 	print c.body
	# 	print c.banned_by
	# 	print "~~~~~~~~"
	# break
	# print(c)
f.close
g.close