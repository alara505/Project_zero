from Project_Zero.data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from Project_Zero.entities.customer import Customer
from Project_Zero.service_layer.implementation_services.customer_postgres_service import CustomerPostgresService
from Project_Zero.custom_execeptions.duplicate_customer_account_number import DuplicateCustomerAccountNumberException

customer_dao = CustomerPostgresDAO()
customer_service = CustomerPostgresService(customer_dao)

customer_with_duplicate_account = Customer("first", "last", 157, 0, 1)


def test_catch_duplicate_account_number_for_create_method():
    try:
        customer_service.service_create_customer_entry(customer_with_duplicate_account)
        assert False
    except DuplicateCustomerAccountNumberException as e:
        assert str(e) == "Account number is already taken!"


def test_catch_duplicate_account_number_for_update_method():
    try:
        customer_service.service_update_customer_information(customer_with_duplicate_account)
        assert False
    except DuplicateCustomerAccountNumberException as e:
        assert str(e) == "Account number is already taken!"
