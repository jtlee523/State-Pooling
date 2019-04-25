from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass
    
class Arthurs_Page(Page):
    form_model = 'player'
    form_fields = ['response', 'response2']

        


	
class Task1_1(Page):
	#form_fields = ['my_hidden_input']
	pass
	
class T1_1Feedback(Page):
	form_model='player'
	form_fields=['R1', 'Y1', 'G1', 'Accuracy1']
	pass
	
	
class Task1_2(Page):
	#form_fields = ['my_hidden_input']
	pass
	
class T1_2Feedback(Page):
	form_model='player'
	form_fields=['R2', 'Y2', 'G2']
	pass


class Task1_3(Page):
	#form_fields = ['my_hidden_input']
	pass
	
class T1_3Feedback(Page):
	form_model='player'
	form_fields=['R3', 'Y3', 'G3']
	pass
	

class Task1_4(Page):
	#form_fields = ['my_hidden_input']
	pass
	
class T1_4Feedback(Page):
	form_model='player'
	form_fields=['R4', 'Y4', 'G4']
	pass


class Task1_5(Page):
	#form_fields = ['my_hidden_input']
	pass
	
class T1_5Feedback(Page):
	form_model='player'
	form_fields=['R5', 'Y5', 'G5']
	pass
	
	
class Task1_6(Page):
	#form_fields = ['my_hidden_input']
	pass
	
class T1_6Feedback(Page):
	form_model='player'
	form_fields=['R6', 'Y6', 'G6']
	pass
	
	
class Task1_7(Page):
	#form_fields = ['my_hidden_input']
	pass
	
class T1_7Feedback(Page):
	form_model='player'
	form_fields=['R7', 'Y7', 'G7']
	pass
	
	
class Task1_8(Page):
	#form_fields = ['my_hidden_input']
	pass
	
class T1_8Feedback(Page):
	form_model='player'
	form_fields=['R8', 'Y8', 'G8']
	pass
	
	
class Task1_9(Page):
	#form_fields = ['my_hidden_input']
	pass
	
class T1_9Feedback(Page):
	form_model='player'
	form_fields=['R9', 'Y9', 'G9']
	pass
	
	
class Task1_10(Page):
	#form_fields = ['my_hidden_input']
	pass
	
class T1_10Feedback(Page):
	form_model='player'
	form_fields=['R10', 'Y10', 'G10']
	pass
	


class Task2_1(Page):
	form_model='player'
	form_fields=['isGray1']
	pass


class T2_1Feedback1(Page):
	form_model='player'
	form_fields=['R1task2', 'Y1task2', 'G1task2', 'Accuracy1task2']
	pass

class T2_1Feedback2(Page):
	pass
	

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
	Task2_1,
	T2_1Feedback1,
	T2_1Feedback2, 
	Task1_1,
	T1_1Feedback,
	Task1_2,
	T1_2Feedback,
	Task1_3,
	T1_3Feedback,
	Task1_4,
	T1_4Feedback,
	Task1_5,
	T1_5Feedback,
	Task1_6,
	T1_6Feedback,
	Task1_7,
	T1_7Feedback,
	Task1_8,
	T1_8Feedback,
	Task1_9,
	T1_9Feedback,
	Task1_10,
	T1_10Feedback,
	
]
