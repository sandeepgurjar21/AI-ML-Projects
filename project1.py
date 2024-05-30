class SimpleChatbot:
    def __init__(self):
        self.context = {}
        self.responses = {
            "how are you": "I'm a chatbot, but I'm doing great! How about you?",
            "what is your name": "I am a simple chatbot created for this project.",
            "what can you do": "I can chat with you and remember our conversations.",
            "tell me a joke": "Why did the computer go to the doctor? Because it had a virus!",
            "thank you": "You're welcome!"
        }
        
    def greet(self):
        return "Hello! How can I assist you today?"

    def farewell(self):
        return "Goodbye! Have a great day!"

    def respond(self, user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return self.responses[user_input]
        elif any(user_input in response.lower() for response in self.context.values()):
            return f"You mentioned: {user_input}. How can I assist you further?"
        else:
            return self.handle_error()

    def ask_questions(self):
        questions = ["What is your name?","Do you like chatbots?", "How can I help you today?"]
        for question in questions:
            print(question)
            user_response = input()
            self.context[question] = user_response
            print(f"You answered: {user_response}")

    def handle_error(self):
        return "I'm sorry, I didn't catch that. Could you please rephrase?"

# Example usage:
simple_bot = SimpleChatbot()
print(simple_bot.greet())
simple_bot.ask_questions()

# Simulate a conversation
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print(simple_bot.farewell())
        break
    else:
        print("Bot:", simple_bot.respond(user_input))
