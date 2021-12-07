from Project_Zero.data_access_layer.abstract_classes.customer_dao import CustomerDAO
from Project_Zero.util.database_connection import connection
from Project_Zero.entities.customer import Customer


class CustomerPostgresDAO(CustomerDAO):
    # we will use %s as placeholders for our values
    def create_customer_entry(self, customer: Customer) -> Customer:
        sql = "insert into customer values(%s, %s, %s, default, %s) returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.account_number, customer.account_id))
        connection.commit()
        customer_id = cursor.fetchone()[0]
        customer.customer_id = customer_id
        return customer

    # get player information

    def get_customer_information(self, customer_id: int) -> Customer:
        sql = "select * from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        customer_record = cursor.fetchone()
        customer = Customer(*customer_record)
        return customer

    # get the entire customer information, you must require list[class name] in order for it to pass the function

    def get_all_customer_information(self) -> list[Customer]:
        sql = "select * from customer"
        cursor = connection.cursor()
        cursor.execute(sql)
        customer_records = cursor.fetchall()
        customer_list = []
        for customer in customer_records:
            customer_list.append(Customer(*customer))
        return customer_list

    def update_customer_information(self, customer: Customer) -> Customer:
        sql = "update customer set first_name = %s, last_name = %s, account_number = %s, account_id = %s where " \
              "customer_id = %s "
        cursor = connection.cursor()
        cursor.execute(sql, (customer.first_name, customer.last_name, customer.account_number, customer.account_id, customer.customer_id))
        connection.commit()
        return customer

    def delete_customer_information(self, customer_id: int) -> bool:
        sql = "delete from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        return True
