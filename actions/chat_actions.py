#!/usr/bin/env python
# coding:utf-8
import random
import json
import logging

from rasa_sdk import Action
from rasa.core.events import AllSlotsReset




from settings.messages import HI_MSGS, BYE_MSGS, THANKS_MSGS

logger = logging.getLogger(__name__)


class ChatAsyncAction(Action):
    """闲聊"""

    def name(self):
        return 'chat'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = "闲聊"
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class Greetings(Action):
    """打招呼"""

    def name(self):
        return 'greetings'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(HI_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class Bye(Action):
    """拜拜"""

    def name(self):
        return 'bye'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(BYE_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class Thanks(Action):
    """谢谢"""

    def name(self):
        return 'thanks'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(THANKS_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]




