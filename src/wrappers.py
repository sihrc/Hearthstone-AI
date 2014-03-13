"""
Wrappers for development and testing

author: chris @ sihrc
"""


def action(func):
	"""
	Action Wrapper to keep track of what's happening
	"""
	def wrapper(*args, **kwargs):
		print
		res = func(*args, **kwargs)
		print "Action:%s" % res
		return res
	return wrapper

def effect(func):
	"""
	Effect Wrapper to keep track of when Effects trigger
	"""

	def wrapper(*args, **kwarges):
		print "EFFECT"
		res = func(*args, **kwargs)
		print "effect:%s" % res
		return res
	return wrapper