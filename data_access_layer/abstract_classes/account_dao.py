from abc import ABC, abstractmethod
from Project_Zero.entities.account import Account


class AccountInfo(ABC):

    # create customer method
    @abstractmethod
    def create_account_entry(self, account: Account) -> Account:
        pass

    # get player information
    @abstractmethod
    def get_account_information(self, account_id) -> Account:
        pass

    # get the entire customer information, you must require list[class name] in order for it to pass the function
    @abstractmethod
    def get_all_account_information(self) -> list[Account]:
        pass

    @abstractmethod
    def update_account_information(self, account: Account) -> Account:
        pass

    @abstractmethod
    def delete_account_information(self, account_id: int) -> bool:
        pass
