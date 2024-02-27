from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

@api_view(['POST'])
def index(request):
    # chat = request.data['chat']
    # return Response({ "chat": chat })

    CORPUS_FILE = "chat.txt"

    chatbot = ChatBot("Chatpot")

    trainer = ListTrainer(chatbot)
    cleaned_corpus = clean_corpus(CORPUS_FILE)
    trainer.train(cleaned_corpus)

    exit_conditions = (":q", "quit", "exit")
    while True:
        # query = input("> ")
        query = request.data['chat']
        # print(query)
        if query in exit_conditions:
            break
        else:
            # Response({ chatbot.get_response(query) })

            print(f"🪴 {chatbot.get_response(query)}")


