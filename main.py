import json
import random
from discord.ext import commands
from discord import Intents
from discord import File as sendFile
from discord import TextChannel
from reddit_api import api_reddit
from chucknorris_api import api_chucknorris

config_json_file = "./config.json"
with open(config_json_file) as f:
    config = json.load(f)

async def reddit_msg(ctx):
    reddit = api_reddit()

    if reddit['status_code'] == 200:
        await ctx.send(reddit['title'])
        await ctx.send(reddit['img_url'])
        return
    
    error = f'Reddit API Error {reddit["status_code"]} : {reddit["reason"]}'
    await ctx.send(error)
    await ctx.send('\N{face screaming in fear}')

async def chucknorris_msg(ctx):
    chucknorris= api_chucknorris()

    if chucknorris['status_code'] == 200:
        await ctx.send(chucknorris['value'])
        return
    
    error = f'ChuckNorris API Error {chucknorris["status_code"]} : {chucknorris["reason"]}'
    await ctx.send(error)
    await ctx.send('\N{face screaming in fear}')

def main() -> None:
    bot_token = config['bot_token']
    intents = Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix = '!', intents = intents)
   
    @client.event
    async def on_ready():
        print("Bot is ready")

    @client.command(aliases=['m'])
    async def msg(ctx, *, input = None):
        api_list = ['reddit','chucknorris']
        
        match random.choice(api_list):
            case 'reddit':
                await reddit_msg(ctx)
            case 'chucknorris':
                await chucknorris_msg(ctx)

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        raise error

    client.run(bot_token)

if __name__ == '__main__':
    main()