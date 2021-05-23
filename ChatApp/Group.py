import json
from ChatApp.Message import *


class Group:
    """
    a chat between multiple users

    Attributes
    ----------
    Redis_Server : redis.Redis() : connection to redis server
    Group_ID : str : id of the group
    Group_Members : list<str> : list of user ids
    Messages : list<str> : list of message ids

    Methods
    ----------
    see below
    """

    def __init__(self):
        self.Redis_Server = redis.Redis()
        self.Group_ID, self.Group_Members, self.Messages = None, None, None

    ####################################################################################################################

    # methods to create or fetch a group

    def create_group(self, users):
        """
        function that creates a group and uploads the necessary data to redis db

        Parameters
        ----------
        users : list<str> : list of users that should be in the group

        Returns
        -------
        boolean --> True : if creation of group is a success
                    False : if group id already exists
        """
        self.Group_ID = generate_id("group")
        if self.Redis_Server.hget(self.Group_ID, "group_members") is None:
            self.Group_Members, self.Messages = users, []
            self.Redis_Server.hmset(self.Group_ID, {"group_members": json.dumps(self.Group_Members),
                                                    "messages": json.dumps(self.Messages)})
            return True
        return False

    def get_group(self, group_id):
        """
        function that fetches the attributes of a group by its id

        Parameters
        ----------
        group_id : str : id of the wanted group

        Returns
        -------
        boolean --> True : if fetching of the values is a success
                    False : if group with this group id does not exist
        """
        if self.Redis_Server.hget(group_id, "group_members") is not None:
            self.Group_ID = group_id
            self.Group_Members = json.loads(self.Redis_Server.hget(group_id, "group_members").decode("utf-8"))
            self.Messages = json.loads(self.Redis_Server.hget(group_id, "messages").decode("utf-8"))
            return True
        return False

    def update_group(self):
        """
        updates the list of messages
        """
        self.Messages = json.loads(self.Redis_Server.hget(self.Group_ID, "messages").decode("utf-8"))

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
        self.Redis_Server.hmset(self.Group_ID, {"messages": json.dumps(self.Messages)})

    def print_group(self):
        """
        create a list of all messages
        the elements of the list are strings that consist of the sender and the content

        Returns
        -------
        list<str> : list of all messages
        """
        self.update_group()
        message_list = []
        for message_id in self.Messages:
            message = Message()
            message.get_message(message_id)
            message_list.append(message.print_message())
        return message_list
