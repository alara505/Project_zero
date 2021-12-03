from abc import ABC, abstractmethod
from Project_Zero.entities.customer import Customer


class CustomerDAO(ABC):

    # create customer method
    @abstractmethod
    def create_customer_entry(self, customer: Customer) -> Customer:
        pass

    # get player information
    @abstractmethod
    def get_customer_information(self, customer_id) -> Customer:
        pass

    # get the entire customer information, you must require list[class name] in order for it to pass the function
    @abstractmethod
    def get_all_customer_information(self) -> list[Customer]:
        pass

    @abstractmethod
    def update_customer_information(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_customer_information(self,customer_id: int) -> bool:
        pass
