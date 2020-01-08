#!/usr/bin/env python
# coding:utf-8
import logging
import random
from rasa.core.events import AllSlotsReset
from rasa_sdk import Action


from settings.messages import MEMBERS_QUERY_MSGS, MEMBERS_LVL_EXPIRATION_MSGS, MEMBERS_RIGHT_MSGS, \
    MEMBERS_PROMOTION_MSGS, MEMBERS_INFO_UPDATE_MSGS, MEMBERS_BIND_MSGS

_logger = logging.getLogger(__name__)


class MembersQuery(Action):
    """会员等级"""

    def name(self):
        return 'members_query'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(MEMBERS_QUERY_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class MembersLvlExpiration(Action):
    """会员等级到期时间"""

    def name(self):
        return 'members_lvl_expiration'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(MEMBERS_LVL_EXPIRATION_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class MembersRights(Action):
    """会员福利"""

    def name(self):
        return 'members_rights'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(MEMBERS_RIGHT_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class MembersPromotion(Action):
    """会员升级条件"""

    def name(self):
        return 'members_promotion'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(MEMBERS_PROMOTION_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class MembersInfoUpdate(Action):
    """修改会员信息"""

    def name(self):
        return 'members_info_update'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(MEMBERS_INFO_UPDATE_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class MembersBind(Action):
    """会员绑定"""

    def name(self):
        return 'members_bind'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(MEMBERS_BIND_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]
