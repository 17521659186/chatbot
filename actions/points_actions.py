#!/usr/bin/env python
# coding:utf-8
import random

from rasa.core.events import AllSlotsReset
from rasa_sdk import Action

from settings.messages import AVAILABLE_POINT_MSGS, EXPIREING_POINT_MSGS


class AvailablePointsQuery(Action):
    """可用积分查询"""

    def name(self):
        return 'available_points_query'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(AVAILABLE_POINT_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class ExpiringSoonPoints(Action):
    """即将过期积分查询"""

    def name(self):
        return 'expiring_soon_points'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(EXPIREING_POINT_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]
