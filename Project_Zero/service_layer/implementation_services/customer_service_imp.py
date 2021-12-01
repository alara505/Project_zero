from Project_Zero.custom_execeptions.duplicate_customer_account_number import DuplicateCustomerAccountNumberException
from Project_Zero.data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from Project_Zero.entities.customer import Customer
from Project_Zero.service_layer.abstract_services.customer_service import CustomerService


class CustomerServiceImp(CustomerService):
    def __init__(self, customer_dao):
        self.customer_dao: CustomerDAOImp = customer_dao

    def service_create_customer_entry(self, customer: Customer) -> Customer:
        # need to implement business logic to our program
        for current_customer in self.customer_dao.customer_list:
            if current_customer.account_id == customer.account_id and current_customer.account_number == customer.account_number:
                raise DuplicateCustomerAccountNumberException("Account number is already taken!")
            else:
                return self.customer_dao.create_customer_entry(customer)

    def service_get_customer_information(self, customer_id: int) -> Customer:
        return self.customer_dao.get_customer_information(customer_id)

    def service_get_all_customer_information(self) -> list[Customer]:
        return self.customer_dao.get_all_customer_information()

    def service_update_customer_information(self, customer: Customer) -> Customer:
        for current_customer in self.customer_dao.customer_list:
            if current_customer.account_id == customer.account_id:
                if current_customer.customer_id != customer.customer_id:
                    if current_customer.account_number == customer.account_number:
                        raise DuplicateCustomerAccountNumberException("Account number is already taken!")
        return self.customer_dao.update_customer_information(customer)
        # for current_customer in self.customer_dao.customer_list:
        #     if current_customer.account_id == customer.account_id:
        #         if current_customer.customer_id != customer.customer_id:
        #             if current_customer.account_number == customer.account_number:
        #                 raise DuplicateCustomerAccountNumberException("Account number is already taken!")
        # return self.customer_dao.update_customer_information(customer)

    def service_delete_customer_information(self, customer_id: int) -> bool:
        return self.customer_dao.delete_customer_information(customer_id)
