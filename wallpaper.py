# !/usr/bin/python3
from tkinter import *
# from tkinter import messagebox
import ctypes
import requests
import shutil
import webbrowser
import praw
import re
from urllib.parse import urlparse

list = []

# A function that sets the wallpaper of the current system.
def changeBg(PATH):
    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, PATH, 3)

# A function used to make a request to download the image and save it.
def doRequest(URL):
    r = requests.get(URL, stream=True)
    filename = urlparse(URL)
    fn = str(filename.path).split('/')
    if (fn != None):
        path = "C:\\Users\\iamto\\Pictures\\Wallpaper\\" + fn[1]
        end = str(fn[1]).split('.')[1]
    if (end == "jpg"):
        file = open(path, "wb")
        file.write(r.content)
        file.close()

# A function to crawl reddit for the top 20 wallpapers from each of the listed subreddits.
def crawl():
    reddit = praw.Reddit(client_id='7-4B300Ip7f-iw',
                         client_secret='rR8THfrDUqKQ8qval9YycTLaQkw',
                         user_agent='crawlbot')

    for submission in reddit.subreddit('wallpaper').hot(limit=20):
        list.append(submission.url)

    for submission in reddit.subreddit('wallpapers').hot(limit=20):
        list.append(submission.url)

    for submission in reddit.subreddit('wallpaperdump').hot(limit=20):
        list.append(submission.url)

    for submission in reddit.subreddit('WQHD_Wallpaper').hot(limit=20):
        list.append(submission.url)

    return list

def siteDetails(list):
    for url in list:
        doRequest(url)


# A function to recreate the top wallpaper list as a website.
def site(list):
    f = open('page.html', 'wb')

    message = """<center>
        <a href=""" + list[0] + """><img height=200px width=400px src=""" + list[0] + """></a>
        <a href=""" + list[1] + """><img height=200px width=400px src=""" + list[1] + """></a>
        <a href=""" + list[2] + """><img height=200px width=400px src=""" + list[2] + """></a>
        <a href=""" + list[3] + """><img height=200px width=400px src=""" + list[3] + """></a>
        <a href=""" + list[4] + """><img height=200px width=400px src=""" + list[4] + """></a>
        <a href=""" + list[5] + """><img height=200px width=400px src=""" + list[5] + """></a>
        <a href=""" + list[6] + """><img height=200px width=400px src=""" + list[6] + """></a>
        <a href=""" + list[7] + """><img height=200px width=400px src=""" + list[7] + """></a>
        <a href=""" + list[8] + """><img height=200px width=400px src=""" + list[8] + """></a>
        <a href=""" + list[9] + """><img height=200px width=400px src=""" + list[9] + """></a>
        <a href=""" + list[10] + """><img height=200px width=400px src=""" + list[10] + """></a>
        <a href=""" + list[11] + """><img height=200px width=400px src=""" + list[11] + """></a>
        <a href=""" + list[12] + """><img height=200px width=400px src=""" + list[12] + """></a>
        <a href=""" + list[13] + """><img height=200px width=400px src=""" + list[13] + """></a>
        <a href=""" + list[14] + """><img height=200px width=400px src=""" + list[14] + """></a>
        <a href=""" + list[15] + """><img height=200px width=400px src=""" + list[15] + """></a>
        <a href=""" + list[16] + """><img height=200px width=400px src=""" + list[16] + """></a>
        <a href=""" + list[17] + """><img height=200px width=400px src=""" + list[17] + """></a>
        <a href=""" + list[18] + """><img height=200px width=400px src=""" + list[18] + """></a>
        <a href=""" + list[19] + """><img height=200px width=400px src=""" + list[19] + """></a>
        <a href=""" + list[20] + """><img height=200px width=400px src=""" + list[20] + """></a>
        <a href=""" + list[21] + """><img height=200px width=400px src=""" + list[21] + """></a>
        <a href=""" + list[22] + """><img height=200px width=400px src=""" + list[22] + """></a>
        <a href=""" + list[23] + """><img height=200px width=400px src=""" + list[23] + """></a>
        """

    f.write(message.encode('UTF-8'))
    f.close()

    webbrowser.open_new_tab('page.html')

# A function to actually change the wallpaper.
def change():
    num = input("enter number:")
    if (int(num) < 10):
        file = doRequest(list[int(num)])
        changeBg(file)
    else:
        print("error")
        change()

# The beginning of a gui implementation for the wallpaper program.
def draw():
    master = Tk()

    list = crawl()
    doRequest(list[0])

    img = PhotoImage(file=r"C:\Users\iamto\Pictures\.png")
    img1 = img.subsample(4, 4)
    img2 = PhotoImage(file=r"C:\Users\iamto\Pictures\*.png")
    img3 = img2.subsample(4, 4)

    Label(master, image=img1).grid(row=0, column=2,
                                   columnspan=2, rowspan=2, padx=5, pady=5)
    Label(master, image=img3).grid(row=2, column=2,
                                   columnspan=2, rowspan=2, padx=5, pady=5)

    button = Button(master, text='1', width=5, command=master.destroy)
    button.place(x=10, y=250)

    button = Button(master, text='2', width=5, command=master.destroy)
    button.place(x=10, y=535)

    button = Button(master, text='Stop', width=25, command=master.destroy)
    button.place(x=150, y=275)

    master.mainloop()


# do function calls, save the crawl function response to a list and then pass it to site to generate the
# fresh html version of the top of top wallpapers
list = crawl()
#site(list)
siteDetails(list)
# change()
# draw()

#TODO
# wallpaper needs to be converted to png to be shown
# need to fix this or figure out another way