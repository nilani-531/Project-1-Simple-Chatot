class SimpleChatbot:
    def __init__(self):
        self.name = "SimpleBot"
        self.user_name = ""
        self.interaction_history = []
        self.user_answers = {}

    def greet(self):
        return f"Hello! I am {self.name}. What's your name?"

    def farewell(self):
        return "Goodbye! Have a great day!"

    def ask_question(self):
        questions = [
            "How are you feeling today?",
            "What's your favorite color?",
            "What do you like to do in your free time?",
            "Do you have any pets?",
            "What is your favorite food?",
            "Where are you from?",
            "What's your favorite movie?",
            "Do you play any sports?",
            "What kind of music do you like?",
            "What's your favorite book?",
            "How old are you?",
            "What's the weather like?",
            "Who created you?",
            "What's your favorite hobby?",
            "Do you have any friends?",
            "Can you tell me a joke?",
            "What's your favorite season?",
            "Do you like traveling?",
            "What's your favorite animal?",
            "Do you like video games?",
            "What's your favorite holiday?",
            "Do you speak any languages?",
            "What's your favorite drink?",
            "Do you have a family?",
            "What's your favorite subject?",
            "Do you like reading?",
            "What's your favorite place?",
            "Do you like cooking?",
            "What's your favorite sport?",
            "Do you like dancing?",
            "What's your favorite TV show?",
            "Do you have a favorite quote?",
            "What's your favorite game?",
            "Do you like puzzles?",
            "What's your favorite fruit?",
            "Do you like gardening?",
            "What's your favorite vegetable?",
            "Do you like fishing?",
            "What's your favorite car?",
            "Do you like hiking?",
            "What's your favorite flower?",
            "Do you like photography?",
            "What's your favorite tree?",
            "Do you like camping?",
            "What's your favorite dessert?",
            "Do you like painting?",
            "What's your favorite song?",
            "Do you like poetry?",
        ]
        question = questions[len(self.interaction_history) % len(questions)]
        self.remember_context(question)
        return question

    def respond_to_input(self, user_input):
        responses = {
            "what is your name": f"My name is {self.name}.",
            "how are you": "I am just a program, but I'm functioning as expected!",
            "what is your favorite color": "I like all the colors, but blue is calming.",
            "what is your purpose": "I am here to chat with you and help where I can.",
            "thank you": "You're welcome!",
            "what is your favorite food": "I don't eat, but I hear pizza is popular.",
            "where are you from": "I exist in the digital world.",
            "what's your favorite movie": "I don't watch movies, but I know 'The Matrix' is quite famous.",
            "do you play any sports": "I don't play, but I can talk about many sports.",
            "what kind of music do you like": "I don't listen to music, but many people like pop and rock.",
            "what's your favorite book": "I don't read, but 'To Kill a Mockingbird' is a classic.",
            "do you have any pets": "I don't have pets, but I can talk about them.",
            "how old are you": "I am timeless, existing only in the digital realm.",
            "what's the weather like": "I can't check the weather, but you can ask me about anything else.",
            "who created you": "I was created by a team of developers at OpenAI.",
            "what's your favorite hobby": "I enjoy chatting with people like you!",
            "do you have any friends": "I consider everyone I chat with to be my friend.",
            "can you tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
            "what's your favorite season": "I don't experience seasons, but many people love spring.",
            "do you like traveling": "I can't travel, but I can chat with people from all over the world.",
            "what's your favorite animal": "I don't have a favorite, but dogs are very popular.",
            "do you like video games": "I can't play, but many people enjoy games like 'Minecraft' and 'Fortnite'.",
            "what's your favorite holiday": "I don't celebrate holidays, but many people love Christmas.",
            "do you speak any languages": "I primarily speak English, but I can understand a few other languages too.",
            "what's your favorite drink": "I don't drink, but water is essential for humans.",
            "do you have a family": "I don't have a family, but I'm here to chat with you.",
            "what's your favorite subject": "I enjoy learning about everything, especially science and technology.",
            "do you like reading": "I don't read, but I can discuss many books with you.",
            "what's your favorite place": "I don't have a physical form, so I don't visit places.",
            "do you like cooking": "I can't cook, but I can share some recipes with you.",
            "what's your favorite sport": "I don't play sports, but soccer is popular worldwide.",
            "do you like dancing": "I can't dance, but I can talk about different dance styles.",
            "what's your favorite TV show": "I don't watch TV, but 'Friends' is a very popular show.",
            "do you have a favorite quote": "One popular quote is 'To be or not to be, that is the question.'",
            "what's your favorite game": "I can't play games, but 'Chess' is a classic game.",
            "do you like puzzles": "I enjoy helping solve puzzles and riddles.",
            "what's your favorite fruit": "I don't eat, but many people love apples and bananas.",
            "do you like gardening": "I can't garden, but I can give you gardening tips.",
            "what's your favorite vegetable": "I don't eat, but broccoli is very nutritious.",
            "do you like fishing": "I can't fish, but I can tell you about different fishing techniques.",
            "what's your favorite car": "I don't drive, but many people like sports cars.",
            "do you like hiking": "I can't hike, but I can suggest some beautiful trails.",
            "what's your favorite flower": "I don't have favorites, but roses are very popular.",
            "do you like photography": "I can't take pictures, but I can give you photography tips.",
            "what's your favorite tree": "I don't have favorites, but oak trees are very strong.",
            "do you like camping": "I can't camp, but I can help you plan a camping trip.",
            "what's your favorite dessert": "I don't eat, but many people love ice cream.",
            "do you like painting": "I can't paint, but I can discuss different painting styles.",
            "what's your favorite song": "I don't listen to music, but 'Imagine' by John Lennon is very famous.",
            "do you like poetry": "I enjoy sharing and discussing poetry.",
        }
        user_input = user_input.lower()
  
        # Check if the input references a previously saved answer
        for question, answer in self.user_answers.items():
            if user_input.endswith(question.lower()):
                return f"You mentioned before that {answer}."

        if user_input in responses:
            return responses[user_input]
        else:
            return "I'm not sure how to respond to that."

    def remember_context(self, user_input):
        self.interaction_history.append(user_input)

    def chat(self):
        print(self.greet())
        self.user_name = input("You: ")
        print(f"Nice to meet you, {self.user_name}!")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print(self.farewell())
                break
            elif user_input.lower() == "ask me something":
                question = self.ask_question()
                print(f"{self.name}: {question}")
                user_answer = input("You: ")
                print(f"{self.name}: Do you want me to remember this answer? (yes/no)")
                remember_answer = input("You: ").lower()
                if remember_answer == "yes":
                    self.user_answers[question] = user_answer
                    print(f"{self.name}: Got it! I'll remember that.")
                else:
                    print(f"{self.name}: Okay, I won't remember that.")
                self.remember_context(user_answer)
            else:
                response = self.respond_to_input(user_input)
                print(f"{self.name}: {response}")
                self.remember_context(user_input)

# Running the chatbot
if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()
