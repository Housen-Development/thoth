import datetime

from django.test import TestCase
from django.utils import timezone

from .models import PartsInOut


class PartsInOutModelTests(TestCase):

    def test_is_input_date_future_with_future_input(self):
        """
        is_input_date_future() returns True for input whose input_date
        is in the future.
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=1)
        future_input = PartsInOut(input_date=time)
        self.assertIs(future_input.is_input_date_future(), True)
