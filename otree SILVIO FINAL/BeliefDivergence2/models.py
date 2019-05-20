from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
#pandas>=0.22.0
#import pandas as pd


author = 'Joseph Lee'

doc = """
Task 2

0-2= prior (ex ante urn probability)
3-5= signal structure (black/white ball probability for each urn)
6=ball color (0/1 based on black/white ball color)
7-9= points for the color urn (risky option)
10= points for the grey urn (status quo option)
"""


class Constants(BaseConstants):
    name_in_url = 'BeliefDivergence2'
    players_per_group = None #Single player game

    data = [[0.25, 0.50,  0.25, 0.8, 0.5, 0.2, 0, 30, 55, 90, 65],
			[0.25, 0.50,  0.25, 0.9, 0.8, 0.7, 1, 30, 60, 90, 60],
			[0.25, 0.50,  0.25, 0.6, 0.5, 0.4, 1, 30, 65, 90, 55]]
    num_rounds = len(data) #as many rounds as there are lines of data



class Subsession(BaseSubsession):

	def creating_session(self):
	
		if self.round_number == 1: #if we are on the first round
			self.session.vars['data'] = Constants.data.copy() #we record the data to something on self.
		
		
		for p in self.get_players():
		
			task1_data = p.current_data()
			
			p.Red_Urn_Given = task1_data[0]
			p.Yellow_Urn_Given = task1_data[1]
			p.Green_Urn_Given = task1_data[2]
			
			p.Assigned_Red = task1_data[3]
			p.Assigned_Yellow = task1_data[4]
			p.Assigned_Green = task1_data[5]
			
			
			p.isBlackBall = task1_data[6]
			
			p.Red_Points = task1_data[7]
			p.Yellow_Points = task1_data[8]
			p.Green_Points = task1_data[9]
			p.Gray_Points = task1_data[10]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
	Red_Probability_guess = models.IntegerField()
	Green_Probability_guess = models.IntegerField()
	Yellow_Probability_guess = models.IntegerField()
	
	Red_Urn_Given = models.FloatField()
	Yellow_Urn_Given = models.FloatField()
	Green_Urn_Given = models.FloatField()
	
	isGray = models.IntegerField() #1 for gray, 0 for not
	Accuracy = models.FloatField()
	
	#These are the black/white probabilities
	Assigned_Red = models.FloatField()
	Assigned_Yellow = models.FloatField()
	Assigned_Green = models.FloatField()
	
	isBlackBall = models.IntegerField()
	
	#point values for the urns
	Red_Points = models.IntegerField()
	Yellow_Points = models.IntegerField()
	Green_Points = models.IntegerField()
	Gray_Points = models.IntegerField()
	
	def current_data(self):
		return self.session.vars['data'][self.round_number-1] #returns a row of the data
	
    



#https://otree.readthedocs.io/en/latest/misc/tips_and_tricks.html
