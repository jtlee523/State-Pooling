from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()
        contributions = [p.contribution for p in players]
        group.total_contribution = sum(contributions)
        group.individual_share = group.total_contribution * Cosntants.multiplier / Constants.players_per_group
        for p in players:
        	p.payoff = Constants.endowment - p.contribution + group.individual_share


class Results(Page):
    pass
    

class Contribute
	form_model = 'player'
	form_fields = ['contribution']


page_sequence = [
    Contribute,
    ResultsWaitPage,
    Results
]
