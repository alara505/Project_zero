from Project_Zero.custom_execeptions.duplicate_account_name import DuplicateAccountNameException
from Project_Zero.data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from Project_Zero.service_layer.implementation_services.account_postgres_service import AccountPostgresService
from Project_Zero.entities.account import Account

account_dao = AccountPostgresDAO()
account_service = AccountPostgresService(account_dao)

# Balance table column to keep track of the database
account_with_duplicate_name = Account("Initial Account", 1, 0)


def test_catch_duplicate_account_number_for_create_method():
    try:
        account_service.service_create_account(account_with_duplicate_name)
        assert False
    except DuplicateAccountNameException as e:
        assert str(e) == "You can not use that name: it is already taken!"


def test_catch_duplicate_account_number_for_update_method():
    try:
        account_service.service_update_account_information(account_with_duplicate_name)
        assert False
    except DuplicateAccountNameException as e:
        assert str(e) == "You can not use that name: it is already taken!"
