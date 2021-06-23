import praw
import config
import time
count = 0
list_gpus = []
list_data = []

filename = "current.txt"
f = open(filename, "r")

def load_data():
    num_gpu = f.readline()
    print(str(num_gpu))

    for x in range(int(num_gpu) - 1):
        gpu = f.readline()
        list_gpus.append(gpu.replace("\n",""))
        avg = f.readline()
        list_data.append(avg.replace("\n",""))
        low = f.readline()
        list_data.append(low.replace("\n",""))
        high = f.readline()
        list_data.append(high.replace("\n",""))



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
        if("!GPU") in comment.body:
            print("Found Comment")
            comment.reply(str(string))
 
            


r = bot_login()
load_data()

f.close()
run_bot(r)