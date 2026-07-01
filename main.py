import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

# 👋 BIENVENUE
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(
            f"👋 Bienvenue {member.mention} !\n"
            f"Tu es le membre n°{member.guild.member_count} R2FG 💸 🎈"
        )

# 🧪 TEST
@bot.command()
async def test(ctx):
    await ctx.send("OK JE MARCHE")

# 🔒 LOCK (admin only)
@bot.command()
async def lock(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("🔒 Salon verrouillé")
    else:
        await ctx.send("❌ Tu n'as pas la permission")

# 🔓 UNLOCK (admin only)
@bot.command()
async def unlock(ctx):
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.send("🔓 Salon déverrouillé")
    else:
        await ctx.send("❌ Tu n'as pas la permission")

bot.run(os.getenv("TOKEN"))
