#!/usr/bin/env python
# coding:utf-8
import random

from rasa_sdk import Action

from rasa.core.events import AllSlotsReset

from settings.messages import MEMBER_REGISTER_MSGS, VERIFICATION_CODE_MSGS, MEMBER_LOGIN_MSGS


class MembersRegister(Action):
    """会员注册"""

    def name(self):
        return 'members_register'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(MEMBER_REGISTER_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class VerificationCode(Action):
    """验证码问题"""

    def name(self):
        return 'verification_code'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(VERIFICATION_CODE_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class MembersLogin(Action):
    """登录问题"""

    def name(self):
        return 'members_login'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(MEMBER_LOGIN_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]
