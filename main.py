import openai

with open('hidden.txt') as file:
    openai.api_key = file.read()

def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.completion.create(
            model='gpt-3.5-turbo',
            prompt=prompt,
            temperature=0.8,
            max_tokens=150,
            top_p=1,
            frequency_panalty=0,
            presence_panelty=0.5,
            stop=[' Human:', ' AI:']
        )

        choices: dict = response.get('choices')[0]
        text = choices.get('text')
        # print(response)
    except Exception as e:
        print('ERROR', e)
    return text
prompt = 'Hello there!'
print(get_api_response(prompt))