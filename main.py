from dotenv import load_dotenv

import os
import g4f

load_dotenv()

open_api=os.getenv('OPENAI_KEY')  

TOKEN=os.getenv('TG_BOT_TOKEN')

print(open_api)
print(TOKEN)         # run python main.py

# Set with provider
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    provider=g4f.Provider.DeepAi,
    messages=[{"role": "user", "content": "Where is Tajmahal Located"}],    # write question and python main.py 
    stream=True,                                                            # during execution 
)

for message in response:
    print(message)