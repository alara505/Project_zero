from Project_Zero.custom_execeptions.duplicate_account_name import DuplicateAccountNameException
from Project_Zero.custom_execeptions.account_does_not_exist import AccountDoesNotExistException
from Project_Zero.custom_execeptions.insufficient_currency import InsufficientCurrency
from Project_Zero.data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from Project_Zero.entities.account import Account
from Project_Zero.service_layer.abstract_services.account_service import AccountService


class AccountPostgresService(AccountService):
    def __init__(self, account_dao: AccountPostgresDAO):
        self.account_dao = account_dao

    def service_create_account(self, account: Account) -> Account:
        accounts = self.account_dao.get_all_account_information()
        for existing_account in accounts:
            if existing_account.account == account.account:
                raise DuplicateAccountNameException("You can not use that name: it is already taken!")
            else:
                return self.account_dao.create_account_entry(account)

    def service_get_account_by_id(self, account_id) -> Account:
        return self.account_dao.get_account_information(account_id)

    def service_get_all_account_information(self) -> list[Account]:
        return self.account_dao.get_all_account_information()

    # Add two methods into this to work with balance variable, and transfer later.
    def service_deposit_account_balance(self, account: Account) -> Account:
        accounts = self.account_dao.get_all_account_information()
        for existing_account in accounts:
            if existing_account.account_id == account.account_id:
                return self.account_dao.deposit_into_account_by_id(account)
        raise AccountDoesNotExistException("This account does not exist in our database.")

    def service_withdraw_account_balance(self, account) -> Account:
        accounts = self.account_dao.get_all_account_information()
        for account_to_withdraw in accounts:
            if account_to_withdraw.account_id == account.account_id:
                if account_to_withdraw.account == account.account:
                    if account_to_withdraw.balance - account.balance >= 0:
                        return self.account_dao.withdraw_from_account_by_id(account)
                    else:
                        raise InsufficientCurrency("You can not withdraw more than what you currently have!")
                else:
                    raise InsufficientCurrency("You can not withdraw more than what you currently have!")
        raise AccountDoesNotExistException("This account does not exist in our database.")

    def service_transfer_account_by_account_id(self, transfer_account: Account, receiver_account: Account,
                                               balance_transferred: float) -> Account:
        accounts = self.account_dao.get_all_account_information()
        for account in accounts:
            if account.account_id == transfer_account.account_id:
                if account.account_id == receiver_account.account_id:
                    if balance_transferred > transfer_account.balance:
                        raise InsufficientCurrency("You can not withdraw more than what you currently have!")
                    return self.account_dao.transfer_from_account_to_account_by_id(transfer_account, receiver_account,
                                                                                   balance_transferred)
                raise AccountDoesNotExistException("This account does not exist in our database.")

    # used the update customer function for the account for the variables for deposit, and withdraw.
    def service_update_account_information(self, account: Account) -> Account:
        accounts = self.account_dao.get_all_account_information()
        for current_account in accounts:
            if current_account.account_id != account.account_id:
                if current_account.account == account.account:
                    raise DuplicateAccountNameException("You can not use that name: it is already taken!")
        updated_account = self.account_dao.update_account_information(account)
        return updated_account

    def service_delete_account_information(self, account_id: int) -> bool:
        return self.account_dao.delete_account_information(account_id)
