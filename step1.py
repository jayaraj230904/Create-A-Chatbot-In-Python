# Import the modules
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# Create a chatbot
chatbot = ChatBot("MyChatBot")
# Create a trainer
trainer = ListTrainer(chatbot)
# Train the chatbot on some sample conversations
trainer.train([
"Hi",
"Hello",
"How are you?",
"I'm fine, thank you.",
"What is your name?",
"My name is MyChatBot.",
"Nice to meet you.",
"Nice to meet you too."
])
# Start a conversation with the chatbot
while True:
user_input = input("You: ")
if user_input.lower() == "quit":
break
response = chatbot.get_response(user_input)
print("ChatBot: ", response)
