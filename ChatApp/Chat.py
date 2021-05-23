import json
from ChatApp.Message import *


class Chat:
    """
    a chat between two users

    Attributes
    ----------
    Redis_Server : redis.Redis() : connection to redis server
    Chat_ID : str : id of the chat
    Chat_Partners : list<str> : list of user ids
    Messages : list<str> : list of message ids

    Methods
    ----------
    see below
    """

    def __init__(self):
        self.Redis_Server = redis.Redis()
        self.Chat_ID, self.Chat_Partners, self.Messages = None, None, None

    ####################################################################################################################

    # methods to create or fetch a chat

    def create_chat(self, user_id1, user_id2):
        """
        function that creates a chat and uploads the necessary data to redis db

        Parameters
        ----------
        user_id1 : str : id chat partner 1
        user_id2 : str : id chat partner 2

        Returns
        -------
        boolean --> True : if creation of chat is a success
                    False : if chat id already exists
        """
        self.Chat_ID = generate_id("chat")
        if self.Redis_Server.hget(self.Chat_ID, "chat_partners") is None:
            self.Chat_Partners, self.Messages = [user_id1, user_id2], []
            self.Redis_Server.hmset(self.Chat_ID, {"chat_partners": json.dumps(self.Chat_Partners),
                                                   "messages": json.dumps(self.Messages)})
            return True
        return False

    def get_chat(self, chat_id):
        """
        function that fetches the attributes of a chat by its id

        Parameters
        ----------
        chat_id : str : id of the wanted chat

        Returns
        -------
        boolean --> True : if fetching of the values is a success
                    False : if chat with this chat_id does not exist
        """
        if self.Redis_Server.hget(chat_id, "chat_partners") is not None:
            self.Chat_ID = chat_id
            self.Chat_Partners = json.loads(self.Redis_Server.hget(chat_id, "chat_partners").decode("utf-8"))
            self.Messages = json.loads(self.Redis_Server.hget(chat_id, "messages").decode("utf-8"))
            return True
        return False

    def update_chat(self):
        """
        updates the list of messages
        """
        self.Messages = json.loads(self.Redis_Server.hget(self.Chat_ID, "messages").decode("utf-8"))

    ####################################################################################################################

    # methods for message handling

    def add_message(self, message_id):
        """
        add new id to the list of messages

        Parameters
        ----------
        message_id : str : id of the new message
        """
        self.Messages.append(message_id)
        self.Redis_Server.hmset(self.Chat_ID, {"messages": json.dumps(self.Messages)})

    def print_chat(self):
        """
        create a list of all messages
        the elements of the list are strings that consist of the sender and the content

        Returns
        -------
        list<str> : list of all messages
        """
        self.update_chat()
        message_list = []
        for message_id in self.Messages:
            message = Message()
            message.get_message(message_id)
            message_list.append(message.print_message())
        return message_list
