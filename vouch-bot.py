import discord
from discord import app_commands
from discord.ext import commands

# installiere die Discord libary mit: pip install -U discord.py


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "" # Mach dein Discord Token zwischen ""
WELCOME_CHANNEL_ID = 123456789101112 # ersetze mit deiner Discord Channel ID
LEAVE_CHANNEL_ID = 123456789101112   # ersetze mit deiner Discord Channel ID
@bot.event
async def on_ready():
    print(f"Bot ist online als {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} Slash-Commands synchronisiert.")
    except Exception as e:
        print(f"Fehler beim Sync: {e}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title=f"Welcome {member.name}",
            description="Welcome to the server! Please read the rules and enjoy your stay.",
            color=discord.Color.blue()
        )
        await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(LEAVE_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title=f"Goodbye {member.name}",
            description="We're sad to see you go! If you have any feedback, please let us know.",
            color=discord.Color.red()
        )
        await channel.send(embed=embed)

@bot.tree.command(name="vouch", description="Vouch a Staff")
@app_commands.describe(
    user="User to vouch",
    product="Product you have purchased",
    rating="1-10"
)
async def vouch(interaction: discord.Interaction, user: discord.User, product: str, rating: int):
    embed = discord.Embed(
        title=f"Vouch",
        description=f"Vouch for {user.mention}\n By {interaction.user.mention}\n Product: {product}\n Rating:{rating}/10",
        color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed)
                                            
bot.run(TOKEN)