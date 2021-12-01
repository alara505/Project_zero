from Project_Zero.data_access_layer.abstract_classes.customer_dao import CustomerDAO
from Project_Zero.entities.customer import Customer


class CustomerDAOImp(CustomerDAO):
    premade_customer = Customer("Premade", "Customer", 101, 1, 0)
    premade_customer_two = Customer("added for", "get all customer test", 102, 2, 1)
    to_delete = Customer("I exist", "to be deleted", 103, 3, 2)

    customer_list = [premade_customer, premade_customer_two, to_delete]

    customer_id_gen = 4

    # For Customer and Account for creating them.
    def create_customer_entry(self, customer: Customer) -> Customer:
        customer.customer_id = CustomerDAOImp.customer_id_gen
        CustomerDAOImp.customer_id_gen += 1
        CustomerDAOImp.customer_list.append(customer)
        return customer

    # Account and Customer ID
    def get_customer_information(self, customer_id: int) -> Customer:
        for customer in CustomerDAOImp.customer_list:
            if customer.customer_id == customer_id:
                return customer

    # Customer function and Account
    def get_all_customer_information(self) -> list[Customer]:
        return CustomerDAOImp.customer_list

    # Customer function
    def update_customer_information(self, customer: Customer) -> Customer:
        for customer_in_list in CustomerDAOImp.customer_list:
            if customer_in_list.customer_id == customer.customer_id:
                index = CustomerDAOImp.customer_list.index(customer_in_list)
                CustomerDAOImp.customer_list[index] = customer
                return customer

    # This will represent for Customer and Account
    def delete_customer_information(self, customer_id: int) -> bool:
        for customer_in_list in CustomerDAOImp.customer_list:
            if customer_in_list.customer_id == customer_id:
                index = CustomerDAOImp.customer_list.index(customer_in_list)
                del CustomerDAOImp.customer_list[index]
                return bool
