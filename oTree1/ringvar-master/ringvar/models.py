import os

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import ringvar.datamaker

author = 'Arthur Prat-Carrabin'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'ringvar'
    players_per_group = None    # single-player game
    if not os.path.isfile('ringvar/blocksets-100-180-10.json'):
        ringvar.datamaker.make_and_save_blocksets(100, 180, 10, 'ringvar/blocksets-100-180-10.json')
    blocksets = ringvar.datamaker.load_blocksets('ringvar/blocksets-100-180-10.json')
    # 'blocksets' contains M blockset
    # a blockset contains N blocks
    # a_blockset = [                  # "block" is my terminology (not oTree's).
    #    {'p': 0.45, 'samples': [0, 1, 0, 1, 0, 0, 0, 1, 1, 1]},
    #    {'p': 0.15, 'samples': [1, 1, 0, 0, 1, 0, 0, 1, 1, 0]},
    #]
    # we transform the data so it is easy to use by otree during the experiment
    data = []
    for blockset in blocksets:
        all_samples = sum((b['samples'] for b in blockset), [])                 # [0, 1, ...., 1, 0]
        all_probs   = sum(([b['p'],]*len(b['samples']) for b in blockset), [])  # [.45, .45, ...., .15, .15]
        block_start = sum(([True, ] + [False, ] * (len(b['samples']) - 1) for b in blockset), []) # block start indicator
        block_end   = sum(([False, ] * (len(b['samples']) - 1) + [True, ] for b in blockset), []) # block end indicator
        inblock_num = sum((list(range(1,len(b['samples'])+1)) for b in blockset), [])             # number within the blocks
        assert len(all_probs) == len(all_samples)
        r = {'all_samples':all_samples, 'all_probs':all_probs, 'block_start':block_start, 'block_end':block_end, 'inblock_num':inblock_num}
        data.append(r)
    num_data = len(data)
    num_rounds = len(all_samples) # we assume it is the same for all blocksets (N)


class Subsession(BaseSubsession):
    def creating_session(self):
        part_id = self.get_players()[0].participant.id
        part_data = Constants.data[ part_id % Constants.num_data ]
        player = self.get_players()[0]
        player.outcome = part_data['all_samples'][self.round_number - 1]
        player.prob = part_data['all_probs'][self.round_number - 1]
        #player.outcome = Constants.all_samples[self.round_number-1]
        #player.prob = Constants.all_probs[self.round_number-1]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(blank=True, min=0)
    sex = models.StringField(choices=['F','M'], blank=True)
    laterality = models.StringField(choices=['Right-handed', 'Left-handed', 'Ambidextrous', 'N/A'], blank=True)
    education = models.StringField(blank=True, label='Education (completed)',
                                   choices=['Elementary school', 'Middle school', 'High school',]
                                                       + ['Higher ed. %dy' % y for y in range(1,10)] + ['Higher ed. 10y+',])
    prob = models.FloatField()
    outcome = models.IntegerField()
    response = models.FloatField(widget=widgets.Slider(attrs={'step': '0.001', 'list':'tickmarks', 'class':'myslider'}, show_value=False),
                                 min=0.001, max=0.999,
                                 label='')