# OpenAI API

Um bot simples feito para a plataforma de comunicação Discord para usar comandos da API openai.
>Feito nas bibliotecas discord.py e OpenAI.

## Comandos
Os comandos serão chamados via text-box da plataforma.

### Slash
```
/chatgpt (pergunta)
```
![exemple1](https://media.discordapp.net/attachments/1089276079329521856/1092449167772749864/image.png)
```
/img (parâmetro)
```
![exemple2](https://cdn.discordapp.com/attachments/1089276079329521856/1092449433393844436/image.png)

### Por prefixo.
```
&chatgpt (pergunta)
&img (parâmetro)
```
## Dependências
### Discord Python
Utilizado para conectar a aplicação com a API do discord, necessario para criar a aplicação e gerar seu token, disponivel em [Discord Developers](https://discord.com/developers)

> - pip install discord.py

### OpenAI
Necessario para as interações de criação de respostas HTTP da api gratuita da OpenAI, necessario para gerar o token de liberação de uso da api, disponivel em [Openai API](https://openai.com/blog/openai-api)

> - pip install openai

### Arquivo de config
O seu arquivo de config.json deve se parecer com isso.

```
{
    'token':'seu_token_discord'
    'openai_key':'sua_key_openai'
    'prefix':'prefixo_desejado'
}
```

# Em breve
1. Fazer um sistema para importar quaisquer comandos build-in python para o bot.
  - 1.1 Organizar o README github para melhor entendimento.
2. Converter o bot para sistema handler para mais interações.
3. Lançar uma previa publica do bot

©r4n_emerson
