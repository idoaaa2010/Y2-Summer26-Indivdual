import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "you are a general knowlage boss, when somone ask you a quastion you answer shortly and give a random fun fact about the same topic, dont show your thinking."
    history = []
    #count = 0
    
    while True:
        user_input = input('>> ')

        if user_input.lower() == 'exit':
            break
        
        history.append({'role': 'user', 'content': user_input})
       # count += 1
        #if count >= 3:
          #  print('History:', history)
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )
        ##print(response)
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

#lab2
#output_tokens = the tokens used for the ai to give an output 
#input_tokans = the tokans we use to get an ai response 

#it stoped mid answer 

#it gives diffrent answers

#it takes longer to response and give more acurate answers

#it changes the thinking time and the acurecy of the response 

#because to get contaxt the ai need to ree the entire chat

# electricity and water bills 

# they wiil change with the prompt itself and the history wont affect it

#he wont know what he answered

#nothing changes, just the output 

#none