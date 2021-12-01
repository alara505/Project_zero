class Account:
    last_id = 0

    def __init__(self, account: str, account_id: int):
        self.account = account
        self.account_id = account_id

    def __str__(self):
        return "Account: {}, Id: {}".format(self.account, self.account_id)

    def make_account_dictionary(self):
        return {
            "account": self.account,
            "accountId": self.account_id,
        }
