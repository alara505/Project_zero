class Account:
    last_id = 0

    def __init__(self, account: str, account_id: int, balance: float):
        self.account = account
        self.account_id = account_id
        self.balance = balance

    def __str__(self):
        return "Account: {}, Id: {}, Balance: {}".format(self.account, self.account_id, self.balance) ,

    def make_account_dictionary(self):
        return {
            "account": self.account,
            "accountId": self.account_id,
            "balance": self.balance
        }
