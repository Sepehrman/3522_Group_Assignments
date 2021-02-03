class User:

    #SHOULD WE HAVE MANY USERS AS A LIST? Which includes parents too?
    def __init__(self, user_name, user_age, user_type, account_number,
                 bank_name, balance, budget):
        self._user_name = user_name
        self._user_age = user_age
        self.user_type = user_type
        self._account_number = account_number
        self._bank_name = bank_name
        self._balance = balance
        self._budget = budget

    @staticmethod
    def load_test_users():
        return User("Bruce Wayne", 10, "Student", 12345678, "Gotham Bank", 98.32,
                    {"Games and Entertainment": 30, "Clothing and Accessories": 20, "Eating Out": 18,
                     "Miscellaneous": 30.32})
