# run this file to perform the pytest

from ChatApp import User, Chat, Group, Message

########################################################################################################################

""" test user methods """

# data needed for the user tests
user_id = "pytest"
pwd = "pytest"
user = User.User()


# test user creation
def test_create_user():
    print("Test user creation...")
    result = user.create_user(user_id, pwd)
    assert result


# test user creation (user id already exists)
def test_double_create_user():
    print("Test double user creation...")
    result = user.create_user(user_id, pwd)
    assert not result


# test user existence
def test_check_user():
    print("Test user existence...")
    result = user.check_user_exists(user_id)
    assert result


# test user login
def test_user_login():
    print("Test user login...")
    result = user.login(user_id, pwd)
    assert result


# test chat creation (integrated)
def test_integrated_chat_creation():
    print("Test chat creation (integrated)...")
    result = user.add_chat_partner(user_id)
    assert result


# test check existence
def test_chat_exists():
    print("Test chat existence...")
    result = user.chat_exists(user_id)
    assert result


# test chat partner fetching
def test_get_chat_partner():
    print("Test chat partner fetching...")
    result = user.get_chat_partner(user.Chats[0])
    assert result == user_id


# test user deletion
def test_delete_user():
    print("Test user deletion...")
    result = user.delete_user(user_id, pwd)
    assert result


# test user login (user does not exist)
def test_false_user_login():
    print("Test false login...")
    result = user.login(user_id, pwd)
    assert not result


########################################################################################################################

""" test message methods """

# data needed for the message, chat and group tests
user1, user2 = User.User(), User.User()
user_id1, user_id2 = "pytest1", "pytest2"
pwd = "pytest"
user1.create_user(user_id1, pwd)
user2.create_user(user_id2, pwd)
message = Message.Message()


# test message creation
def test_message_creation():
    print("Test message creation...")
    result = message.create_message(user_id1, "pytest")
    assert result


# test printing message
def test_message_print():
    print("Test printing message...")
    result = message.print_message()
    assert result == user_id1 + "\n\npytest\n\n"


########################################################################################################################

""" test chat methods """

chat = Chat.Chat()


# test chat creation
def test_chat_creation():
    print("Test chat creation...")
    result = chat.create_chat(user_id1, user_id2)
    assert result


# test chat messages (integrated)
def test_chat_messages():
    print("Test chat messages (integrated)...")
    chat.add_message(message.Message_ID)
    result = chat.print_chat()
    assert result == [message.print_message()]


########################################################################################################################

""" test group methods """

group = Group.Group()


# test group creation
def test_group_creation():
    print("Test group creation...")
    result = group.create_group([user_id1, user_id2])
    assert result


# test group messages (integrated)
def test_group_messages():
    print("Test group messages (integrated)...")
    group.add_message(message.Message_ID)
    result = group.print_group()
    assert result == [message.print_message()]


# delete test users
user1.delete_user(user_id1, pwd)
user2.delete_user(user_id2, pwd)
