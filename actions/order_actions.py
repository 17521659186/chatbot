#!/usr/bin/env python
# coding:utf-8
import random

from rasa_sdk import Action
from rasa.core.events import AllSlotsReset

from settings.messages import ORDER_QUERY_MSGS, ORDER_CANCEL_MSGS, ORDER_TRANSFER_MSGS, ORDER_RERURN_MSGS


class OrderQuery(Action):
    """订单查询"""

    def name(self):
        return 'order_query'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(ORDER_QUERY_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class OrderCacel(Action):
    """订单取消"""

    def name(self):
        return 'order_cancel'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(ORDER_CANCEL_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class OrderTransfer(Action):
    """订单物流"""

    def name(self):
        return 'order_transfer'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(ORDER_TRANSFER_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class OrderReturn(Action):
    """订单退换货"""

    def name(self):
        return 'order_return'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(ORDER_RERURN_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]
