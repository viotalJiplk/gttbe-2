import urllib.parse
from config import discord

def endpoint_url(state, prompt="consent"):
    scope = "identify"
    state = urllib.parse.quote(state, safe='')
    # redir_url_urlencoded = urllib.parse.quote(discord["redir_url"], safe='')
    return "https://discord.com/oauth2/authorize?response_type=code&client_id="+str(discord["client_id"])+"&scope="+ scope +"&state="+ state +"&prompt=" + prompt
