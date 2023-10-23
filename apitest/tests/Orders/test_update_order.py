from apitest.src.helpers.orders_helper import OrdersHelper
from apitest.src.utilities.wooAPIUtility import WooAPIUtility
from apitest.src.utilities.genericUtilities import generate_random_string
import pytest

pytestmark = [pytest.mark.orders, pytest.mark.regression]


@pytest.mark.parametrize("new_status",
                         [
                             pytest.param('cancelled', marks=[pytest.mark.tcid55, pytest.mark.smoke]),
                             pytest.param('completed', marks=pytest.mark.tcid56),
                             pytest.param('on-hold', marks=pytest.mark.tcid57)
                         ])
def test_update_order_status(new_status):

    # Create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    cur_status = order_json['status']
    assert cur_status != new_status, f"Current status of order is already {new_status}. Unable to run test."

    # update the status
    order_id = order_json['id']
    payload = {"status": new_status}
    order_helper.call_update_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_order(order_id)

    # verify the new order status is what we updated
    assert new_order_info['status'] == new_status, f"Updated order status to {new_status}, " \
        f"but order is still {new_order_info['status']}"

# negative test case (validating all allowed statuses)


@pytest.mark.tcid58
def test_update_order_status_to_random_string():

    new_status = 'abcdefg'

    # Create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    # update the status
    payload = {"status": new_status}
    rs_api = WooAPIUtility().put(f'orders/{order_id}', params=payload, expected_status_code=400)

    assert rs_api['code'] == 'rest_invalid_param', f"Update order status to random string did not have " \
        f"correct code in response. Expected: 'rest_invalid_param'" \
        f"Actual: {rs_api['code']}."
    assert rs_api['message'] == "Invalid parameter(s): status", \
        f"string did not have correct message in response. " \
        f"Expected: 'rest_invalid_param', Actual: {rs_api['message']}"


@pytest.mark.tcid59
def test_update_order_customer_note():
    # Create new order
    order_helper = OrdersHelper()
    order_json = order_helper.create_order()
    order_id = order_json['id']

    # update the customer note
    random_note = generate_random_string(40)
    payload = {'customer_note': random_note}
    order_helper.call_update_order(order_id, payload)

    # get order information
    new_order_info = order_helper.call_retrieve_order(order_id)
    assert new_order_info['customer_note'] == random_note, f"Update order's customer note field failed. " \
        f"Expected value: {random_note}, Actual value: {new_order_info['customer_note']}"
