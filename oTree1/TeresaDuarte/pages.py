from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#FOR TASK 1

#ConsentPage: Page certifying consent for the experimentee
#Contains a button that says "I accept"
class ConsentPage(Page):
	pass
	
#IntructionPage1: Instructions for task 1 
#contains an I understand next page
class InstructionPage1(Page):
	pass

#InstructionPage2: Identical to page 1 but for the second task
class InstructionPage2(Page):
	pass


class Game1Green(Page):
	form_model='player'
	form_fields=['GreenRoundChoice']
	pass
	
class Game1Blue(Page):
	form_model='player'
	form_fields=['BlueRoundChoice']
	pass
	
class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class Task2(Page):
	#form_model = 'player'
	#form_fields=['Points']
	pass

class Results(Page):
    pass



page_sequence = [

	#ConsentPage,
	#InstructionPage1,
	#Game1Green,
	Game1Blue,
	InstructionPage2,
	Task2,
	#Task_One,
	#Task_One_Feedback,
    #Test,
    #Results
]
