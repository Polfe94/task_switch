""""""""""""""""""""""""""
""" DEFAULT PARAMETERS """
""""""""""""""""""""""""""

''' MODEL '''
N = 10 # number of automata
beta = 0.6 # 1.5 # rate of action in arena
# gamma = 0.01 # 10**-5 # spontaneous activation
foodXvertex = 1
tau = 60 # memory decay

# sto_1: randomly distributed food (stochastic)
# sto_2: stochastic with clusterized food (hexagon patches)
# det: deterministic (sto_2 but with a specific and fixed positioning, emulating deterministic experiments)
# nf: no food (simulations without food)
food_condition = 'det'# 'det', 'sto_1', 'sto_2', 'nf'

''' LATTICE PARAMETERS '''
#Lattice size
width    = 22
height   = 13

nest = (0, 22)
nest_influence = [nest, (1, 21), (1, 22), (1, 23)] 
# direction_bias = 2 

''' THRESHOLDS ''' 
theta = 0
Theta = 10**-10 # 10**-15

''' Coupling coefficients matrix '''
# 0 - No info; 1 - Info
Jij = {'0-0': 1, '0-1': 1,
	   '1-0': 1, '1-1': 1}
# Jij = {'0-0': 0.4, '0-1': 1,
# 	   '1-0': 0.4, '1-1': 1}
    
''' Movement probability matrix '''            
mov_matrix = {'l': 0.4, 'b': 0.2, 'r': 0.4}
rand_matrix = {'l': 0.333, 'b': 0.333, 'r': 0.333}
