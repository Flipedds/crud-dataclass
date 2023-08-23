from classes.User import User
from classes.ListOfUsers import ListOfUsers
from typing import List

def test_creating_a_new_user_in_list():
    user = User('Filipe', 19, '06/03/2004')
    new_list = ListOfUsers()
    result = new_list.insert_user(user)

    assert 'User added in the list !' == result

def test_failing_creating_a_new_user_in_list():
    user = 1
    new_list = ListOfUsers()
    result = new_list.insert_user(user)

    assert 'Not a user, could not add in list !' == result

def test_removing_a_user_in_list():
    user = User('Filipe', 19, '06/03/2004')
    new_list = ListOfUsers()
    new_list.insert_user(user)
    result = new_list.remove_user(0) # remove a partir do index do usuário

    assert 'User 0 removed !' == result


def test_failing_removing_a_user_in_list():
    user = User('Filipe', 19, '06/03/2004')
    new_list = ListOfUsers()
    new_list.insert_user(user)
    result = new_list.remove_user(1) # remove a partir do index do usuário

    assert "User don't exists" == result

def test_showing_the_list_of_users():
    user = User('Filipe', 19, '06/03/2004')
    other_user = User('André', 19, '06/03/2004')
    new_list = ListOfUsers()
    new_list.insert_user(user)
    new_list.insert_user(other_user)
    result = new_list.show_users()
    assert isinstance(result, List) == True

def test_failing_showing_the_list_of_users_is_empty():
    new_list = ListOfUsers()
    result = new_list.show_users()
    assert 'The list is empty !' == result