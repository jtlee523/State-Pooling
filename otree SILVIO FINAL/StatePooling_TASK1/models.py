from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Joseph Lee'

doc = """
DATA:

0-2: colored ball values: RED, YELLOW, GREEN
3: GRAY ball values

4-6: Advisor 1 percentages (LHS)
7-9: Advisor 2 percentages (RHS)

"""



class Constants(BaseConstants):
	name_in_url = 'StatePooling_TASK1'
	data = [ [10, 30, 80, 60], 
		[15, 35, 85, 55], 
		[5, 25, 75, 50], 
		[10, 60, 80, 40], 
		[10, 60, 80, 30]]
		
	num_rounds=len(data)
	players_per_group = None #single player game
	
	
	
class Subsession(BaseSubsession):
	def creating_session(self):
	
		if self.round_number == 1: #if we are on the first round
			self.session.vars['data'] = Constants.data.copy() #we record the data to something on self.
		
		
		for p in self.get_players():
			task1_data = p.current_data()
			
			p.RedPoints = task1_data[0]
			p.YellowPoints = task1_data[1]
			p.GreenPoints = task1_data[2]
			p.GrayPoints = task1_data[3]




class Group(BaseGroup):
	pass
	
class Player(BasePlayer):

	
	#Variable for choice without advisors
	Choice_NoQ = models.IntegerField()
	
	#Choice_Color(Yes/No). These are for all the advisors
	#i.e. Choice_RedYes is when you have the red advisor and the ball is red.
	Choice_RedYes = models.IntegerField()
	Choice_RedNo = models.IntegerField()

	Choice_YellowYes = models.IntegerField()
	Choice_YellowNo = models.IntegerField()
	
	Choice_GreenYes = models.IntegerField()
	Choice_GreenNo = models.IntegerField()	
	
	# Variables for choices when the rainbow advisor says a color.
	Choice_RainbowRed = models.IntegerField()
	Choice_RainbowYellow = models.IntegerField()
	Choice_RainbowGreen = models.IntegerField()
	
	#===For the red page variables
	Red_Q0 = models.IntegerField()
	Red_Q1 = models.IntegerField()
	Red_Q2 = models.IntegerField()
	Red_Q3 = models.IntegerField()
	Red_Q4 = models.IntegerField()
	Red_Q5 = models.IntegerField()
	Red_Q6 = models.IntegerField()
	Red_Q7 = models.IntegerField()
	Red_Q8 = models.IntegerField()
	Red_Q9 = models.IntegerField()
	Red_Q10 = models.IntegerField()
	
	#===For the yellow page variables
	Yellow_Q0 = models.IntegerField()
	Yellow_Q1 = models.IntegerField()
	Yellow_Q2 = models.IntegerField()
	Yellow_Q3 = models.IntegerField()
	Yellow_Q4 = models.IntegerField()
	Yellow_Q5 = models.IntegerField()
	Yellow_Q6 = models.IntegerField()
	Yellow_Q7 = models.IntegerField()
	Yellow_Q8 = models.IntegerField()
	Yellow_Q9 = models.IntegerField()
	Yellow_Q10 = models.IntegerField()
	
	#===For the green page variables
	Green_Q0 = models.IntegerField()
	Green_Q1 = models.IntegerField()
	Green_Q2 = models.IntegerField()
	Green_Q3 = models.IntegerField()
	Green_Q4 = models.IntegerField()
	Green_Q5 = models.IntegerField()
	Green_Q6 = models.IntegerField()
	Green_Q7 = models.IntegerField()
	Green_Q8 = models.IntegerField()
	Green_Q9 = models.IntegerField()
	Green_Q10 = models.IntegerField()
	
	#===For the rainbow page variables
	Rainbow_Q0 = models.IntegerField()
	Rainbow_Q1 = models.IntegerField()
	Rainbow_Q2 = models.IntegerField()
	Rainbow_Q3 = models.IntegerField()
	Rainbow_Q4 = models.IntegerField()
	Rainbow_Q5 = models.IntegerField()
	Rainbow_Q6 = models.IntegerField()
	Rainbow_Q7 = models.IntegerField()
	Rainbow_Q8 = models.IntegerField()
	Rainbow_Q9 = models.IntegerField()
	Rainbow_Q10 = models.IntegerField()
	
	# Variables for storing data that is displayed
	RedPoints = models.FloatField()
	YellowPoints = models.FloatField()
	GreenPoints = models.FloatField()
	GrayPoints = models.FloatField()
	
	def current_data(self):
		return self.session.vars['data'][self.round_number-1] #returns a row of the data
	
    

	
	#colored is 0, gray is 1