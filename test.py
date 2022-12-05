from revChatGPT.revChatGPT import Chatbot

import json 

# import secret.json as config
config = json.load(open('secret.json'))

chatbot = Chatbot(config, conversation_id=None)
chatbot.reset_chat() # Forgets conversation
chatbot.refresh_session() # Uses the session_token to get a new bearer token

prompt = "Hello how are you?"

resp = chatbot.get_chat_response(prompt, output="text") # Sends a request to the API and returns the response by OpenAI
print(resp)
# resp['message'] # The message sent by the response
# resp['conversation_id'] # The current conversation id
# resp['parent_id'] # The ID of the response

# print(resp['message'])
# headers = {
#   "Authorization":
# }

# response = requests.post(
#     "https://chat.openai.com/backend-api/conversation",
#     headers=headers, 
#     data={}, 
#     stream=True) # This returns a stream of text (live update)

# for line in response: # You have to loop through the response stream
#         print(line['message']) # Same format as text return type
#         ...