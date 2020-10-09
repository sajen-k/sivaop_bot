from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if 'elon sucks' in message.content:
        await message.channel.send('Don\'t you dare say that about elon!')
    
    if bot.user in message.mentions:
        await message.channel.send(f'Hi {message.author.mention}, how may I help you?')

    if message.content == 'hi':
        await message.add_reaction('👋')

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command(rest_is_raw=True)
async def s(ctx, *, args):
    if ctx.author.id == 393093317233082370:
        await ctx.message.delete()
        await ctx.send(args)
        

bot.run('your token here')