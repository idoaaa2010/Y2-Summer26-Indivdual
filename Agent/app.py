import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "you are a general knowlage boss, when somone ask you a quastion you answer shortly and give a random fun fact about the"
    history = []

    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )

        reply = response.content[0].text
        print(f'Claude: {reply}')
        history.append({'role': 'assistant', 'content': reply})

run_chat()

#Its diffrent from using chatgpt because you get tottaly diffrent ai's only from a prompt in the code

#reflaction:
#1. its like a sport, you need to carry all the effort from before and continue it, and if you will not, you will lose progress.
#2 for me the AI rememberd clearly 
# no it didnt run, beacause the code didnt have the libary for part of its code
#the ai is responding a bit diffrent- dumer or smarter kind of
#3. one bug is that i didnt manage to install the pip install, and i fixed it by breaking the berier 