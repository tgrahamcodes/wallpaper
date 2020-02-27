# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import ctypes
import requests
import shutil
import bs4
import re
import webbrowser
import praw
import random


list = []


def test():
    print("test")


def draw():
    top = Tk()
    top.geometry("100x100")

    list = crawl()
    doRequest(list[0])

    B = Button(top, text="set", command=test)
    B.place(x=50, y=50)
    top.mainloop()


def changeBg(PATH):
    ctypes.windll.user32.SystemParametersInfoW(
        20, 0, PATH, 3)


def doRequest(URL):
    r = requests.get(URL, stream=True)
    URL = URL.strip('.')
    print(URL)
    filename = "C:\\Users\\iamto\\Pictures\\Wallpaper\\" + "background.png"
    print(filename)
    with open(filename, 'wb') as out_file:
        shutil.copyfileobj(r.raw, out_file)
    del r


def crawl():
    reddit = praw.Reddit(client_id='7-4B300Ip7f-iw',
                         client_secret='rR8THfrDUqKQ8qval9YycTLaQkw',
                         user_agent='crawlbot')
    if (reddit.read_only):
        print('Successfully connected to bot.')

    for submission in reddit.subreddit('wallpaper').hot(limit=20):
        list.append(submission.url)

    for submission in reddit.subreddit('wallpapers').hot(limit=20):
        list.append(submission.url)

    for submission in reddit.subreddit('wallpaperdump').hot(limit=20):
        list.append(submission.url)

    for submission in reddit.subreddit('WQHD_Wallpaper').hot(limit=20):
        list.append(submission.url)

    return list

   # bs = bs4.BeautifulSoup(html, 'html.parser')
   # images = bs.find_all('img', {'src': re.compile('.jpg')})

   # for image in images:
   #     print(image['src']+'\n')

   # PATH = 'C:\\Users\\iamto\\Pictures\\Wallpaper\\background.jpg'
   # URL = 'https://c4.wallpaperflare.com/wallpaper/410/867/750/vector-forest-sunset-forest-sunset-forest-wallpaper-preview.jpg'
   # doRequest(URL)
   # changeBg(PATH)


def details(list):
    print("Length: " + len(list))


def site(list):

    f = open('page.html', 'wb')

    page = ""

    for url in list:
        message = """
        <a href=""" + list[0] + """><img height=300px width=500px src=""" + list[0] + """>
        <a href=""" + list[1] + """><img height=300px width=500px src=""" + list[1] + """>
        <a href=""" + list[2] + """><img height=300px width=500px src=""" + list[2] + """>
        <a href=""" + list[3] + """><img height=300px width=500px src=""" + list[3] + """>
        <a href=""" + list[4] + """><img height=300px width=500px src=""" + list[4] + """>
        <a href=""" + list[5] + """><img height=300px width=500px src=""" + list[5] + """>
        <a href=""" + list[6] + """><img height=300px width=500px src=""" + list[6] + """>
        <a href=""" + list[7] + """><img height=300px width=500px src=""" + list[7] + """>
        <a href=""" + list[8] + """><img height=300px width=500px src=""" + list[8] + """>
        <a href=""" + list[9] + """><img height=300px width=500px src=""" + list[9] + """>
        <a href=""" + list[10] + """><img height=300px width=500px src=""" + list[10] + """>
        """

    newMessage = page + message
    f.write(newMessage.encode('UTF-8'))
    f.close()

    webbrowser.open_new_tab('page.html')


# site(list)
draw()
