# -*- coding: utf-8 -*-

import re

from discord.ext import commands


class Amongus(commands.Cog):
    """The description for Amongus goes here."""

    def __init__(self, bot):
        self.bot = bot
        self.last_invite_code = None

    @commands.Cog.listener()
    async def on_message(self, message):
        result = re.match(r"^[A-Z]{6}$", message.content)
        if result:
            if self.last_invite_code is None:
                self.last_invite_code = message
            else:
                await self.last_invite_code.delete()
                self.last_invite_code = message


def setup(bot):
    bot.add_cog(Amongus(bot))
