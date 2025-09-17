from discord.ext import commands
import aiohttp

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        """Fetches a random joke from the API."""
        url = f"https://jokeapi.dev/joke/Any?safe-mode"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    await ctx.send("Something went wrong.")
                    return
                data = await response.json()

                # Handle different joke types
                if data.get('type') == 'single':
                    # Single joke format
                    joke = data.get('joke')
                    if joke:
                        await ctx.send(joke)
                    else:
                        await ctx.send("Something went wrong.")
                elif data.get('type') == 'twopart':
                    # Two-part joke format
                    setup = data.get('setup')
                    delivery = data.get('delivery')
                    if setup and delivery:
                        await ctx.send(f"{setup}\n{delivery}")
                    else:
                        await ctx.send("Something went wrong.")
                else:
                    await ctx.send("Something went wrong.")

async def setup(bot):
    await bot.add_cog(Fun(bot))