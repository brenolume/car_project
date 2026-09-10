from xml.parsers.expat import model

from openai import OpenAI

client = OpenAI(
    api_key='API_KEY'
)

def get_car_ai_bio(model, brand, year):
    message = '''
    Monte uma descrição de venda para o carro {} - {} do ano {}. A descrição deve ser persuasiva, destacando os pontos fortes do carro e incentivando o comprador a entrar em contato para mais informações. A descrição deve ter no máximo 250 caracteres.
'''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages=[
            {
            "role": "user",
            "content": message
            }
        ],
        max_tokens=1000,
        model="gpt-3.5-turbo"
    )
    return response['choices'][0]['text']