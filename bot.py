import json
import bs4
import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = "/")

@bot.command()
async def Biography(ctx, *, arg=None):
    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    request_data = requests.get(f'https://www.instagram.com/{arg}/?__a=1', headers=headers)
    user_json = json.loads(request_data.text)
    Biography = user_json['graphql']['user']['biography']
    await ctx.channel.send(Biography)

@bot.command()
async def is_private(ctx, *, arg=None):
    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    request_data = requests.get(f'https://www.instagram.com/{arg}/?__a=1', headers=headers)
    user_json = json.loads(request_data.text)
    is_private = user_json['graphql']['user']['is_private']
    await ctx.channel.send(is_private)

@bot.command()
async def is_verified(ctx, *, arg=None):
    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    request_data = requests.get(f'https://www.instagram.com/{arg}/?__a=1', headers=headers)
    user_json = json.loads(request_data.text)
    is_verified = user_json['graphql']['user']['is_verified']
    await ctx.channel.send(is_verified)

@bot.command()
async def full_name(ctx, *, arg=None):
    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    request_data = requests.get(f'https://www.instagram.com/{arg}/?__a=1', headers=headers)
    user_json = json.loads(request_data.text)
    full_name = user_json['graphql']['user']['full_name']
    await ctx.channel.send(full_name)

@bot.command()
async def external_url(ctx, *, arg=None):
    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    request_data = requests.get(f'https://www.instagram.com/{arg}/?__a=1', headers=headers)
    user_json = json.loads(request_data.text)
    external_url = user_json['graphql']['user']['external_url']
    await ctx.channel.send(external_url)

@bot.command()
async def profile_pic(ctx, *, arg=None):
    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    request_data = requests.get(f'https://www.instagram.com/{arg}/?__a=1', headers=headers)
    user_json = json.loads(request_data.text)
    profile_pic = user_json['graphql']['user']['profile_pic_url_hd']
    await ctx.channel.send(profile_pic)

@bot.command()
async def following(ctx, *, arg=None):
    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    request_data = requests.get(f'https://www.instagram.com/{arg}/?__a=1', headers=headers)
    user_json = json.loads(request_data.text)
    following = user_json['graphql']['user']['edge_followed_by']['count']
    await ctx.channel.send(following)

@bot.command()
async def followers(ctx, *, arg=None):
    headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    request_data = requests.get(f'https://www.instagram.com/{arg}/?__a=1', headers=headers)
    user_json = json.loads(request_data.text)
    followers = user_json['graphql']['user']['edge_follow']['count']
    await ctx.channel.send(followers)

@bot.command()
async def no_posts(ctx, *, arg=None):
    URL = "https://www.instagram.com/"+str(arg)
    HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    response = requests.get(URL, headers=HEADERS)
    soup=bs4.BeautifulSoup(response.text,"html.parser")
    posts = (str(soup.find('meta',attrs={'property':"og:description"})).split(",")[2].split("-")[0].replace("Posts"," "))
    await ctx.channel.send(posts)

bot.run(os.environ['Token'])