from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass

class WaitForP1(WaitPage):
	pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
    	group = self.group
    	p1 = group.get_player_by_id(1)
    	p2 = group.get_player_by_id(2)
    	p1.payoff = Constants.edowment - group.sent_amount + group.sent_back_amount
    	p2.payoff = group.sent_amount * Constants.multiplication_factor - group.sent_back_amount


class Results(Page):
    pass

class Send(Page): #not sure if this is right
	
	form_model = 'group'
	form_fields = ['sent_amount']
	
	def is_displayed(self):
		return self.player.id_in_group == 1

class SendBack(Page):
	
	form_model = 'group'
	form_fields = ['sent_back_amount']
	
	def is_displayed(self):
		return self.player.id_in_group == 2
		
	def vars_for_template(self):
		return {
			'tripled_amount': self.group.sent_amount * Constants.multiplication_factor
		}
	
	def sent_back_amount_choices(self):
		return currency_range(
			c(0),
			self.group.sent_amount * Constants.multiplication_factor,
			c(1),
		)

page_sequence = [
    Send,
    WaitForP1,
    SendBack,
    ResultsWaitPage,
    Results,
]
