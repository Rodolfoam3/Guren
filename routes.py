
from dashcord import route

@route("/")
async def index(bot, request):
    """The url path is defined within the @route decorator"""
    if request.method == "GET":
        guilds = len(bot.guilds)
        
        return bot.dashboard.render_html("index.html", guilds=guilds)
    
    else:
        json = await request.json()
        
        channel = bot.get_channel()
        await channel.send("We just made a POST request with the data: `{}`".format(str(json)))
        
        return bot.dashboard.render_html("index.html", guilds=guilds)
