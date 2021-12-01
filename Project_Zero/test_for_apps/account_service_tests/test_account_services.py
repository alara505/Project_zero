from Project_Zero.custom_execeptions.duplicate_account_name import DuplicateAccountNameException
from Project_Zero.data_access_layer.implementation_classes.account_dao_imp import AccountInfoImp
from Project_Zero.entities.account import Account
from Project_Zero.service_layer.implementation_services.account_service_imp import AccountServiceImp

account_dao = AccountInfoImp()
account_service = AccountServiceImp(account_dao)

bad_account = Account("duplicate name", 0)
bad_update_account = Account("duplicate name", 1)


def test_catch_creating_account_with_duplicate_name():
    try:
        account_service.service_create_account(bad_account)
        assert False
    except DuplicateAccountNameException as e:
        assert str(e) == "You can not use that name: it is already taken!"


def test_catch_updating_account_with_duplicate_name():
    try:
        account_service.service_update_account_information(bad_update_account)
        assert False
    except DuplicateAccountNameException as e:
        assert str(e) == "You can not use that name: it is already taken!"
