import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.utils.utils import *

class TestE2ECD(object):
    @allure.title("E2E - Create Booking ->Delete(Verify)")
    @allure.description("Test to verify Create Booking Id is successful and also user should able to delete")
    @pytest.mark.positivetestcase
    def test_create_booking_id_and_delete(self,get_booking_id,create_token):
        booking = get_booking_id
        token = create_token
        print(booking,token)
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking)
        response = delete_requests(
            url=delete_url,
            auth=None,
            headers=Utils().common_header_put_delete_patch_cookie(token=token),
            in_json=False
        )
        verify_http_status_code(response_data=response,expected_data=201)
        verify_response_delete(response=response.text)
        print(response.text)

