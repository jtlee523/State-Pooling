from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_test_game'
    players_per_group = None
    num_rounds = 1
    
    given_amount = c(10)


class Subsession(BaseSubsession):
	#this part is all for this slider
	#def creating_session(self):
	#	for p in self.get_players():
	#		p.prepare_sliders(num=3, min=0, max=4)
	pass

class Group(BaseGroup):
    pass

#class TestPlayer(BasePlayer):
	#response = models.FloatField(widget=widgets. #I don't know if we can put in the slider here?
#	pass
	
class Player(BasePlayer):
	R1 = models.IntegerField() 
	Y1 = models.IntegerField()
	G1 = models.IntegerField()
	Accuracy1 = models.IntegerField()                           
	
	R2 = models.IntegerField() 
	Y2 = models.IntegerField()
	G2 = models.IntegerField()
	
	R3 = models.IntegerField() 
	Y3 = models.IntegerField()
	G3 = models.IntegerField()
	
	R4 = models.IntegerField() 
	Y4 = models.IntegerField()
	G4 = models.IntegerField()
	
	R5 = models.IntegerField() 
	Y5 = models.IntegerField()
	G5 = models.IntegerField()
	
	R6 = models.IntegerField() 
	Y6 = models.IntegerField()
	G6 = models.IntegerField()
	
	R7 = models.IntegerField() 
	Y7 = models.IntegerField()
	G7 = models.IntegerField()
	
	R8 = models.IntegerField() 
	Y8 = models.IntegerField()
	G8 = models.IntegerField()
	
	R9 = models.IntegerField() 
	Y9 = models.IntegerField()
	G9 = models.IntegerField()
	
	R10 = models.IntegerField() 
	Y10 = models.IntegerField()
	G10 = models.IntegerField()
	
	isGray1 = models.BooleanField()
	R1task2 = models.IntegerField()
	Y1task2 = models.IntegerField()
	G1task2 = models.IntegerField()
	Accuracy1task2 = models.IntegerField() 
	
	
#This class is for out slider
#class Slider(BaseSlider):
#	player = ForeignKey(Player)