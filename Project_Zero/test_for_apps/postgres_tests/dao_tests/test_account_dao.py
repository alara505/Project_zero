from Project_Zero.data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from Project_Zero.entities.account import Account

account_dao = AccountPostgresDAO()

new_account = Account("test team", 0, 100)
account_names = {"Jake"}
account_names.add("Sandy")
account_names.add("Fed")
account_names.add("Ale")

new_accounts = account_names.pop()
update_account = Account(new_accounts, 3, 0)

deleted_account = account_names.pop()
delete_account = Account(deleted_account, 0, 0)


def test_create_account_success():
    account_result = account_dao.create_account_entry(new_account)
    assert account_result.account_id != 0


def test_get_account_success():
    initial_team = account_dao.get_account_information(1)
    assert initial_team.account_id == 1


def test_get_all_account_success():
    accounts = account_dao.get_all_account_information()
    assert len(accounts) >= 3


def test_update_account_success():
    updated_account = account_dao.update_account_information(update_account)
    assert updated_account.account == new_accounts


def test_delete_account_success():
    to_be_deleted = account_dao.create_account_entry(delete_account)
    result = account_dao.delete_account_information(to_be_deleted.account_id)
    assert result
