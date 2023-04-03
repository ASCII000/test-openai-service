import openai


def ask_gpt(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return answer

def image_generator(imagem):
    image1 = openai.Image.create(
    prompt=imagem,
    n=1,
    size="512x512"
    )
    image_url1 = image1['data'][0]['url']

    image2 = openai.Image.create(
    prompt=imagem,
    n=2,
    size="512x512"
    )
    image_url2 = image2['data'][0]['url']

    image3 = openai.Image.create(
    prompt=imagem,
    n=3,
    size="512x512"
    )
    image_url3 = image3['data'][0]['url']

    image4 = openai.Image.create(
    prompt=imagem,
    n=4,
    size="512x512"
    )
    image_url4 = image4['data'][0]['url']

    return [image_url1, image_url2, image_url3, image_url4]