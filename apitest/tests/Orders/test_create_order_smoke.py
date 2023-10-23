import pytest
from apitest.src.dao.products_dao import ProductsDAO
from apitest.src.helpers.orders_helper import OrdersHelper
from apitest.src.helpers.customers_helper import CustomerHelper

@pytest.fixture(scope='module')
def orders_smoke_setup():
    product_dao = ProductsDAO()
    order_helper = OrdersHelper()

    # get a product from the db
    rand_product = product_dao.get_random_product_from_db(1)
    product_id = rand_product[0]['ID']

    info = {'product_id': product_id,
            'order_helper': order_helper}

    return info

@pytest.mark.orders
@pytest.mark.smoke
@pytest.mark.tcid48
def test_create_paid_order_guest_user(orders_smoke_setup):

    order_helper = orders_smoke_setup['order_helper']
    customer_id = 0
    product_id = orders_smoke_setup['product_id']

    # make the call
    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ]}
    order_json = order_helper.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)


@pytest.mark.orders
@pytest.mark.smoke
@pytest.mark.tcid49
def test_create_paid_order_new_created_customer(orders_smoke_setup):

    customer_helper = CustomerHelper()

    product_id = orders_smoke_setup['product_id']
    order_helper = orders_smoke_setup['order_helper']

    # make the call
    cust_info = customer_helper.create_customer()
    customer_id = cust_info['id']

    info = {"line_items": [
        {
            "product_id": product_id,
            "quantity": 1
        }
    ],
        "customer_id": customer_id
    }
    order_json = order_helper.create_order(additional_args=info)

    # verify response
    expected_products = [{'product_id': product_id}]
    order_helper.verify_order_is_created(order_json, customer_id, expected_products)
