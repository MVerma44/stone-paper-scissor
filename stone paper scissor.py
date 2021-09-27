import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

l = ['s', 'p', 'sc']

global chance
chance = 10
global your_score
your_score = 0
global com_score
com_score = 0
global no_of_chance_left
no_of_chance_left = 0
global game_tied
game_tied = 0


@client.command()
async def start(ctx, play : discord.Member):
    global no_of_chance_left
    global your_score
    global com_score
    global players
    players = play

    no_of_chance_left = 0
    your_score = 0
    com_score = 0

    embed = discord.Embed(title="Instructions to play the game\n1. :headstone:  's' stands for Stone\n2. :page_facing_up: 'p' stands for Paper\n3. :scissors: 'sc' for Scissor\n"
                                "You have 10 chances to beat TGB :robot:", colour=discord.Colour.from_rgb(0, 255, 255))
    await ctx.reply(embed=embed)


@client.command()
async def t(ctx, _inp: str):
    global no_of_chance_left
    global game_tied
    global com_score
    global your_score
    global turn
    global players

    turn = ctx.author

    if turn == players:
        _ran = random.choice(l)

        if _inp.lower() == _ran.lower():
            await ctx.reply(f":expressionless: :face_with_raised_eyebrow: Game tied\nYou guessed, {_inp} and Computer guessed, {_ran}")
            game_tied += 1

        elif _inp not in l:
            no_of_chance_left -= 1

        elif (_inp == "s" ) and (_ran == "p"):
            com_score += 1
            await ctx.reply(f"You guessed, {_inp} and Computer guessed, {_ran}\n"
                            f":robot: Computer is the winner in this round\n"
                            f"Paper catches the stone")

        elif (_inp == "p" ) and (_ran == "sc"):
            com_score += 1
            await ctx.reply(f"You guessed, {_inp} and Computer guessed, {_ran}\n"
                            f":robot: Computer is the winner in this round\n"
                            f"Scissor cut the piece of paper")

        elif (_inp == "p") and (_ran == "s") :
            your_score += 1
            await ctx.reply(f"You guessed, {_inp} and Computer guessed, {_ran}\n"
                            f":person_raising_hand: You are the winner in this round\n"
                            f"Paper catches the stone")

        elif (_inp == "sc") and (_ran == "s"):
            com_score += 1
            await ctx.reply(f"You guessed, {_inp} and Computer guessed, {_ran}\n"
                            f":robot: Computer is the winner in this round\n"
                            f"Stone breaks the scissor")

        elif (_inp == "sc") and (_ran == "p"):
            your_score = your_score + 1
            await ctx.reply(f"You guessed, {_inp} and Computer guessed, {_ran}\n"
                            f":person_raising_hand: You are the winner in this round\n"
                            f"Scissor cut the piece of paper")

        elif (_inp == "s" ) and (_ran == "sc"):
            your_score = your_score + 1
            await ctx.reply(f"You guessed, {_inp} and Computer guessed, {_ran}\n"
                            f":person_raising_hand: ou are the winner in this round\n"
                            f"Stone breaks the scissor")

        no_of_chance_left += 1

    if no_of_chance_left >= 10:
        if your_score > com_score:
            embed = discord.Embed(title=f"{ctx.author.name}'s score is {your_score} and TGB's score is {com_score}"
                            f"\n:person_raising_hand: Congrats {ctx.author.name}! you are the winner\n"
                            f"Start a new game.", colour=discord.Colour.green())
            await ctx.reply(embed=embed)

        elif your_score == com_score:
            embed = discord.Embed(title=f"{ctx.author.name}'s score is {your_score} and TGB's score is {com_score}"
                            "\nGame tied\nStart a new game.", colour=discord.Colour.teal())
            await ctx.reply(embed=embed)

        else:
            embed = discord.Embed(title=f"{ctx.author.name}'s score is {your_score} and TGB's score is {com_score}"
                            f"\n:robot:  TGB is the winner as always\nBetter luck next time. Start a new game.", colour=discord.Colour.dark_red())
            await ctx.reply(embed=embed)

        your_score = 0
        com_score = 0
        no_of_chance_left = 0

    elif turn != players:
        await ctx.reply("It's not your turn so just sit & keep quite, don't jump in between.")


client.run('Your_bot_token')