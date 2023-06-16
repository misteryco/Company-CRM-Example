# import random
#
# from crm_for_companies.fixtures.factory import UsersFactory, CompanyFactory, EmployeeFactory, UserModel
#
# USERS_TO_CREATE = 10
# COMPANIES_TO_CREATE = 5
# EMPLOYEES_TO_CREATE = 50
#
# UsersFactory.create_batch(10)
#
# for c in range(COMPANIES_TO_CREATE):
#     CompanyFactory.create(owner=random.choices(UserModel.objects.all(), k=3))
#
# EmployeeFactory.create_batch(EMPLOYEES_TO_CREATE)
