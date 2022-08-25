import discord
from discord.ext import commands  # IDK, in the case I don't want to use slash
from discord.ext.commands import BucketType, cooldown
import os  # default module
from dotenv import load_dotenv

load_dotenv()  # load all the variables from the env file
bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="massdeleterole",
                   description="Mass delete a specific role, purpose-used after raids. Only available to administrators.")
@discord.default_permissions(administrator=True)
@commands.cooldown(1, 3, BucketType.guild)
@commands.has_permissions(administrator=True)
async def massdeleterole(ctx, rolename: str):
    for role in ctx.guild.roles:
        print(role)
        message = await ctx.respond('Deleting roles...')
        count = 0
        if str(rolename) in str(role):
            count += 1
            await role.delete()
        if count == 0:
            return await message.edit_original_message(content=f':white_check_mark: No role found named `{rolename}`.')
        await message.edit(f':white_check_mark: Successfully deleted {count} roles.')

bot.run(os.getenv('TOKEN'))  # run the bot with the token
