import pytest
from apitest.src.utilities.requestsUtility import RequestsUtility
from apitest.src.dao.products_dao import ProductsDAO
from apitest.src.helpers.products_helper import ProductsHelper

pytestmark = [pytest.mark.products, pytest.mark.smoke]

@pytest.mark.tcid25
def test_get_product_by_id():

    # get a product from db
    rand_product = ProductsDAO().get_random_product_from_db(1)
    rand_product_id = rand_product[0]['ID']
    db_name = rand_product[0]['post_title']
    db_product_id = rand_product_id

    # make the call
    product_helper = ProductsHelper()
    rs_api = product_helper.get_product_by_id(rand_product_id)
    api_name = rs_api['name']
    api_product_id = rs_api['id']

    # verify the response
    assert db_name == api_name, f"Get product by id returned wrong product name: " \
                                f"Db name: {db_name}. Api name: {api_name}"
    assert db_product_id == api_product_id, f"Get product id returned wrong product Id: " \
                                            f"Db Id: {db_product_id}, Api Id: {api_product_id}"
