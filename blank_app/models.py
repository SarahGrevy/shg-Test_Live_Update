
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'blank_app'
    players_per_group = None
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    highest_bidder = models.IntegerField()
    highest_bid = models.CurrencyField()
    def my_method(self):
        def live_auction(self, id_in_group, bid):
                if bid > self.highest_bid:
                    self.highest_bid = bid
                    self.highest_bidder = id_in_group
                    broadcast = {'id_in_group': id_in_group, 'bid': bid}
                    return {0: broadcast}
    def my_method2(self):
        pass
class Player(BasePlayer):
    pass