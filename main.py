import discord, json, openai
from discord.ext import commands
import openai_func as op


#INICIALIZAR
token, prefix, openai_token = '', '', ''
with open("config.json") as config:
    arr = json.loads(config.read())
    token , prefix, openai_token = arr['token'], arr['prefix'], arr['openai_key']

openai.api_key = openai_token
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

#INICIALIZAR
@bot.event
async def on_ready():
    print(f'O Client foi logado em: {bot.user}')
    print(f'Com a lantencia de: {bot.latency}')

    rich_presence = discord.Activity(name=' Os malês do mundo.', type=discord.ActivityType.listening)
    print(f'Login {bot.user}!')
    
    await bot.change_presence(status=discord.Status.online, activity=rich_presence)
    
    #SINCRONIZA OS COMANDOS SLASH
    try:
        synced = await bot.tree.sync()
        print(f"Comando sincronizados.")
    except Exception as e:
        print(e)
    else:
        print("Algo deu errado")

#COMANDOS PREFIXO

#COMANDO CHATGPT
@bot.command(name='chatgpt')
async def chatgpt(ctx, comando):
    resposta = op.ask_gpt(ctx.message.content)
    print(resposta)
    embed=discord.Embed(title="ChatGPT",
                        description=f"**R**: {resposta}", color=0x30df3b)
    embed.set_author(name="OpenAI",
                    icon_url="http://cruckz.com/wp-content/uploads/2023/01/chat-gpt-alternatives.jpg")
    embed.set_footer(text=f"{ctx.author.name}: {ctx.message.content}")
                
    await ctx.channel.send(embed=embed)

####### SLASH COMMANDS
#COMANDO CHATGPT

#COMANDO GERADOR DE IMG
@bot.tree.command(name='img', description='Contexto')
async def img(interaction: discord.Interaction, question: str):
    embed0 = discord.Embed()
    embed0.set_thumbnail(url='https://res.cloudinary.com/practicaldev/image/fetch/s--ypttW29q--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://i.imgur.com/j3IISku.gif')
    await interaction.response.send_message(embed=embed0, ephemeral=True)
    
    imagem = op.image_generator(question)

    embed1=discord.Embed(url="https://www.bing.com/create", description=f"AI: {question}",color=0x080707)
    embed1.set_author(name="OpenAI",
            icon_url="https://centralized.ai/content/images/2022/12/DALL-E.png")
    embed2 = discord.Embed(url="https://www.bing.com/create")
    embed3 = discord.Embed(url="https://www.bing.com/create")
    embed4 = discord.Embed(url="https://www.bing.com/create")
                
    embed1.set_image(url=f"{imagem[0]}")
    embed2.set_image(url=f"{imagem[1]}")
    embed3.set_image(url=f"{imagem[2]}")
    embed4.set_image(url=f"{imagem[3]}")

    await interaction.edit_original_response(embeds=[embed1, embed2, embed3, embed4])

#BEM VINDO
@bot.event
async def on_member_join(Member):
    mensagem = op.ask_gpt(
        'Faça uma mensagem de bem vindo para o grupo Mojagaum para o novo usuario ' + Member.name
        )

    if Member.bot:
        return
    embed=discord.Embed(
        title=f"Bem vindo(a) **{Member.name}**",
        description=f"{mensagem}\n\n**Desbloqueie o servidor:** <#884228840447152199>",
        color=0x2d80cd)
    embed.set_author(
        name="╭──MOJANGÃO──╮",
        icon_url="https://cdn.discordapp.com/icons/884223954233987083/82d72e11bfa07fd78afa6e486131a7de.png?size=2048")
    embed.set_thumbnail(
        url=f"{Member.avatar}")
    embed.set_image(url='https://media.tenor.com/PQgWghXKP0MAAAAC/games-eduuuu.gif')
    await bot.get_channel(884271494316830720).send(f'<@{Member.id}>',embed=embed)
    print(f'{Member} Se juntou')

#RUN
bot.run(token)