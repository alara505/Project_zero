from Project_Zero.data_access_layer.implementation_classes.account_dao_imp import AccountInfoImp
from Project_Zero.entities.account import Account

account_dao_imp = AccountInfoImp()
test_account = Account("test account", 0)
updated_account = Account("updated account", 2)


def test_create_account_success():
    created_account = account_dao_imp.create_account_entry(test_account)
    assert created_account.account_id != 0


def test_get_account_success():
    selected_account = account_dao_imp.get_account_information(1)
    assert selected_account.account_id == 1


def test_get_all_account_success():
    accounts = account_dao_imp.get_all_account_information()
    assert len(accounts) >= 2


def test_update_account_success():
    result = account_dao_imp.update_account_information(updated_account)
    assert result.account == "updated account"


def test_delete_account_success():
    result = account_dao_imp.delete_account_information(3)
    assert result
