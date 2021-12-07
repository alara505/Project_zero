from Project_Zero.custom_execeptions.duplicate_customer_account_number import DuplicateCustomerAccountNumberException
from Project_Zero.data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from Project_Zero.entities.customer import Customer
from Project_Zero.service_layer.abstract_services.customer_service import CustomerService


class CustomerPostgresService(CustomerService):
    def __init__(self, customer_dao: CustomerPostgresDAO):
        self.customer_dao = customer_dao

    def service_create_customer_entry(self, customer: Customer) -> Customer:
        customers = self.customer_dao.get_all_customer_information()
        for existing_customer in customers:
            if existing_customer.account_id == customer.account_id:
                if existing_customer.account_number == customer.account_number:
                    raise DuplicateCustomerAccountNumberException("Account number is already taken!")
        created_customer = self.customer_dao.create_customer_entry(customer)
        return created_customer

    # get player information
    def service_get_customer_information(self, customer_id) -> Customer:
        return self.customer_dao.get_customer_information(customer_id)

    # get the entire customer information, you must require list[class name] in order for it to pass the function
    def service_get_all_customer_information(self) -> list[Customer]:
        return self.customer_dao.get_all_customer_information()

    def service_update_customer_information(self, customer: Customer) -> Customer:
        customers = self.customer_dao.get_all_customer_information()
        for current_customer in customers:
            if current_customer.account_id == customer.account_id:
                if current_customer.customer_id != customer.customer_id:
                    if current_customer.account_number == customer.account_number:
                        raise DuplicateCustomerAccountNumberException("Account number is already taken!")
        updated_customer = self.customer_dao.update_customer_information(customer)
        return updated_customer

    def service_delete_customer_information(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_information(customer_id)
