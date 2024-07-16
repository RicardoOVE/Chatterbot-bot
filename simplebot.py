from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import collections.abc
collections.Hashable = collections.abc.Hashable

# Crear un ChatBot en español
chatbot = ChatBot('Ejemplo', read_only=True, language='spanish')

# Entrenar el chatbot con el corpus en español
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.spanish')

# Ejecución del chatbot
while True:
    try:
        user_input = input("Pregunta: ")
        response = chatbot.get_response(user_input)
        print("Chatbot: ", response)

    except KeyboardInterrupt:
        print("Saliendo...")
        break