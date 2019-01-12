import keras, keras.layers as L, keras.backend as K

#implements v estimator and QUpdates with experience replay.experience
#first work with tabular methods, then go ahed with keras' neural network
class VEstimator(object):
	"""docstring for VEstimator"""
	def __init__(self):
		self.v = {}


	def get_value(self, afterstate):
		return self.v.get(''.join(afterstate), 0)

	def init_value(self, state):
		self.v[''.join(state)] = 0.0	#

	def update(self, s, s_next, reward, gamma, alpha):
		self.v[''.join(s)] += alpha*(reward + gamma*self.v[''.join(s_next)] - self.v[''.join(s)])

	def update_terminal(self, s, reward, alpha)
		self.v[''.join(s)] += alpha*(reward + gamma*self.v[''.join(s_next)] - self.v[''.join(s)])

