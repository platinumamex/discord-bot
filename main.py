import discord
from discord.ext import commands
import random
import os
import asyncio
from collections import defaultdict
from typing import Optional
import aiohttp


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

leaderboard = defaultdict(lambda: {'wins': 0, 'games_played': 0})
# --- LOVE / FRIENDSHIP COMMANDS ---

hug_gifs = [
    "https://media.tenor.com/2roX3uxz_68AAAAM/cuddle-hug.gif",
    "https://media.tenor.com/1Z8V2aM8rRwAAAAM/hug-anime.gif",
    "https://media.tenor.com/G5D3y9B6vWAAAAAM/hug-love.gif",
    "https://media.tenor.com/YTzXvCuL1-0AAAAM/anime-hug.gif"
]

kiss_gifs = [
    "https://media.tenor.com/0YF3UPjDgwMAAAAM/anime-kiss.gif",
    "https://media.tenor.com/F02Ep3b2jJ4AAAAM/anime-kiss-love.gif",
    "https://media.tenor.com/Wx9IEmZZXSoAAAAM/kiss-anime.gif",
    "https://media.tenor.com/1Gr0Z1qM9QYAAAAM/anime-love.gif"
]

rape_gifs = [
    "https://www.gifmeat.com/wp-content/uploads/2018/07/Carter-Cruise-screaming-painful-anal-sex-gif.gif",
    "https://el.phncdn.com/gif/10528432.gif",
    "https://russmus.net/wp-content/uploads/2024/02/bbc-porn-gif-17.gif"
]


trivia_questions = [
    {
        'question': 'What is the most derogatory term?',
        'options': ['A) Nigga', 'B) Fuck you', 'C) Faggot', 'D) Cunt'],
        'answer': 'A'
    },
    {
        'question': 'What is the purpose of eating your own poop?',
        'options': ['A) Better gut health', 'B) Save money', 'C) You have a sexual kink', 'D) You enjoy the taste'],
        'answer': 'A'
    },
    {
        'question': 'Who is the most subscribed OnlyFans model?',
        'options': ['A) Sophie Rain', 'B) Arikytsya', 'C) Lana Rhoades', 'D) Angela White'],
        'answer': 'A'
    },
    {
        'question': 'Who has the loosest vagina?',
        'options': ['A) ', 'B) Arikytsya', 'C) Lana Rhoades', 'D) Angela White'],
        'answer': 'A'
    },
    {
        'question': 'In Iceland, there’s a traditional dish called hákarl. What is it made from?',
        'options': ['A) Shark piss', 'B) Women's vaginal discharge', 'C) Menstrual blood', 'D) Feces'],
        'answer': 'C'
    },
    {
        'question': 'Who has the biggest penis?',
        'options': ['A) Johnny Sins', 'B) Jonah Falcon', 'C) Ashban Aziz', 'D) Alex Jones'],
        'answer': 'B'
    },
    {
        'question': 'Who is the hottest female at our school?',
        'options': ['A) Maddy Shannon', 'B) Alyssa Assell', 'C) Fiona Reeves', 'D) Paiten Kruse'],
        'answer': 'C'
    },
    {
        'question': 'How big is Ashbans (uncut) Penis?',
        'options': ['A) 4 inches', 'B) 8 centimeters', 'C) 3 inches', 'D) 10 centimeters'],
        'answer': 'C'
    },
    {
        'question': 'Is it legal to rape underage girls in the Czech Republic ?',
        'options': ['A) Yes', 'B) No', 'C) Only if you are underage', 'D) Only if you are a man'],
        'answer': 'C'
    },
    {
        'question': 'What is NOT a fluid that leaks out of a woman's vagina?',
        'options': ['A) Semen', 'B) Vaginal Discharge', 'C) Pee', 'D) Menstrual blood'],
        'answer': 'A'
    }
]

magic_8ball_responses = [
    "It is certain.", "It is decidedly so.", "Without a doubt.",
    "Yes definitely.", "You may rely on it.", "As I see it, yes.",
    "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
    "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
    "Cannot predict now.", "Concentrate and ask again.",
    "Don't count on it.", "My reply is no.", "My sources say no.",
    "Outlook not so good.", "Very doubtful."
]

active_games = {}

adventure_story = [
    {
        'text': "🏰 **THE QUEST FOR SEX** 🏰\n\nYou wake up your house, under your cozy blanket and wet puddle from your wet dream last night...",
        'image': 'https://www.shutterstock.com/image-photo/pee-on-bed-mattressbed-wetting-260nw-2652335391.jpg'
    },
    {
        'text': "🗺️ **GOING DOWNSTAIRS FOR BREAKFAST** 🗺️\n\nYou go downstairs and see your sister cooking a suprise breakfast for you! How thoughtful and delicious!",
        'image': 'https://st4.depositphotos.com/4678277/31013/i/450/depositphotos_310132374-stock-photo-profile-side-view-of-her.jpg'
    },
    {
        'text': "🏔️ **THE HORNINESS BEGINS** 🏔️\n\nYour penis starts to harden slowly but surely...",
        'image': 'https://el.phncdn.com/gif/38869991.gif'
    },
    {
        'text': "🏘️ **BROTHER NO!!!!** 🏘️\n\nYour sister looks down and sees your massive cock throbbing and bloody, waiting to be sucked on! You waste no time and waddle over to your sister and put your hard, throbbing dick inside of her mouth!",
        'image': 'https://el.phncdn.com/pics/gifs/029/882/121/(m=ldpwiqacxtE_Ai)(mh=Ialgv7wcqF11znEN)29882121b.gif'
    },
    {
        'text': "⚔️ **OH NO! MOM WALKS IN...** ⚔️\n\nAfter finishing in her mouth, your step mom walks in!!",
        'image': 'https://media.tenor.com/Tm8gkHoGYfYAAAAM/walk-model.gif'
    },
    {
        'text': "🌙 **SHE GETS SOOOO WET!** 🌙\n\nYou expected your mom to be furious about your actions, but she gets turned on and wants to join!",
        'image': 'https://cdn05.iwantclips.com/uploads/contents/videos/73691/76d3fb924553f54b5f80ebf1222f4e4b.gif'
    },
    {
        'text': "🐲 **THREESOME TIME!** 🐲\n\nThe three of you are all turned on and decide to have a threesome! You decide to try ANAL for the first time...",
        'image': 'https://gifcandy.net/wp-content/uploads/2016/04/gifcandy-threesome-14.gif'
    },
    {
        'text': "💬 **TOO LOUD!** 💬\n\n'Your sister is moaning too loud! Your dad comes downstairs to see what all the noise is about.",
        'image': 'https://el.phncdn.com/pics/gifs/016/142/932/(m=ldpwiqacxtE_Ai)(mh=jLo6c9sh4lT5E4dM)16142932b.gif'
    },
    {
        'text': "🤝 **UNEXPECTED TURN!** 🤝\n\nYour dad is so turned on that he goes straight for your sister! No such thing as a perfect family without some INCEST!",
        'image': 'https://el.phncdn.com/pics/gifs/041/089/901/(m=ldpwiqacxtE_Ai)(mh=gn669CXq-CdXrC-G)41089901b.gif'
    },
    {
        'text': "👑 **HAPPILY EVER AFTER!** 👑\n\nDad decides to finish inside of your sister! After a few weeks, she is now PREGNANT and is planning on keeping the baby!",
        'image': 'https://media0.giphy.com/media/v1.Y2lkPTZjMDliOTUydWExaWYwM2c4ZmM4bHpxYngzYnZjNXRwbmR4Z2N0bHNlZXgzZXRjdCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/g11HmKv2CkS3rSOuUi/source.gif'
    }
]

active_games = {}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guilds')

@bot.command(name='love_help', help='Shows love and fun interaction commands')
async def love_help(ctx):
    embed = discord.Embed(
        title="💖 Love & Friendship Commands",
        description="Spread positivity and affection with these commands!",
        color=discord.Color.pink()
    )

    embed.add_field(
        name="!hug @user",
        value="Send a warm hug to someone.",
        inline=False
    )
    embed.add_field(
        name="!kiss @user",
        value="Send someone a kiss 💋",
        inline=False
    )
    embed.add_field(
        name="!rape @user",
        value="Rape someone! 👋",
        inline=False
    )

    await ctx.send(embed=embed)


@bot.command(name='help_games', help='Shows all available game commands')
async def help_games(ctx):
    embed = discord.Embed(
        title="🎮 Games Bot Commands",
        description="Here are all the fun games you can play!",
        color=discord.Color.blue()
    )
    
    embed.add_field(
        name="!rps <choice>",
        value="Play Rock, Paper, Scissors\nExample: `!rps rock`",
        inline=False
    )
    embed.add_field(
        name="!mindread",
        value="The bot will read your mind and guess your number!\nExample: `!mindread`",
        inline=False
    )
    embed.add_field(
        name="!trivia",
        value="Answer a random trivia question",
        inline=False
    )
    embed.add_field(
        name="!8ball <question>",
        value="Ask the magic 8-ball a question\nExample: `!8ball Will I win?`",
        inline=False
    )
    embed.add_field(
        name="!coinflip",
        value="Flip a coin (Heads or Tails)",
        inline=False
    )
    embed.add_field(
        name="!roll [sides]",
        value="Roll a dice (default 6 sides)\nExample: `!roll 20`",
        inline=False
    )
    embed.add_field(
        name="!adventure",
        value="Start an epic adventure story with GIFs!\nExample: `!adventure`",
        inline=False
    )
    embed.add_field(
        name="!leaderboard",
        value="View the games leaderboard",
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name='rps', help='Play Rock, Paper, Scissors')
async def rock_paper_scissors(ctx, choice: Optional[str] = None):
    if not choice:
        await ctx.send("Please choose: rock, paper, or scissors!\nExample: `!rps rock`")
        return
    
    choice = choice.lower()
    valid_choices = ['rock', 'paper', 'scissors']
    
    if choice not in valid_choices:
        await ctx.send(f"Fuck you nigga! Please choose a valid choice: {', '.join(valid_choices)}")
        return
    
    bot_choice = random.choice(valid_choices)
    
    result = determine_rps_winner(choice, bot_choice)
    
    emojis = {
        'rock': '🪨',
        'paper': '📄',
        'scissors': '✂️'
    }
    
    embed = discord.Embed(title="🎮 Rock, Paper, Scissors", color=discord.Color.green())
    embed.add_field(name="Your choice", value=f"{emojis[choice]} {choice.capitalize()}", inline=True)
    embed.add_field(name="Bot's choice", value=f"{emojis[bot_choice]} {bot_choice.capitalize()}", inline=True)
    
    user_id = str(ctx.author.id)
    leaderboard[user_id]['games_played'] += 1
    
    if result == 'win':
        embed.add_field(name="Result", value="🎉 You win!", inline=False)
        embed.color = discord.Color.gold()
        leaderboard[user_id]['wins'] += 1
    elif result == 'lose':
        embed.add_field(name="Result", value="😢 You lose!", inline=False)
        embed.color = discord.Color.red()
    else:
        embed.add_field(name="Result", value="🤝 It's a tie!", inline=False)
        embed.color = discord.Color.blue()
    
    await ctx.send(embed=embed)

def determine_rps_winner(player, bot):
    if player == bot:
        return 'tie'
    
    wins = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if wins[player] == bot:
        return 'win'
    return 'lose'

@bot.command(name='mindread', help='The bot will read your mind!')
async def mindread(ctx):
    user_id = ctx.author.id
    active_games[user_id] = {
        'type': 'mindread'
    }
    
    embed = discord.Embed(
        title="🔮 Mind Reading",
        description="Think of a number between **1** and **1,000,000** and type it in the chat!\n\nI will read your mind and guess it correctly... 🧠✨",
        color=discord.Color.purple()
    )
    
    await ctx.send(embed=embed)

@bot.command(name='adventure', help='Start an adventure story!')
async def adventure(ctx):
    user_id = ctx.author.id
    
    active_games[user_id] = {
        'type': 'adventure',
        'scene': 0
    }
    
    scene_data = adventure_story[0]
    
    embed = discord.Embed(
        title="📖 The Dragon's Quest",
        description=scene_data['text'],
        color=discord.Color.green()
    )
    
    embed.set_image(url=scene_data['image'])
    embed.set_footer(text="Type 'next' to continue the story...")
    
    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    user_id = message.author.id
    
    if user_id in active_games and active_games[user_id]['type'] == 'mindread':
        try:
            user_number = int(message.content)
            
            if user_number < 1 or user_number > 1000000:
                await message.channel.send("Please choose a number between 1 and 1,000,000!")
                return
            
            thinking_embed = discord.Embed(
                title="🧠 Reading your mind...",
                description="Let me concentrate... 🔮",
                color=discord.Color.purple()
            )
            thinking_msg = await message.channel.send(embed=thinking_embed)
            
            await asyncio.sleep(5)
            
            reveal_embed = discord.Embed(
                title="✨ I've got it!",
                description=f"You were thinking of the number **{user_number}**!",
                color=discord.Color.gold()
            )
            await thinking_msg.edit(embed=reveal_embed)
            
            del active_games[user_id]
            return
                
        except ValueError:
            await message.channel.send("Please type a valid number between 1 and 1,000,000!")
            return
    
    if user_id in active_games and active_games[user_id]['type'] == 'adventure':
        if message.content.lower() != 'next':
            return
        
        current_scene = active_games[user_id]['scene']
        next_scene = current_scene + 1
        
        if next_scene >= len(adventure_story):
            embed = discord.Embed(
                title="📖 The Dragon's Quest",
                description="✨ **THE END** ✨\n\nThank you for playing!",
                color=discord.Color.gold()
            )
            embed.set_footer(text="Type !adventure to play again!")
            await message.channel.send(embed=embed)
            del active_games[user_id]
            return
        
        scene_data = adventure_story[next_scene]
        active_games[user_id]['scene'] = next_scene
        
        embed = discord.Embed(
            title="📖 The Dragon's Quest",
            description=scene_data['text'],
            color=discord.Color.green()
        )
        
        embed.set_image(url=scene_data['image'])
        
        if next_scene == len(adventure_story) - 1:
            embed.color = discord.Color.gold()
            embed.set_footer(text="Type 'next' for the finale...")
        else:
            embed.set_footer(text="Type 'next' to continue the story...")
        
        await message.channel.send(embed=embed)
        return
    
    if user_id in active_games and active_games[user_id]['type'] == 'trivia':
        answer = message.content.upper()
        if answer in ['A', 'B', 'C', 'D']:
            game = active_games[user_id]
            correct_answer = game['answer']
            
            user_id_str = str(user_id)
            leaderboard[user_id_str]['games_played'] += 1
            
            if answer == correct_answer:
                leaderboard[user_id_str]['wins'] += 1
                embed = discord.Embed(
                    title="✅ Correct!",
                    description="You got it right! Well done! 🎉",
                    color=discord.Color.green()
                )
            else:
                embed = discord.Embed(
                    title="❌ Wrong!",
                    description=f"The correct answer was **{correct_answer}**",
                    color=discord.Color.red()
                )
            
            await message.channel.send(embed=embed)
            del active_games[user_id]
            return
    
    await bot.process_commands(message)

@bot.command(name='trivia', help='Answer a trivia question')
async def trivia(ctx):
    question_data = random.choice(trivia_questions)
    
    user_id = ctx.author.id
    active_games[user_id] = {
        'type': 'trivia',
        'answer': question_data['answer']
    }
    
    embed = discord.Embed(
        title="🧠 Trivia Question",
        description=question_data['question'],
        color=discord.Color.blue()
    )
    
    for option in question_data['options']:
        embed.add_field(name=option, value="\u200b", inline=False)
    
    embed.set_footer(text="Type the letter of your answer (A, B, C, or D)")
    
    await ctx.send(embed=embed)

@bot.command(name='8ball', help='Ask the magic 8-ball a question')
async def magic_8ball(ctx, *, question: Optional[str] = None):
    if not question:
        await ctx.send("You need to ask a question!\nExample: `!8ball Will I win the game?`")
        return
    
    response = random.choice(magic_8ball_responses)
    
    embed = discord.Embed(
        title="🔮 Magic 8-Ball",
        color=discord.Color.purple()
    )
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=response, inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='coinflip', help='Flip a coin')
async def coinflip(ctx):
    result = random.choice(['Heads', 'Tails'])
    emoji = '🟡' if result == 'Heads' else '⚪'
    
    embed = discord.Embed(
        title="🪙 Coin Flip",
        description=f"{emoji} **{result}**!",
        color=discord.Color.gold()
    )
    
    await ctx.send(embed=embed)

@bot.command(name='roll', help='Roll a dice')
async def roll_dice(ctx, sides: int = 6):
    if sides < 2:
        await ctx.send("A dice must have at least 2 sides!")
        return
    
    if sides > 100:
        await ctx.send("That's too many sides! Maximum is 100.")
        return
    
    result = random.randint(1, sides)
    
    embed = discord.Embed(
        title=f"🎲 Rolling a {sides}-sided dice",
        description=f"You rolled a **{result}**!",
        color=discord.Color.green()
    )
    
    await ctx.send(embed=embed)

@bot.command(name='purge', help='Delete a number of messages (Admin only)')
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    try:
        if amount < 1:
            await ctx.send("Please specify a number greater than 0.")
            return

        # Deletes command message + previous messages
        deleted = await ctx.channel.purge(limit=amount + 1)
        confirm = await ctx.send(f"🧹 Deleted {len(deleted) - 1} messages.")
        await asyncio.sleep(3)
        await confirm.delete()
    except discord.Forbidden:
        await ctx.send("❌ I don’t have permission to delete messages in this channel.")
    except discord.HTTPException as e:
        await ctx.send(f"⚠️ An error occurred: {e}")

@bot.command(name='hug', help='Send someone a hug ❤️')
async def hug(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("You need to tag someone to hug! Example: `!hug @username`")
        return

    gif = random.choice(hug_gifs)
    embed = discord.Embed(
        title="🤗 Hug Time!",
        description=f"{ctx.author.mention} gives {member.mention} a warm hug ❤️",
        color=discord.Color.pink()
    )
    embed.set_image(url=gif)
    await ctx.send(embed=embed)


@bot.command(name='kiss', help='Send someone a kiss 💋')
async def kiss(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Tag someone to kiss! Example: `!kiss @username`")
        return

    gif = random.choice(kiss_gifs)
    embed = discord.Embed(
        title="💋 Kiss!",
        description=f"{ctx.author.mention} gives {member.mention} a sweet kiss 💞",
        color=discord.Color.magenta()
    )
    embed.set_image(url=gif)
    await ctx.send(embed=embed)


@bot.command(name='rape', help='Playfully rape someone 👋')
async def rape(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Tag someone to rape! Example: `!rape @username`")
        return

    gif = random.choice(rape_gifs)
    embed = discord.Embed(
        title="👋 Rape!",
        description=f"{ctx.author.mention} playfully rapes {member.mention}! 😂",
        color=discord.Color.orange()
    )
    embed.set_image(url=gif)
    await ctx.send(embed=embed)

@bot.command(name='leaderboard', help='View the games leaderboard')
async def show_leaderboard(ctx):
    if not leaderboard:
        await ctx.send("No games have been played yet! Start playing to get on the leaderboard!")
        return
    
    sorted_players = sorted(
        leaderboard.items(),
        key=lambda x: (x[1]['wins'], -x[1]['games_played']),
        reverse=True
    )
    
    embed = discord.Embed(
        title="🏆 Games Leaderboard",
        description="Top players ranked by wins!",
        color=discord.Color.gold()
    )
    
    for i, (user_id, stats) in enumerate(sorted_players[:10], 1):
        try:
            user = await bot.fetch_user(int(user_id))
            username = user.name
        except:
            username = f"User {user_id}"
        
        win_rate = (stats['wins'] / stats['games_played'] * 100) if stats['games_played'] > 0 else 0
        
        medal = ""
        if i == 1:
            medal = "🥇 "
        elif i == 2:
            medal = "🥈 "
        elif i == 3:
            medal = "🥉 "
        
        embed.add_field(
            name=f"{medal}{i}. {username}",
            value=f"Wins: {stats['wins']} | Games: {stats['games_played']} | Win Rate: {win_rate:.1f}%",
            inline=False
        )
    
    await ctx.send(embed=embed)

token = os.environ.get('DISCORD_BOT_TOKEN')
if not token:
    print("ERROR: DISCORD_BOT_TOKEN environment variable not found!")
    print("Please set your Discord bot token in the Secrets tab.")
else:
    bot.run(token)
