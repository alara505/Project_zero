from Project_Zero.custom_execeptions.duplicate_customer_account_number import DuplicateCustomerAccountNumberException
from Project_Zero.data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from Project_Zero.entities.customer import Customer
from Project_Zero.service_layer.implementation_services.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)
customer = Customer("service", "testing", 101, 1, 0)
customer_update = Customer("update", "test", 101, 2, 0)


def test_validate_create_customer_method():
    try:
        customer_service.service_create_customer_entry(customer)
        assert False
    except DuplicateCustomerAccountNumberException as e:
        assert str(e) == "Account number is already taken!"


def test_validate_update_customer_method():
    try:
        customer_service.service_update_customer_information(customer_update)
        assert False
    except DuplicateCustomerAccountNumberException as e:
        assert str(e) == "Account number is already taken!"
