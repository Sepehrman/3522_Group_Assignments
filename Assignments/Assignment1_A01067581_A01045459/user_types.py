# from user import User
# from abc import ABC
#
# 
# class Angel(User):
#     def __init__(self, user_name, user_age, account_number, bank_name, balance, budget):
#         super().__init__(user_name, user_age, account_number, bank_name, balance, budget)
#         self._spending_limit = 0.9
#
#     # self._category_name = category_name
#     # self._budget_limit = budget_limit
#     # self._is_locked = is_locked
#     # self._current_spent = current_spent
#     # self._budget_count = budget_limit - current_spent
#     # self._transactions = transactions
#
#     def get_warning_message(self, budget_category):
#         percentile = budget_category._budget_count * self._spending_limit
#         if budget_category._current_spent > percentile and budget_category._budget_li
#
#
# class Rebel(User):
#     def __init__(self, user_name, user_age, account_number, bank_name, balance, budget):
#         super().__init__(user_name, user_age, account_number, bank_name, balance, budget)
#         self._limit_rate = 0.5
#
#
# class TroubleMaker(User):
#     def __init__(self, is_locked, user_name, user_age, account_number, bank_name, balance, budget):
#         super().__init__(user_name, user_age, account_number, bank_name, balance, budget)
#         self._spending_limit = 0.75
