# !/usr/bin/env python
# coding:utf-8
import random

from rasa.core.events import AllSlotsReset
from rasa_sdk import Action


from settings.messages import STORE_QUERY_MSGS, CERTIFIED_SOURCE_MSGS, ACTIVITY_CONSULTATION_MSGS, \
    LETTERING_SERVICE_MSGS, PROMOTION_CODE_MSGS, JOINT_AGENT_MSGS, COMPLAINTFILING_MSGS


class StoresQuery(Action):
    """门店查询"""

    def name(self):
        return 'stores_query'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(STORE_QUERY_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class CertifiedSourceQuery(Action):
    """正品渠道咨询"""

    def name(self):
        return 'certified_source_query'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(CERTIFIED_SOURCE_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class ActivityConsultation(Action):
    """活动咨询"""

    def name(self):
        return 'activity_consultation'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(ACTIVITY_CONSULTATION_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class LetteringService(Action):
    """刻字服务"""

    def name(self):
        return 'lettering_service'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(LETTERING_SERVICE_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class PromotionCode(Action):
    """促销代码"""

    def name(self):
        return 'promotion_code'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(PROMOTION_CODE_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class JointAgentQuery(Action):
    """加盟代理"""

    def name(self):
        return 'joint_agent_query'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(JOINT_AGENT_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]


class ComplaintFiling(Action):
    """投诉"""

    def name(self):
        return 'complaint_filing'

    def is_async(self):
        return False

    def run(self, dispatcher, tracker, domain):
        msg = random.choice(COMPLAINTFILING_MSGS)
        dispatcher.utter_message(msg)
        return [AllSlotsReset()]
