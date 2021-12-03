from flask import Flask, request, jsonify

from Project_Zero.custom_execeptions.insufficient_currency import InsufficientCurrency
from Project_Zero.custom_execeptions.duplicate_customer_account_number import DuplicateCustomerAccountNumberException
from Project_Zero.custom_execeptions.duplicate_account_name import DuplicateAccountNameException
from Project_Zero.custom_execeptions.account_does_not_exist import AccountDoesNotExistException
from Project_Zero.data_access_layer.implementation_classes.customer_dao_imp import CustomerDAOImp
from Project_Zero.data_access_layer.implementation_classes.account_dao_imp import AccountInfoImp
from Project_Zero.data_access_layer.implementation_classes.customer_postgres_dao import CustomerPostgresDAO
from Project_Zero.data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDAO
from Project_Zero.entities.customer import Customer
from Project_Zero.entities.account import Account
from Project_Zero.service_layer.implementation_services.customer_postgres_service import CustomerPostgresService
from Project_Zero.service_layer.implementation_services.account_postgres_service import AccountPostgresService
from Project_Zero.service_layer.implementation_services.customer_service_imp import CustomerServiceImp
from Project_Zero.service_layer.implementation_services.account_service_imp import AccountServiceImp

import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")
# there are a few different levels of logging going from the most inclusive to most exclusive:
# debug
# info
# warning
# error
# critical

app: Flask = Flask(__name__)

customer_info = CustomerPostgresDAO()  # CustomerDAOImp()
customer_service = CustomerPostgresService(customer_info)  # CustomerServiceImp(customer_info)
account_dao = AccountPostgresDAO()  # AccountInfoImp()
account_service = AccountPostgresService(account_dao)  # AccountServiceImp(account_dao)


@app.post("/customer")
def create_customer_entry():
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["accountNumber"],
            customer_data["customerId"],
            customer_data["accountId"]
        )
        customer_to_return = customer_service.service_create_customer_entry(new_customer)
        customer_as_dictionary = customer_to_return.make_customer_dictionary()
        customer_as_json = jsonify(customer_as_dictionary)
        return customer_as_json
    except DuplicateCustomerAccountNumberException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/customer/<customer_id>")
def get_customer_information(customer_id: str):
    result = customer_service.service_get_customer_information(int(customer_id))
    result_as_dictionary = result.make_customer_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json


@app.get("/customer/all")
def get_all_customer_information():
    customer_as_customers = customer_service.service_get_all_customer_information()
    customer_as_dictionary = []
    for customers in customer_as_customers:
        dictionary_customer = customers.make_customer_dictionary()
        customer_as_dictionary.append(dictionary_customer)
    return jsonify(customer_as_dictionary)


@app.patch("/customer/<customer_id>")
def update_customer_information(customer_id: str):
    try:
        customer_data = request.get_json()
        new_customer = Customer(
            customer_data["firstName"],
            customer_data["lastName"],
            customer_data["accountNumber"],
            int(customer_id),
            customer_data["accountId"]
        )
        updated_customer = customer_service.service_update_customer_information(new_customer)
        return "Customer updated successfully, the customer info is now " + str(updated_customer)
    except DuplicateCustomerAccountNumberException as e:
        return str(e)


@app.delete("/customer/<customer_id>")
def delete_customer_information(customer_id: str):
    result = customer_service.service_delete_customer_information(int(customer_id))
    if result:
        return "Customer with id {} was deleted successfully.".format(customer_id)
    else:
        return "Something went wrong: customer with id {} was not deleted".format(customer_id)


@app.post("/account")
def create_account():
    try:
        body = request.get_json()
        new_account = Account(
            body["account"],
            body["accountId"],
            body["balance"]
        )
        created_account = account_service.service_create_account(new_account)
        created_account_as_dictionary = created_account.make_account_dictionary()
        return jsonify(created_account_as_dictionary), 201
    except DuplicateAccountNameException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message), 400


@app.get("/account/<account_id>")
def get_account_by_id(account_id: str):
    account = account_service.service_get_account_by_id(int(account_id))
    account_as_dictionary = account.make_account_dictionary()
    return jsonify(account_as_dictionary), 200


@app.get("/account")
def get_all_accounts():
    accounts = account_service.service_get_all_account_information()
    accounts_as_dictionaries = []
    for account in accounts:
        dictionary_account = account.make_account_dictionary()
        accounts_as_dictionaries.append(dictionary_account)
    return jsonify(accounts_as_dictionaries), 200


@app.patch("/account/<customer_id>")
def update_account(customer_id: str):
    try:
        body = request.get_json()
        update_info = Account(
            body["account"],
            body["accountId"],
            body["balance"]
        )
        updated_customer = account_service.service_update_account_information(update_info)
        updated_customer_as_dictionary = updated_customer.make_account_dictionary()
        return jsonify(updated_customer_as_dictionary), 200
    except DuplicateAccountNameException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message)


@app.patch("/account/deposit/<account_id>")
def update_deposit_account(account_id: str):
    try:
        body = request.get_json()
        update_info = Account(
            body["account"],
            int(account_id),
            body["balance"]
        )
        updated_account = account_service.service_deposit_account_balance(update_info)
        updated_account_as_dictionary = updated_account.make_account_dictionary()
        return jsonify(updated_account_as_dictionary), 200
    except AccountDoesNotExistException as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message)


@app.patch("/account/withdraw/<account_id>")
def update_withdrawal_account(account_id: str):
    try:
        body = request.get_json()
        update_info = Account(
            body["account"],
            int(account_id),
            body["balance"]
        )
        updated_account = account_service.service_withdraw_account_balance(update_info)
        updated_account_as_dictionary = updated_account.make_account_dictionary()
        return jsonify(updated_account_as_dictionary), 200
    except InsufficientCurrency as e:
        error_message = {"errorMessage": str(e)}
        return jsonify(error_message)


@app.delete("/account/<account_id>")
def delete_account(account_id: str):
    result = account_service.service_delete_account_information(int(account_id))
    if result:
        return "Customer with id {} was deleted successfully.".format(account_id)
    else:
        return "Something went wrong: customer with id {} was not deleted".format(account_id)


app.run()
