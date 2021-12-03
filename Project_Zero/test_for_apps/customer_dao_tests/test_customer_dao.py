from Project_Zero.data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from Project_Zero.data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from Project_Zero.entities.customer import Customer

customer_info_imp = CustomerDAOImp()
customer = Customer("Test", "Customer", 103, 0, 1)


def test_create_customer_success():
    new_customer: Customer = customer_info_imp.create_customer_entry(customer)
    assert new_customer.customer_id != 0


def test_get_customer_success():
    returned_customer: Customer = customer_info_imp.get_customer_information(1)
    assert returned_customer.customer_id == 1


def test_get_all_customer_success():
    customer_list = customer_info_imp.get_all_customer_information()
    assert len(customer_list) >= 2


def test_update_customer_success():
    updated_info = Customer("changed by", "update customer method", 202, 2, 2)
    updated_customer: Customer = customer_info_imp.update_customer_information(updated_info)
    assert updated_customer.customer_id == updated_info.customer_id


def test_delete_customer_success():
    confirm_customer_deleted = customer_info_imp.delete_customer_information(2)
    assert confirm_customer_deleted
