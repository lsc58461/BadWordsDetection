import os
import discord
from Now_Time import Time
from word_detection import word_detection
Token = os.environ["Token"]

client = discord.Client()
a = word_detection()
a.load_data()
a.load_badword_data()


@client.event
async def on_ready():
    print(f"{Time()})---------------    CONNECTED    ---------------")
    print(f"{Time()})  봇 이름 : {client.user.name}")
    print(f"{Time()})  봇 ID : {client.user.id}")
    print(f"{Time()})-----------------------------------------------")


@client.event
async def on_message(message):
    word = str(message.content)
    a.input=word
    a.text_modification()
    a.lime_compare(a.token_badwords , a.token_detach_text[0], 0.9)
    result = a.result
    a.lime_compare(a.new_token_badwords , a.token_detach_text[1], 0.9 , True)
    result += a.result
    if len(result) == 0:
        return None
    for j in result:
            word = word[0:j[0]] + '-'*(j[1]-j[0]+1) + word[j[1]+1:]
    embed = discord.Embed(title = '' , color = 0xFF3636)
    embed.add_field(name='----------    필터링된 채팅    ----------', value = word)
    embed.set_author(name=str(message.author), icon_url=message.author.avatar_url)
    await message.channel.send('어머')
    await message.channel.send(embed = embed)
    await message.delete()
        
client.run(Token)