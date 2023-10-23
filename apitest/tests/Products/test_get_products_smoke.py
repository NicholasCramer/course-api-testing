import pytest
import logging as logger
from apitest.src.utilities.requestsUtility import RequestsUtility

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid24
def test_get_all_products():
    req_helper = RequestsUtility()
    rs_api = req_helper.get('products')

    assert rs_api, f"Request to get all products returned nothing."
