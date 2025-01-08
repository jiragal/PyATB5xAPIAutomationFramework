import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import *

class TestClass(object):
    @allure.title("E2E - Create Booking -> patch")
    @allure.description("Test to verify user is able to create Booking and then patch the data")
    @pytest.mark.positivetestcase
    def test_create_id_patch_id(self,create_token,get_booking_id):
        booking_id=get_booking_id
        token = create_token
        print(token, booking_id,sep=' ', end='=')
        patch_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = patch_requests(
            url=patch_url,
            auth=None,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            payload=payload_patch_booking_id(),
            in_json=False
        )
        verify_http_status_code(response_data=response,expected_data=200)
        assert response.json()["firstname"] == "James"
        assert response.json()["lastname"] == "Anaveer"
