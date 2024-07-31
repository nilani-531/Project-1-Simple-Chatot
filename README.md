SimpleChatbot

Description:
The SimpleChatbot class is a Python-based chatbot designed for interactive conversations. It can greet users, ask predefined questions, and respond to user inputs with set answers. The chatbot remembers user responses and maintains conversation context for a more engaging experience.

Features:
Greeting and Farewell:

greet(): Starts the conversation with a friendly greeting.
farewell(): Ends the conversation with a goodbye message.

Question Asking:
ask_question(): Asks questions from a predefined list based on the number of interactions, and can remember user answers.
Response Handling:
respond_to_input(user_input): Provides responses based on user input, including handling references to previously saved answers.
Context Management:
remember_context(user_input): Keeps track of user inputs and interactions.
Conversation Flow:
chat(): Manages the conversation, handles user inputs, asks questions, and provides responses. Ends when the user types "exit".

Installation
No installation is required. Simply ensure you have Python installed on your system.

Usage:
Clone the Repository:
git clone https://github.com/yourusername/Project1-SimpleChatbot.git
cd Project1-SimpleChatbot

Run the Chatbot:
python simple_chatbot.py
This will start the chatbot and prompt you to interact with it.
