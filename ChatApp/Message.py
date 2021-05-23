import redis
from datetime import datetime


class Message:
    """
    a message

    Attributes
    ----------
    Redis_Server : redis.Redis() : connection to redis server
    Message_ID : str : id of the message
    From : str : user id of the sender
    Content : str : message content

    Methods
    ----------
    see below
    """

    def __init__(self):
        self.Redis_Server = redis.Redis()
        self.Message_ID, self.From, self.Content = None, None, None

    ####################################################################################################################

    def create_message(self, user_id, content):
        """
        function that creates a new message

        Parameters
        ----------
        user_id : str : id of the user
        content : str : content of the message

        Returns
        -------
        boolean --> True : if message creation is a success
                    False : if message id already exists
        """
        self.Message_ID = generate_id("message")
        if self.Redis_Server.hget(self.Message_ID, "from") is None:
            self.From = user_id
            self.Content = content
            self.Redis_Server.hmset(self.Message_ID, {"from": self.From, "content": self.Content})
            return True
        return False

    def get_message(self, message_id):
        """
        function that fetches the messages attributes

        Parameters
        ----------
        message_id : str : id of the message

        Returns
        -------
        boolean --> True : if fetching was a success
                    False : if message id does not exist
        """
        if self.Redis_Server.hget(message_id, "from") is not None:
            self.Message_ID = message_id
            self.From = self.Redis_Server.hget(message_id, "from").decode("utf-8")
            self.Content = self.Redis_Server.hget(message_id, "content").decode("utf-8")
            return True
        return False

    ####################################################################################################################

    def print_message(self):
        """
        create an output string consisting of sender and content

        Returns
        -------
        str : message sender and content
        """
        printable_content = self.From + "\n\n" + self.Content + "\n\n"
        return printable_content


def generate_id(id_type):
    """
    create unique message id by usage of the current timestamp

    Returns
    -------
    str : id
    """
    return id_type + "-" + datetime.now().strftime("%d%b%Y-%H%M%S%f")
