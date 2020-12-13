# -*- coding: utf-8 -*-

import re
from collections import defaultdict

import discord
from discord.ext import commands


class Amongus(commands.Cog):
    """The description for Amongus goes here."""

    def __init__(self, bot):
        self.bot = bot
        self.last_invite_code = defaultdict(lambda: None)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild is None:
            return

        result = re.match(r"^[A-Z]{6}$", message.content)
        if result:
            if not self.last_invite_code[message.guild]:
                self.last_invite_code[message.guild] = message
            else:
                try:
                    await self.last_invite_code[message.guild].delete()
                except discord.Forbidden:
                    await message.channel.send('I am missing permissions to delete messages.')
                except discord.HTTPException:
                    pass
                self.last_invite_code[message.guild] = message
        elif message.application:
            await message.channel.send(message.activity['party_id'])


def setup(bot):
    bot.add_cog(Amongus(bot))
