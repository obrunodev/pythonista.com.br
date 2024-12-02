from decouple import config
from openai import OpenAI

client = OpenAI(api_key=config('OPENAI_API_KEY'))

gpt_models = ['gpt-4', 'gpt-4o-mini', 'gpt-4-32k', 'gpt-4-32k-0613', 'gpt-4-0613', 'gpt-4-0314', 'gpt-4-32k-0314']

def get_chat_completion(messages, model='gpt-4o-mini'):
    if model in gpt_models:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
        )
        return response.choices[0].message.content


def get_chat_completion_stream(messages, model='gpt-4o-mini'):
    if model in gpt_models:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )
        return response.choices[0].message.content
