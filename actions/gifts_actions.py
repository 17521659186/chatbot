#!/usr/bin/env python
# coding:utf-8
import random

from rasa_sdk import Action
from rasa.core.events import AllSlotsReset



from settings.messages import GIFT_REDEMPTION_METHOD_MSGS, GIFT_REDEMPTION_TRANSFER_MSGS


class GiftRedemptionMethod(Action):
    """积分兑礼方法"""

    def name(self):
        return 'gift_redemption_method'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(GIFT_REDEMPTION_METHOD_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class GiftRedemptionTransfer(Action):
    """积分兑礼物流"""

    def name(self):
        return 'gift_redemption_transfer'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(GIFT_REDEMPTION_TRANSFER_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]
