from crm_for_companies.fixtures.factory import *
UsersFactory.create_batch(10)
for c in range(5):
    CompanyFactory.create(owner=random.choices(UserModel.objects.all(), k=3))
# # In above row k describes amount of owners per company
EmployeeFactory.create_batch(30)
# =====================================