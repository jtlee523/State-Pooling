from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#FOR TASK 2

class Task_Two(Page):
	form_model='player'
	form_fields=['isGray']
	pass
	
class Task_Two_Page1(Page): #added for the two page system
	form_model='player'
	#form_fields=['isGray']
	pass
	
class Task_Two_Page2(Page): #added for the two page system
	form_model='player'
	form_fields=['isGray']
	pass
	
class Task_Two_Feedback(Page):
	form_model='player'
	form_fields=['Red_Probability_guess', 'Yellow_Probability_guess', 'Green_Probability_guess', 'Accuracy']
    

class Task_Two_FollowUp(Page):
	pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
	#Task_Two,
	Task_Two_Page1,
	Task_Two_Page2,
	Task_Two_Feedback,
	Task_Two_FollowUp,
    #Test,
    #Results
]
