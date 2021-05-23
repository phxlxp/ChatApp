from ChatApp.Chat import *
from ChatApp.Group import *
from ChatApp.Message import *


class User:
    """
    a user

    Attributes
    ----------
    Redis_Server : redis.Redis() : connection to redis server
    User_ID : str : id of the user
    Password : str : password of the user
    Chats : list<str> : list of chat ids
    Chat_Partners : list<str> : list of names
    Groups : list<str> : list of group ids

    Methods
    ----------
    see below
    """

    def __init__(self):
        self.Redis_Server = redis.Redis()
        self.User_ID, self.Password = None, None
        self.Chats, self.Chat_Partners, self.Groups = [], [], []

    ####################################################################################################################

    # methods for creation/deletion of a user

    def create_user(self, user_id, password):
        """
        function that creates a new user

        Parameters
        ----------
        user_id : str : user id of the new user
        password : str : password for the new user

        Returns
        -------
        boolean --> True : if user creation was a success
                    False : if user id already exists
        """
        if self.Redis_Server.hget("users", user_id) is None:
            self.Redis_Server.hmset("users", {user_id: password})
            self.Redis_Server.hmset(user_id, {"chats": json.dumps([]), "groups": json.dumps([])})
            self.User_ID, self.Password = user_id, password
            return True
        return False

    def delete_user(self, user_id, password):
        """
        function that deletes a user if user id and password are correct
        HINT: functionality is currently not used

        Parameters
        ----------
        user_id : str : id of user
        password : str : password of user

        Returns
        -------
        boolean --> True : if deletion is a success
                    False : if password does not match the users password (get correct password by user id)
        """
        if self.User_ID == user_id and self.Password == password:
            self.Redis_Server.hdel("users", user_id)
            self.Redis_Server.hdel(user_id, "chats", "groups")
            self.User_ID, self.Password = None, None
            return True
        return False

    ####################################################################################################################

    # methods for login/logout

    def login(self, user_id, password):
        """
        user login

        Parameters
        ----------
        user_id : str : id of user
        password : str : password of user

        Returns
        -------
        boolean --> True : if login is a success
                    False : if password does not match the users password
        """
        if self.Redis_Server.hget("users", user_id) is not None and self.Redis_Server.hget("users", user_id).decode("utf-8") == password:
            self.User_ID = user_id
            self.Password = password
            return True
        return False

    def logout(self):
        """
        user logout (set the attributes to None)
        """
        self.User_ID, self.Password = None, None

    ####################################################################################################################

    # update attributes

    def update_user(self):
        """
        update the users attributes
        """
        self.Chats = json.loads(self.Redis_Server.hget(self.User_ID, "chats").decode("utf-8"))
        self.Groups = json.loads(self.Redis_Server.hget(self.User_ID, "groups").decode("utf-8"))
        self.Chat_Partners = []
        for chat_id in self.Chats:
            self.Chat_Partners.append(self.get_chat_partner(chat_id))

    ####################################################################################################################

    # chat specific methods

    def add_chat_partner(self, user_id):
        """
        add a new chat partner

        Parameters
        ----------
        user_id : str : user id of chat partner

        Returns
        -------
        boolean --> True : if there already is a chat with this user / adding a new chat partner is a success
                    False: if user id does not exist
        """
        if self.chat_exists(user_id):
            return True

        elif self.Redis_Server.hget("users", user_id) is not None:
            chat = Chat()
            chat.create_chat(self.User_ID, user_id)
            self.Chats.append(chat.Chat_ID)
            self.Redis_Server.hmset(self.User_ID, {"chats": json.dumps(self.Chats)})

            if user_id != self.User_ID:
                partner_chats = json.loads(self.Redis_Server.hget(user_id, "chats").decode("utf-8"))
                partner_chats.append(chat.Chat_ID)
                self.Redis_Server.hmset(user_id, {"chats": json.dumps(partner_chats)})

            return True

        else:
            return False

    def chat_exists(self, user_id):
        """
        checks whether chat with a user exists

        Parameters
        ----------
        user_id : str : id of the user

        Returns
        -------
        boolean --> False : if chat exists
        str : id of the chat
        """
        self.update_user()
        for chat_id in self.Chats:
            chat = Chat()
            chat.get_chat(chat_id)
            if chat.Chat_Partners == [user_id, self.User_ID] or chat.Chat_Partners == [self.User_ID, user_id]:
                return chat_id
        return False

    def get_chat_partner(self, chat_id):
        """
        get user id of the chat partner

        Parameters
        ----------
        chat_id : str : id of the chat

        Returns
        -------
        str : user id of the chat partner
        """
        chat = Chat()
        chat.get_chat(chat_id)
        if chat.Chat_Partners[0] == self.User_ID:
            return chat.Chat_Partners[1]
        else:
            return chat.Chat_Partners[0]

    ####################################################################################################################

    # group specific methods

    def check_user_exists(self, user_id):
        """
        check whether there is a user with a explicit user id

        Parameters
        ----------
        user_id : str : user id to check

        Returns
        -------
        boolean : existence of the user
        """
        return self.Redis_Server.hget("users", user_id) is not None

    def create_group(self, users):
        """
        create a new group

        Parameters
        ----------
        users : list<str> : list of user ids (of users that should be in the group)
        """
        group = Group()
        if self.User_ID not in users:
            users.append(self.User_ID)
        group.create_group(users)

        for user_id in users:
            groups = json.loads(self.Redis_Server.hget(user_id, "groups").decode("utf-8"))
            groups.append(group.Group_ID)
            self.Redis_Server.hmset(user_id, {"groups": json.dumps(groups)})

    def get_group_members(self, group_id):
        """
        returns the user ids of the group members

        Parameters
        ----------
        group_id : str : id of group

        Returns
        -------
        list<str> : list of user ids
        """
        group = Group()
        group.get_group(group_id)
        members = ""
        for member in group.Group_Members:
            if member != group.Group_Members[len(group.Group_Members)-1]:
                members += member + ", "
            else:
                members += member
        return members

    ####################################################################################################################

    # methods for message handling

    def send_message(self, id_param, content):
        """
        send a message to a chat or a group

        Parameters
        ----------
        id_param : str : id of the chat or the group
        content : str : message content
        """
        message = Message()
        message.create_message(self.User_ID, content)
        if "chat" in id_param:
            chat = Chat()
            chat.get_chat(id_param)
            chat.add_message(message.Message_ID)
        else:
            group = Group()
            group.get_group(id_param)
            group.add_message(message.Message_ID)

    def print_messages(self, id_param):
        """
        creates the message output of the chat or the group

        Parameters
        ----------
        id_param : str : id of the chat or the group

        Returns
        -------
        list<str> : list of messages
        """
        if "chat" in id_param:
            chat = Chat()
            chat.get_chat(id_param)
            return chat.print_chat()
        else:
            group = Group()
            group.get_group(id_param)
            return group.print_group()
