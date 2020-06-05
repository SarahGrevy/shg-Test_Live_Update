
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class MyPage(Page):
    form_model = 'group'
    form_fields = ['highest_bidder', 'highest_bid']
page_sequence = [MyPage]