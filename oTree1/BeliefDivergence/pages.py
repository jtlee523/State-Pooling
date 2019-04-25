from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#FOR TASK 1

class Task_One(Page):
    pass

class Task_One_Feedback(Page):
	form_model='player'
	form_fields=['Red_Probability_guess', 'Yellow_Probability_guess', 'Green_Probability_guess', 'Accuracy']
    
    
class Test(Page):
    pass




class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
	Task_One,
	Task_One_Feedback,
    #Test,
    #Results
]
