from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#FOR TASK 1

class Task1_Page1(Page):
	form_model = 'player'
	form_fields=['Var6', 'Var0','Var1', 'Var2','Var3','Var4','Var5' ]
	pass


class Task1_PageRED(Page):
	pass	

class Task1_PageGREEN(Page):
	pass	
	
class Task1_PageYELLOW(Page):
	pass	
	
class Task1_PageRainbow(Page):
	pass		
	
class Test(Page):
    pass

class Task2_Page1(Page):
	form_model = 'player'
	form_fields=['Advisor_VAR']
	pass	

class Task2_PageLHS(Page):
	pass
	
class Task2_PageRHS(Page):
	pass	
	
class Task2_PageSELECTED(Page):
	pass	
	
class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
	Task2_Page1,
	Task2_PageSELECTED,
	Task1_Page1,
	Task1_PageRED,
	Task1_PageGREEN,
	Task1_PageYELLOW,
	Task1_PageRainbow,
	

]

