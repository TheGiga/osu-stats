"""
By gigabit- AKA https://github.com/TheGiga 24.03.2022
Glory to Ukraine.
"""

import os

import discord
from discord import Option, SlashCommandOptionType
from dotenv import load_dotenv

from lib import OsuBot, Api, UserNotFound, RANKING_EMOJIS, UserScoreNotFound

load_dotenv()
intents = discord.Intents.default()

bot_instance = OsuBot(intents=intents)
API = Api(api_key=os.getenv("API_KEY"))


@bot_instance.event
async def on_ready():
    print("Bot is running...")


@bot_instance.slash_command(name='information', description='Information about osu!stats bot.')
async def info_command(
        ctx: discord.ApplicationContext
):
    embed = discord.Embed(
        title='osu!stats', colour=discord.Colour.magenta(), timestamp=discord.utils.utcnow(),
        description="""
            **osu!stats** is an open source project made by `gigalegit-#0880`.
            
            [Click here for source code](https://github.com/TheGiga/osu-stats)
        """
    )

    embed.set_footer(text=f'{len(bot_instance.guilds)} guilds.')

    await ctx.respond(embed=embed)


@bot_instance.slash_command(name='player', description='Check player statistics.')
async def osu_player(
        ctx: discord.ApplicationContext,
        name: str,
        mode: Option(
            SlashCommandOptionType.string,
            description="osu! game type.",
            choices=["osu!", "osu!mania", "Taiko", "CtB"]
        )
):
    try:
        player = await API.get_osu_player(name=name, mode=mode)
    except UserNotFound:
        return await ctx.respond(
            embed=discord.Embed(title="User not found!", colour=discord.Colour.red()),
            ephemeral=True
        )

    try:
        best_score = await player.best_score
        best_score_map = await best_score.map
    except UserScoreNotFound:
        return await ctx.respond(
            embed=discord.Embed(title="User has no stats in this game mode!", colour=discord.Colour.red()),
            ephemeral=True
        )

    embed = discord.Embed(
        title=f'{player.username} - Lvl. {player.level}',
        timestamp=discord.utils.utcnow(),
        description=f"""
            Showing only __RANKED__ statistics in __{player.game_mode}__ game mode.
            
            **PP:** **`{player.pp}`**
            **Rank:** `{player.rank}` | `{player.country_rank}` :flag_{player.country.lower()}:
            **Accuracy**: `{player.accuracy}%`
            
            **SS** count: `{player.total_ss}`
            **S** count: `{player.total_s}`
            
            Player country is **{player.country}** :flag_{player.country.lower()}:
            
            **BEST SCORE**:
            ｜ {RANKING_EMOJIS.get(best_score.rank)} - **{best_score_map.title}**
            ｜ With **{best_score.misses}**:x:
            ｜ `PP:` **{best_score.pp}**
            
            [Go to website profile](https://osu.ppy.sh/users/{player.user_id})
        """,
        colour=discord.Colour.purple()
    )

    embed.set_thumbnail(url=player.profile_image_url)
    embed.set_footer(text=f'ID: {player.user_id}')

    await ctx.respond(embed=embed)


if __name__ == "__main__":
    bot_instance.run(os.getenv("TOKEN"))
