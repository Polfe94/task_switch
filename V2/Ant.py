from mesa import Agent
import numpy as np
from functions import direction, get_cos , get_cos_180, dist 
import math
from parameters import nest, theta # , nest_influence, direction_bias
import random

''' ANT AGENT '''
class Ant(Agent):

	def __init__(self, unique_id, model, mot_matrix, behavior, g = np.random.uniform(0.0, 1.0), social = True):

		super().__init__(unique_id, model)

		self.Si = 0
		self.g = g
  
		# number of encounters with food
		self.evidence = 0
		# self.s_food = 0
		# self.s_empty = 0
  
		# time since last interaction
		self.time_last_interaction = 0
  
		# interaction with individuals 
		self.last_interaction = str([])

		# average n of interactions to switch to recruit / scout 
  
		### PROBLEMA: HI HA MASSA INTERACCIONS AL NIU, I O BÉ CANVIEN MOLT RAPID A SCOUT, O BE NO CANVIEN MAI
		self.thresholds = {'scout': 1, 'recruit': 1}

		self.is_active = False
		self.state = '0'
		self.status = 'gamma'
		self.behavior_tag = behavior

		self.origin = nest

		self.food = []

		# start in the arena
		self.model.grid.place_agent(self, nest)
   
		self.reset_movement()
		self.move_default = self.move_exp
  
		self.mot_matrix = mot_matrix
  
		if social:
			self.interaction = self.interaction_with_recruitment
		else:
			self.interaction = self.interaction_without_recruitment
		
	def reset_movement(self):
		self.movement = 'default'
		self.move_history = (self.origin, 
				random.choice(self.model.grid.get_neighborhood(self.origin)),
				self.origin)
 
	def update_movement(self):
		self.move_history = (self.move_history[1], self.move_history[2], self.pos)
  
	def move_exp(self, pos):
		if None in self.move_history:
			return self.move_random(pos)

		else:

			p = []
			r = range(len(pos))
			for i in r:
				x = [self.model.coords[self.move_history[1]], self.model.coords[self.move_history[2]], self.model.coords[pos[i]]]
				try:
					p.append(self.mot_matrix[direction(x)])
				except:
					print(x)

			idx = np.random.choice(r, p = p / np.sum(p)) # normalize to 1 in case probabilities don't already sum 1
			return pos[idx]
  
	# def move_exp(self, pos):
	# 	if None in self.move_history:
	# 		return self.move_random(pos)

	# 	else:

	# 		p = np.array(self.mot_matrix[direction([self.model.coords[i] for i in self.move_history])])
	# 		ords = []
	# 		pord = []
	# 		for i in range(len(pos)):
	# 			x = [self.model.coords[self.move_history[1]], self.model.coords[self.move_history[2]], self.model.coords[pos[i]]]
	# 			ords.append(i)
	# 			dirx = direction(x)
	# 			if dirx == 1:
	# 				pord.append(p[0])
	# 			elif dirx == 0:
	# 				pord.append(p[1])
	# 			elif dirx == -1:
	# 				pord.append(p[2])

	# 		idx = np.random.choice(ords, p = pord / np.sum(pord)) # normalize to 1 in case probabilities don't already sum 1
	# 		return pos[idx]

	def move_random(self, pos):
		l = list(range(len(pos)))
		idx = np.random.choice(l)
		return pos[idx]

	def move_homing(self, pos):
    		
		x0 = np.array(self.model.coords[self.pos])
		x1 = np.array([self.model.coords[i] for i in pos])
	
		tpos = x1 - x0
		d = self.target - x0

		l = len(pos)
		if l == 2:
			A = 1+get_cos(d, tpos[0])
			p1 = (A) / (A + (1+get_cos(d, tpos[1])))
			p2 = 1-p1
			p = [p1, p2]
			idx = np.random.choice(l, p = p / np.sum(p))

		elif l == 3:
			p = []
			for i in range(l):
				pi = (1/3) * (1 + get_cos(d, tpos[i]))
				p.append(pi)
			idx = np.random.choice(l, p = p/np.sum(p))
		else:
			idx = 0

		return pos[idx]

	# def move_homing(self, pos):
		
	# 	x0 = np.array(self.model.coords[self.pos])
	# 	x1 = np.array([self.model.coords[i] for i in pos])
	
	# 	tpos = x1 - x0
	# 	d = self.target - x0

	# 	l = len(pos)
	# 	if l == 2:
	# 		A = 1+get_cos(d, tpos[0])
	# 		p1 = (A) / (A + (1+get_cos(d, tpos[1])))
	# 		p2 = 1-p1
	# 		p = [p1, p2]
	# 		idx = np.random.choice(l, p = p / np.sum(p))

	# 	elif l == 3:
	# 		p = []
	# 		for i in range(l):
	# 			pi = (1/3) * (1 + get_cos(d, tpos[i]))
	# 			p.append(pi)
	# 		idx = np.random.choice(l, p = p/np.sum(p))
	# 	else:
	# 		idx = 0

	# 	return pos[idx]

	# Move method
	def move(self):
     
		possible_steps = self.model.grid.get_neighborhood(
		self.pos,
		include_center = False)

		if self.movement == 'default':
			pos = self.move_default(possible_steps)
	
		else:
			pos = self.move_homing(possible_steps) # works also towards food

		self.model.grid.move_agent(self, pos)
		self.model.nodes['N'][self.model.nodes['Node'].index(self.pos)] += 1
		# self.model.nodes.loc[self.model.nodes['Node'] == self.pos, 'N'] += 1
		self.update_movement() 

	def find_neighbors(self):
     
		alist = self.model.grid.get_cell_list_contents([self.pos])
   
		flist = list(filter(lambda a: a.unique_id != self.unique_id, alist))
  
		if len(flist) <= 4 and len(flist) > 0:
			neighbors = np.random.choice(flist, size = len(flist), replace = False)
		elif len(flist) > 4:
			neighbors = np.random.choice(flist, size = 4, replace = False)
		else:
			neighbors = []

		return neighbors

	def update_features(self):
		self.mot_matrix = self.model.matrices[self.behavior_tag]
		self.g = self.model.gains[self.behavior_tag]
		self.evidence = 0.0 # reset evidence


	def switch_role(self):
		if self.behavior_tag == 'scout':
			self.behavior_tag = 'recruit'
		else:
			self.behavior_tag = 'scout'
   
		self.update_features()
		
	def update_role(self, n_food, n_empty):
		# Evidence is the difference between what I currently am, and the opposite role
		# if I'm scout, food triggers a switch towards recruit
		# if I'm recruit, absence of food triggers a switch towards scout

		# compute time since last interaction
		dt = self.model.time - self.time_last_interaction
  
		if self.behavior_tag == 'scout':
			input_signal = n_food - n_empty
		else:
			input_signal = n_empty - n_food

		# 2. Leaky Integration
		leak = np.exp(-dt / self.model.tau)
		self.evidence = self.evidence * leak + input_signal
		self.evidence = max(0, self.evidence) # avoid negative values

		# 3. Decisió per Llindar (sense saturació de ràtio)
		# if self.cooldown > 0:
		# 	self.cooldown -= 1
		# 	return

		if self.evidence > self.thresholds[self.behavior_tag]:
			
			self.switch_role()
			print('++++ Role updated! Switched to', self.behavior_tag, '++++')
   
	def integrate_activity(self, neighbor):
		act = self.model.Jij[self.state + "-" + neighbor.state]* neighbor.Si - self.model.Theta
		nfood = len(neighbor.food)
  
		return act, nfood


	def interaction_with_recruitment(self):
		neighbors = self.find_neighbors()

		z = [] # activity
		t = [] # target
		ids = [] # neighbor ids
  
		l = len(neighbors)
  
		if l:
			nfood = 0
			# for more than one neighbor...
			for i in neighbors:
				zneighbor, food = self.integrate_activity(i)
				z.append(zneighbor)
				nfood += food
				if hasattr(i, 'food_location'): t.append(self.model.coords[i.food_location])
				ids.append(i.unique_id)
    
			# VERSION 1: absolute encounters
			# self.update_role(n_food = nfood, n_empty = l - nfood)

			# VERSION 2: relative encounters

			self.update_role(n_food = int(bool(nfood)), n_empty = int(not nfood))
			z = sum(z)
		else:
			z = 0

		self.Si = math.tanh(self.g * (z + self.Si -self.model.Theta) ) # update activity
		if len(t):
		# if len(t) and not hasattr(self, 'target'):
			self.target = t[-1]
			self.movement = 'target'
   
		self.last_interaction = str(ids)
   
	def interaction_without_recruitment(self):
		neighbors = self.find_neighbors()

		z = [] # activity
		int_type = self.behavior_tag + '_' + self.movement + '+'
  
		l = len(neighbors)
		if l:
			# for more than one neighbor...
			for i in neighbors:
				z.append(self.model.Jij[self.state + "-" + i.state]* i.Si - self.model.Theta)
				int_type += i.behavior_tag + '_' + i.movement + '+'

			z = sum(z)
   
		else:
			z = 0
		self.Si = math.tanh(self.g * (z + self.Si -self.model.Theta) ) # update activity
		
		return int_type[:-1]
	
	def update_status(self):
		self.check_status()
		for i in self.model.activity:
			try:
				self.model.activity[i].remove(self)
			except:
				continue
		self.model.activity[self.is_active].append(self)

	# def update_status(self):
	# 	self.check_status()
  
	# 	for i in self.model.states:
	# 		try:
	# 			self.model.states[i].remove(self)
	# 		except:
	# 			continue
	# 	for i in self.model.activity:
	# 		try:
	# 			self.model.activity[i].remove(self)
	# 		except:
	# 			pass
		
	# 	if self.status == 'gamma':
	# 		self.model.states['gamma'].append(self)

	# 	self.model.states['beta'].append(self)
	# 	self.model.activity[self.is_active].append(self)
	
	def check_status(self):
     
		if self.Si < theta and self.pos == nest:
			self.is_active = False
		else:
			self.is_active = True
	# 		self.status = 'gamma'
	# 	else:
	# 		self.status = 'beta'
 
	def leave_nest(self):
		self.model.grid.place_agent(self, nest)
		self.is_active = True


	# all ants start in the arena
	def enter_nest(self):
		# self.model.remove_agent(self)
		self.is_active = False
		# self.pos = 'nest'
		self.ant2explore()
		self.origin = nest
		
		if len(self.food):
			self.food[-1].in_nest(self.model.time)

	def ant2nest(self):
		self.target = self.model.coords[nest]
		self.movement = 'homing'

	def ant2explore(self):
		if hasattr(self, 'target'):
			del self.target
		self.reset_movement()

	def pick_food(self):
		self.model.remove_agent(self.model.food[self.pos][0])
		self.food.append(self.model.food[self.pos].pop(0))
		self.model.food[self.pos].extend(self.food)
		self.model.food[self.pos][-1].collected(self.model.time)
		self.model.food_dict[self.pos] -= 1
		self.food_location = self.pos
		self.state = '1'
		### MODIFICATION OF DEFAULT MOVEMENT !!
		# self.model.set_default_movement('exp')
  
	def role_switch():
		pass

	def update_memory():
		pass


	def drop_food(self):
		self.food[-1].dropped(self.model.time)
		self.food.pop()
  
	def action(self):
    		
      
		if self.is_active:
      
			if len(self.food):
				self.ant2nest()
    
			if self.Si < theta:
				self.ant2nest()

			if self.pos == nest:
				if hasattr(self, 'target') and self.target == self.model.coords[nest]:
					self.enter_nest()

				else:
					self.move()

			elif self.pos in self.model.food_positions:
       
				if not self.model.food[self.pos][-1].is_detected:
					self.model.food[self.pos][-1].detected(self.model.time, self.origin)
     
				self.origin = self.pos
       
				if hasattr(self, 'target') and self.model.coords[self.pos] == self.target:
					self.ant2explore()
	   
				if self.model.food_dict[self.pos] > 0 and not len(self.food):
					self.pick_food()

				else:
					self.move()
     
			else:
				self.move()
   
		else:
			if np.random.uniform(0, 1) < 0.01:
				self.Si = 1
				self.is_active = True
				self.model.activity[True].append(self)


		self.interaction()
		self.update_status()

	
  
	# def action(self, rate):
		
	# 	# if rate == 'alpha':
	# 	# 	if len(self.food):
	# 	# 		self.drop_food()
	# 	# 	else:
	# 	# 		if self.Si > theta:
	# 	# 			self.leave_nest()

	# 	if rate == 'beta':
	  
	# 		if len(self.food):
	# 			self.ant2nest()
    
	# 		if self.Si < theta:
	# 			self.ant2nest()

	# 		if self.pos == nest:
	# 			if hasattr(self, 'target') and self.target == self.model.coords[nest]:
	# 				self.enter_nest()

	# 			else:
	# 				self.move()

	# 		elif self.pos in self.model.food_positions:
       
	# 			if not self.model.food[self.pos][-1].is_detected:
	# 				self.model.food[self.pos][-1].detected(self.model.time, self.origin)
     
	# 			self.origin = self.pos
       
	# 			if hasattr(self, 'target') and self.model.coords[self.pos] == self.target:
	# 				self.ant2explore()
	   
	# 			if self.model.food_dict[self.pos] > 0 and not len(self.food):
	# 				self.pick_food()

	# 			else:
	# 				self.move()
     
	# 		else:
	# 			self.move()
   
	# 	else:
	# 		self.Si = 1 # np.random.uniform(0.0, 1.0) ## spontaneous activation


	# 	int_type = self.interaction()
	# 	self.update_status()

	# 	return int_type