import praw
import config
import time
import os
count = 0
list_gpus = []
list_data = []
list_responded =[]


def load_comment():
    file_2 = "repliedto.txt"
    f2 = open(file_2, "w")
    if not os.path.isfile(file_2):
        list_responded = []

    with open("repliedto.txt", "r") as f2:
        list_responded = f2.read()
        list_responded = list_responded.split("\n")
    f2.close()


def load_data():
    filename = "current.txt"
    f = open(filename, "r")
    num_gpu = f.readline()

    for x in range(int(num_gpu) - 1):
        gpu = f.readline()
        list_gpus.append(gpu.replace("\n",""))
        avg = f.readline()
        list_data.append(avg.replace("\n",""))
        low = f.readline()
        list_data.append(low.replace("\n",""))
        high = f.readline()
        list_data.append(high.replace("\n",""))
    f.close()



def form_string():
    string = "Thanks for using BuddyBot!\n\n"
    length = len(list_gpus)
    for x in range(length -1):
        list_iter = x * 3
        string += "GPU Series: " + list_gpus[x] + "\n\nAverage Price: $" + list_data[list_iter] +  " Ranging from: $" + list_data[list_iter + 1] + " - $" + list_data[list_iter + 2] + "\n\n"
    return string





def bot_login():
   r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "BuddyBot test")
   return r

def run_bot(r):
    print('Searching for "!GPU" ')
    string = form_string()
    for comment in r.subreddit('test').comments(limit= 40):
        if("!GPU") in comment.body and comment.id not in list_responded and comment.author != r.user.me():
            print("Found Comment")
            comment.reply(str(string))
            list_responded.append(comment.id)
            with open("repliedto.txt", "a") as f2:
                f2.write(comment.id + "\n")
 
            

#login
r = bot_login()
#Load previous comments
load_comment()

while True:
    load_data()
    run_bot(r)
    time.sleep(30)