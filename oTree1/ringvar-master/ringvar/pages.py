from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

def get_participant_data(part_id):
    return Constants.data[part_id % Constants.num_data]

class StartPage(Page):
    def is_displayed(self):
        return self.round_number == 1
    form_model = 'player'
    form_fields = ['age', 'sex', 'laterality', 'education']

class NewBlockPage(Page):
    def is_displayed(self):
        part_data = get_participant_data(self.participant.id)
        return part_data['block_start'][self.round_number-1]
        #return Constants.block_start[self.round_number-1]

class EndBlockPage(Page):
    def is_displayed(self):
        part_data = get_participant_data(self.participant.id)
        return part_data['block_end'][self.round_number - 1]
        #return Constants.block_end[self.round_number-1]

    def vars_for_template(self):
        part_data = get_participant_data(self.participant.id)
        num = part_data['inblock_num'][self.round_number-1]
        #num = Constants.inblock_num[self.round_number-1];
        block_players = self.player.in_rounds( self.round_number - num + 1, self.round_number )
        resps_as_pct = [p.response*100 for p in block_players]
        points_in_block = sum(p.payoff for p in block_players)
        return {'pct': self.player.prob*100, 'resps':resps_as_pct, 'points':points_in_block}

class SliderPage(Page):
    form_model = 'player'
    form_fields = ['response', ]

    def vars_for_template(self):
        slider_start = .5
        part_data = get_participant_data(self.participant.id)
        #if not Constants.block_start[self.round_number-1]: # and self.round_number > 1:
        if not part_data['block_start'][self.round_number - 1]:  # and self.round_number > 1:
                slider_start = self.player.in_round(self.round_number - 1).response
        slider_start_pct = 100*slider_start
        return {'slider_start' : slider_start, 'slider_start_pct':slider_start_pct}

    def before_next_page(self):
        self.player.payoff = 1. - (self.player.response - self.player.prob)**2

'''
class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass
'''

class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    StartPage,
    NewBlockPage,
    SliderPage,
    EndBlockPage,
    Results
]
