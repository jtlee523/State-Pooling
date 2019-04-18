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
	
	
class Test(Page):
    pass




class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass



page_sequence = [
	Task2_Page1,
	Task1_Page1,
	Task1_PageRED,
	Task1_PageGREEN,
	Task1_PageYELLOW,
]
