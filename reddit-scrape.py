import praw

reddit = praw.Reddit(client_id='', client_secret='', user_agent='')

submission = reddit.submission(url="https://www.reddit.com/r/uofm/comments/nsiuxj/law_library/") #example

submission.comments.replace_more(limit=0)
textfile = open("reddit-comments.txt", "w")
for comment in submission.comments.list():
    textfile.write(str(comment.body) + '\n')
    # print(comment.body)
textfile.close()