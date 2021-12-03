from Project_Zero.data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from Project_Zero.entities.customer import Customer

customer_dao = CustomerPostgresDAO()
customer: Customer = Customer("first", "last", 101, 0, 1)

# random generator for names
random_names = {"Jorge"}
random_names.add("Sally")
random_names.add("George")
random_names.add("Lupe")

random_name = random_names.pop()
update_customer = Customer(random_name, "customer", 157, 6, 1)
customer_to_delete = Customer(random_names.pop(), random_names.pop(), 0, 0, 1)


def test_create_customer_success():
    created_customer = customer_dao.create_customer_entry(customer)
    assert created_customer.customer_id != 0


def test_get_customer_success():
    alex_lara = customer_dao.get_customer_information(1)
    assert alex_lara.first_name == "Alex" and alex_lara.last_name == "Lara"


def test_get_all_customer_success():
    customers = customer_dao.get_all_customer_information()
    assert len(customers) > 2


# This one is still causing minor errors, because of the table name(I think)
def test_update_customer_success():
    updated_customer = customer_dao.update_customer_information(update_customer)
    assert updated_customer.first_name == random_name


def test_delete_customer_success():
    customer_to_be_deleted = customer_dao.create_customer_entry(customer_to_delete)
    result = customer_dao.delete_customer_information(customer_to_be_deleted.customer_id)
    assert result
