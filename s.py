import discord
import openai


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
openai.api_key = "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"

@client.event
async def on_ready():
    print(f'O Client foi logado em: {client.user}')
    print(f'Com a lantencia de: {client.latency}')

    rich_presence = discord.Activity(name=' os pecados de Erik', type=discord.ActivityType.listening)
    print(f'Login {client.user}!')
    
    await client.change_presence(status=discord.Status.idle, activity=rich_presence)

@client.event
async def on_message(message):
    mensagem = str(message.content.replace('&', '').lower())[8:]

    if message.author == client.user:
        return
    
    if message.content.startswith('&'):
        comando = message.content.replace('&', '').lower().split()[0]
        print(f"Novo comando utilizado: {comando}")
        match comando:
            case 'olá':
                await message.channel.send('Bom dia meu nobre')

            case 'ping':
                ping = str((str(client.latency).split('.'))[1])[:3]
                await message.channel.send(f'{ping} MS')

            case 'calcular':
                await message.channel.send("Calculo não ti vira aí burro.")

            case 'chatgpt':
                
                ### MENSAGEM EMBED ###
                resposta = ask_gpt(mensagem +' resuma em uma frase')
                embed=discord.Embed(title="ChatGPT",
                                    description=f"{resposta}", color=0x30df3b)
                embed.set_author(name="OpenAI",
                        icon_url="http://cruckz.com/wp-content/uploads/2023/01/chat-gpt-alternatives.jpg")
                #######################
                
                await message.channel.send(embed=embed)

            case 'fazimgs':
                embed0 = discord.Embed()
                embed0.set_thumbnail(url='https://res.cloudinary.com/practicaldev/image/fetch/s--ypttW29q--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.imgur.com/j3IISku.gif')
                
                msg = await message.channel.send(embed=embed0)

                imagem = image_generator(mensagem)

                embed1=discord.Embed(url="https://www.bing.com/create", description=f"AI: {mensagem}",color=0x080707)
                embed1.set_author(name="OpenAI",
                        icon_url="https://centralized.ai/content/images/2022/12/DALL-E.png")
                embed2 = discord.Embed(url="https://www.bing.com/create")
                embed3 = discord.Embed(url="https://www.bing.com/create")
                embed4 = discord.Embed(url="https://www.bing.com/create")
                
                embed1.set_image(url=f"{imagem[0]}")
                embed2.set_image(url=f"{imagem[1]}")
                embed3.set_image(url=f"{imagem[2]}")
                embed4.set_image(url=f"{imagem[3]}")

                await msg.edit(embeds=[embed1, embed2, embed3, embed4])

@client.event
async def on_member_join(Member):
    if Member.bot:
        return
    embed=discord.Embed(
        title=f"**Bem vindo(a) ao servidor** {Member.name}!",
        description=f"<@{Member.id}> Para desbloquear o servidor vá para o chat <#884228840447152199>",
        color=0x2d80cd)
    embed.set_author(
        name="╭──MOJANGÃO──╮",
        icon_url="https://cdn.discordapp.com/icons/884223954233987083/82d72e11bfa07fd78afa6e486131a7de.png?size=2048")
    embed.set_thumbnail(
        url=f"{Member.avatar}")
    embed.set_image(url='https://media.tenor.com/PQgWghXKP0MAAAAC/games-eduuuu.gif')
    
    await client.get_channel(884271494316830720).send(embed=embed)
    print(f'{Member} Se juntou')

client.run('MTA4ODgzMzIwMDYzMTA2Njc0Ng.G5pIdC.T1lL6VkMeoAKT8pASoOfRmUa2_U7uJ_9v29Vec')
#client.run('MTA4OTMxMzY1OTIyODAwNDQ5Mg.GCKCsd.vT4YdX-YFamV5WHvkhxiQsfn5OSwo8bb3Oh0yU')
