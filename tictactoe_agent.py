import numpy as np
from V_estimator import VEstimator

class QAgent:

	def __init__(self, symbol):
		self.alpha = 0.1
		self.gamma = 0.9
		self.epsilon = 0.1
		self.v = VEstimator()		#
		self.symbol = symbol
		self.first_play = True

	def set_greed(self, epsilon):
		self.epsilon = epsilon

	def init_game(self, start_state=np.full(9, '.')):
		self.first_play = True
		self.current_state = start_state
		#should add global init of vestimator

	def afterstates(self, state):
		next_states = []
		for i, s in enumerate(state=='.'):
			if s:
				state_copy = state.copy()
				state_copy[i] = self.symbol
				next_states.append(state_copy)
				self.v.init_state(state_copy)	#should be removed with global init
#				self.v[''.join(state_copy)] = 0.0	#
		return next_states


	def get_best_afterstate(self, afterstates):
		av = [self.v.get_value(afterstate) for afterstate in afterstates]
		max_index = av.index(max(av))
		return afterstates[max_index]


	def update_and_play(self, new_state, reward ):

		#update
		afterstates = self.afterstates(new_state)
		best_afterstate = self.get_best_afterstate(afterstates)
		if not self.first_play:
			self.v.update(self.current_state, self.new_state, reward, self.gamma, self.alpha)
#			self.v[''.join(self.current_state)] += self.alpha*(reward + self.gamma*self.v[''.join(best_afterstate)] - self.v[''.join(self.current_state)])
			self.first_play = False

		#update: epsilon geedy
		if(np.random.choice([True, False], p=[self.epsilon, 1-self.epsilon])):
			self.current_state = afterstates[np.random.randint(0, len(afterstates))]
		else:
			self.current_state = best_afterstate

		return self.current_state


	def update_final(self, reward ):
		self.v.update_terminal(self.current_state, reward, self.alpha)
#		self.v[''.join(self.current_state)] += self.alpha*(reward - self.v[''.join(self.current_state)])



# testing functions
if __name__=="__main__":
	init_state = np.full(9, ['.'])
	qq = QAgent('x')
	qq.init_game()
	z = qq.afterstates(init_state)
	print(z)
	print(qq.get_best_afterstate(z))
	print(qq.update_and_play(init_state, 1.0))
