from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass

class ResultsSummary(Page):
	
	def is_displayed(self):
		return self.round_number == Constants.num_rounds
		#returns a boolean to see if its the last round
	
	def vars_for_template(self):
		
		return {
			'total_payoff': sum([p.payoff for p in self.player.in_all_rounds()]),
			'paying_round': self.session.vars['paying_round'],
			'player_in_all_rounds': self.player.in_all_rounds(),
		}
    
class Choice(Page):
	form_model = 'player' #I think tis creates a place to put the player name
	form_fields = ['penny_side']	#a field to pick the peny side
	
	def vars_for_template(self):
		return {
			'player_in_previous_rounds': self.player.in_previous_rounds(),
		}


page_sequence = [
    Choice,
    ResultsWaitPage,
    ResultsSummary
]
