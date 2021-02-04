class User:

    #SHOULD WE HAVE MANY USERS AS A LIST? Which includes parents too?
    def __init__(self, user_name, user_age, account_number,
                 bank_name, balance, budget):
        self._user_name = user_name
        self._user_age = user_age
        self._account_number = account_number
        self._bank_name = bank_name
        self._balance = balance
        self._budget = budget

    @staticmethod
    def load_test_user():
        return User("Bruce Wayne", 10, 12345678, "Gotham Bank", 98.32,
                    {"Games and Entertainment": 30, "Clothing and Accessories": 20, "Eating Out": 18,
                     "Miscellaneous": 30.32})

    def __repr__(self):
        return f"User(user_name: {self._user_name}, user_age: {self._user_age}, " \
               f"account_number: {self._account_number}," \
               f" bank_name: {self._bank_name}, balance: {self._balance}, budget: {self._budget}"

def main():
    user = User.load_test_user()
    print(user)


if __name__ == '__main__':
    main()
