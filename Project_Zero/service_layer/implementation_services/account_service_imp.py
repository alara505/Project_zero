from typing import List

from Project_Zero.custom_execeptions.duplicate_account_name import DuplicateAccountNameException
from Project_Zero.data_access_layer.implementation_classes.account_dao_imp import AccountInfoImp
from Project_Zero.entities.account import Account
from Project_Zero.service_layer.abstract_services.account_service import AccountService


class AccountServiceImp(AccountService):

    def __init__(self, account_dao: AccountInfoImp):
        self.account_dao = account_dao

    def service_create_account(self, account: Account) -> Account:
        for existing_account in self.account_dao.account_list:
            if existing_account.account == account.account:
                raise DuplicateAccountNameException("You can not use that name: it is already taken!")
        new_account = self.account_dao.create_account_entry(account)
        return new_account

    def service_get_account_by_id(self, account_id) -> Account:
        return self.account_dao.get_account_information(account_id)

    def service_get_all_account_information(self) -> list[Account]:
        return self.account_dao.get_all_account_information()

    def service_update_account_information(self, account: Account) -> Account:
        for existing_account in self.account_dao.account_list:
            if existing_account.account_id != account.account_id:
                if existing_account.account == account.account:
                    raise DuplicateAccountNameException("You can not use that name: it is already taken!")
        updated_account = self.account_dao.update_account_information(account)
        return updated_account

    def service_delete_account_information(self, account_id: int) -> bool:
        return self.account_dao.delete_account_information(account_id)
