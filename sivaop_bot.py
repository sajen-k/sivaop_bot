from discord.ext import commands
from shannon_coding import shannon_coding
from formulas import *

bot = commands.Bot(command_prefix='+')
TOKEN = ''

with open('token.txt', 'r') as f:
    TOKEN = f.readlines()[2]

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

@bot.command(rest_is_raw=True, name='information')
async def info(ctx, *, args):
    args = args.split()
    if len(args) > 1:
        await ctx.send("Too many arguments.")
        return
    await ctx.send(information(float(args[0])))

@bot.command(rest_is_raw=True, name='entropy')
async def e(ctx, *, args):
    probabilities = list(map(float, args.split()))
    await ctx.send(entropy(probabilities))

@bot.command(rest_is_raw=True)
async def shannon(ctx, *, args):
    """
    probabilities = list(map(float, args.split()))
    answer = shannon_coding(probabilities)
    s = ''
    for prob, bin, length in zip(probabilities, answer['idx_to_bin'].values(), answer['idx_to_len'].values()):
        s += str(prob) + '\t' + bin + '\t' + str(length) + '\n'
    await ctx.send(s)
    await ctx.send(f"Entropy: {answer['H']}\nAverage length: {answer['lavg']}\nEfficiency: {answer['eff']}\nRedundancy: {answer['red']}\nCode Variance: {answer['cv']}")
    """
    result = solve(args, shannon_coding)
    ctx.send(result)

@bot.command(rest_is_raw=True)
async def huffman(ctx, *, args):
    result = solve(args, huffman_coding)
    ctx.send(result)


        
bot.run(TOKEN)