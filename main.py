import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

@bot.command()
async def test(ctx):
    await ctx.send("OK JE MARCHE")

@bot.command()
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send("🔒 Lock OK")

@bot.command()
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send("🔓 Unlock OK")


@bot.command()
@commands.has_permissions(administrator=True)
async def booster(ctx):
    embed = discord.Embed(
        title="💎 ・Avantages des Boosters",
        description=(
            "Merci de soutenir le serveur en le boostant ! ❤️\n\n"
            "En obtenant le rôle **<@&1520067918392459284>**, vous débloquez les avantages suivants :"
        ),
        color=0xFF69B4
    )

    embed.add_field(
        name="✨ Vos avantages",
        value=(
            "▸ 🎖️ **Accès prioritaire**\n"
            "Débloquez plus rapidement les rôles évolutifs.\n\n"

            "▸ 🎨 **Rôle personnalisé**\n"
            "Choisissez le nom et la couleur de votre rôle.\n\n"

            "▸ 🖼️ **Images & GIFs**\n"
            "Envoyez librement des images et des GIFs dans les salons autorisés."
        ),
        inline=False
    )

    embed.add_field(
        name="💖 Merci !",
        value="Votre soutien permet d'améliorer et de faire vivre le serveur. Merci à tous nos Boosters !",
        inline=False
    )

    embed.set_footer(text="Merci pour votre soutien 😁")

    embed.set_image(
        url="https://tse2.mm.bing.net/th/id/OIP.EuK-k4KBxm-6eb1Kumtr_wHaET?r=0&cb=thfvnextfalcon3&rs=1&pid=ImgDetMain&o=7&rm=3"
    )

    await ctx.send(embed=embed)

bot.run("MTUyMTA5NTk4NDAzMTk5MzkxNg.G4CcXp.Tw8Lo01JwyCoB04PwUqc10Wn8sq77PgPcGHmSU")
