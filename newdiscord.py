import discord

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("botstart")
    game = discord.Game("?명령어 1호기")
    await client.change_presence(status=discord.Status.online, activity=game)


    @client.event
    async def on_message(message):
        if message.content.startswith("안녕!"):
            await message.channel.send("안녕하세요!")
        if message.content.startswith("?서버주소"):
            await message.channel.send("서버주소는 hrfarm.kro.kr입니다!")
        if message.content.startswith("ㅎㅇ"):
            await message.channel.send("어디서 반말이야")
        if message.content.startswith("?명령어"):
            await message.channel.send("현재 추가된 명령어는 안녕!, ?서버주소, ㅎㅇ, ?서버장, ?호랑봇, ?제작자 그리고 ?명령어입니다! 명령어는 계속 추가될 예정입니다!")
        if message.content.startswith("?호랑봇"):
            await message.channel.send("저는 밤하늘님이 만들어주신 호랑팜 서버 전용 봇입니다!")
        if message.content.startswith("?서버장"):
            await message.channel.send("이 서버의 주인장은 바로 HR 호랑님입니다!")
        if message.content.startswith("?제작자"):
            await message.channel.send("저를 만드신 분은 대단하신 밤하늘(NightSkyblue1)님입니다!")

client.run("NjY2NjA0NDMxOTQwMjU1NzQ0.Xqonew.Ai7m8lcx71zt6xyUsgw3f3Opuiw")