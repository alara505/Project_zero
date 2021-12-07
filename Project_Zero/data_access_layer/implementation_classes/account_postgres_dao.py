from typing import List

from Project_Zero.data_access_layer.abstract_classes.account_dao import AccountInfo
from Project_Zero.entities.account import Account
from Project_Zero.util.database_connection import connection


# Make sure to add another code for balance id.
class AccountPostgresDAO(AccountInfo):

    def create_account_entry(self, account: Account) -> Account:
        sql = "insert into account values(%s, default, %s) returning account_id"
        cursor = connection.cursor()
        cursor.execute(sql, [account.account, account.balance])
        connection.commit()
        generated_id = cursor.fetchone()[0]
        account.account_id = generated_id
        return account

    def get_account_information(self, account_id) -> Account:
        sql = "select * from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        account_record = cursor.fetchone()
        account = Account(*account_record)
        return account

    def get_all_account_information(self) -> list[Account]:
        sql = "select * from account"
        cursor = connection.cursor()
        cursor.execute(sql)
        account_record = cursor.fetchall()
        accounts = []
        for account in account_record:
            accounts.append(Account(*account))
        return accounts

    def deposit_into_account_by_id(self, account: Account) -> Account:
        sql = "select balance from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account.account_id])
        balance = cursor.fetchone()[0]
        account.balance += balance

        sql = "update account set balance = %s where account_id = %s returning balance"
        cursor.execute(sql, (account.balance, account.account_id))
        connection.commit()
        return account

    def withdraw_from_account_by_id(self, account: Account) -> Account:
        sql = "select balance from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account.account_id])
        balance = cursor.fetchone()[0]
        new_balance = balance - account.balance

        sql = "update account set balance = %s where account_id = %s returning balance"
        cursor.execute(sql, (new_balance, account.account_id))
        account.balance = cursor.fetchone()[0]
        connection.commit()
        return account

    def transfer_from_account_to_account_by_id(self, transfer_account: Account, received_account: Account,
                                               balance_transfer: float) -> Account:
        sql = "select balance from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [transfer_account.account_id])
        transfer_account_balance = cursor.fetchone()[0]

        sql = "select balance from account where account_id = %s"
        cursor.execute(sql, [received_account.account_id])
        received_account_bal = cursor.fetchone()[0]
        received_account_bal += balance_transfer
        transfer_account_balance = balance_transfer - transfer_account_balance

        sql = "update account set balance = %s where account_id = %s returning balance"
        cursor.execute(sql, (received_account_bal, received_account.account_id))

        sql = "update account set balance %s where account_id = %s returning balance"
        cursor.execute(sql, (transfer_account_balance, transfer_account.account_id))
        connection.commit()
        return self.transfer_from_account_to_account_by_id(transfer_account, received_account, balance_transfer)

    def update_account_information(self, account: Account) -> Account:
        sql = "update account set account = %s, balance = %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account, account.balance, account.account_id))
        connection.commit()
        return account

    def delete_account_information(self, account_id: int) -> bool:
        sql = "delete from account where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
        return True
