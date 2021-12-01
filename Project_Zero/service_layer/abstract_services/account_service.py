from abc import ABC, abstractmethod
from typing import List

from Project_Zero.entities.account import Account


class AccountService(ABC):

    # create customer method
    @abstractmethod
    def service_create_account(self, account: Account) -> Account:
        pass

    # get player information
    @abstractmethod
    def service_get_account_by_id(self, account_id) -> Account:
        pass

    # get the entire customer information, you must require list[class name] in order for it to pass the function
    @abstractmethod
    def service_get_all_account_information(self) -> list[Account]:
        pass

    @abstractmethod
    def service_update_account_information(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_delete_account_information(self, account_id: int) -> bool:
        pass