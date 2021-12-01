from typing import List

from Project_Zero.data_access_layer.abstract_classes.account_dao import AccountInfo
from Project_Zero.entities.account import Account


class AccountInfoImp(AccountInfo):
    account_one = Account("first account", 1)
    account_two = Account("second account", 2)
    account_three = Account("to be deleted", 3)
    account_four = Account("duplicate name", 4)
    account_list = [account_one, account_two, account_three, account_four]
    account_id_gen = 5

    # For Customer and Account for creating them.
    def create_account_entry(self, account: Account) -> Account:
        new_account = account
        new_account.account_id = AccountInfoImp.account_id_gen
        AccountInfoImp.account_id_gen += 1
        AccountInfoImp.account_list.append(new_account)
        return new_account

    # Account and Customer ID
    def get_account_information(self, account_id: int) -> Account:
        for account in AccountInfoImp.account_list:
            if account.account_id == account_id:
                return account

    # Customer function and Account
    def get_all_account_information(self) -> list[Account]:
        return AccountInfoImp.account_list

    # Customer function
    def update_account_information(self, account: Account) -> Account:
        for account_in_list in AccountInfoImp.account_list:
            if account_in_list.account_id == account.account_id:
                account_in_list.account = account.account
                return account_in_list

    # This will represent for Customer and Account
    def delete_account_information(self, account_id: int) -> bool:
        for account in AccountInfoImp.account_list:
            if account.account_id == account_id:
                index = AccountInfoImp.account_list.index(account)
                del AccountInfoImp.account_list[index]
                return True
