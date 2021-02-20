# from user import User
# from abc import ABC
#
#
# class Angel(User):
#     def __init__(self, user_name, user_age, account_number, bank_name, balance, budget):
#         super().__init__(user_name, user_age, account_number, bank_name, balance, budget)
#         self._spending_limit = 0.9
#
#     def get_warning_message(self):
#         pass
#
#
# class Rebel(User):
#     def __init__(self, user_name, user_age, account_number, bank_name, balance, budget):
#         super().__init__(user_name, user_age, account_number, bank_name, balance, budget)
#         self._limit_rate = 0.5
#
# class TroubleMaker(User):
#     def __init__(self, is_locked, user_name, user_age, account_number, bank_name, balance, budget):
#         super().__init__(user_name, user_age, account_number, bank_name, balance, budget)
#         self._spending_limit = 0.75
