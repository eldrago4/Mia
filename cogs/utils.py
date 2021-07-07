import discord
import urbandictionary as ud
from discord.ext import commands

@commands.command(aliases=['urban'])
    async def ud(self, ctx, *, query):
        '''Search terms with urbandictionary.com'''
        em = discord.Embed(title=f'{query}', color=discord.Color.green())
        em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        em.set_footer(text='Powered by urbandictionary.com')
        defs = ud.define(query)
        try:
            res = defs[0]
        except IndexError:
            em.description = 'No results.'
            return await ctx.send(embed=em)
        em.description = f'**Definition:** {res.definition}\n**Usage:** {res.example}\n**Votes:** {res.upvotes}:thumbsup:{res.downvotes}:thumbsdown:'
        await ctx.send(embed=em)