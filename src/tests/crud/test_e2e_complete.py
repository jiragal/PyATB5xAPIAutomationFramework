import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import *

import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Utils


class TestE2E(object):

    @allure.title("E2E - Create Booking -> Update -> Delete(Verify)")
    @allure.description(
        "Verify that created booking id when we update we are able to update it and delete it also | Full CRUD")
    @allure.testcase(url="https://bugz.atlassian.net/browse/BUG-1", name="E2ETC1")
    def test_update_booking_with_id_token(self, create_token, get_booking_id):
        print(create_token, get_booking_id)

