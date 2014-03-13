"""
Wrappers for development and testing

author: chris @ sihrc
"""
import os,sys

class RedirectStdStreams(object):
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr


def action(func):
	"""
	Action Wrapper to keep track of what's happening
	"""
	def wrapper(*args, **kwargs):
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

def shutup(func):
	"""
	Silence stdout
	"""
	def wrapper(*args, **kwargs):
		with RedirectStdStreams():
			res = func(*args, **kwargs)
		return res
	return wrapper

def redirect(func):
	"""
	Redirect Output
	"""
	def wrapper(*args, **kwargs):
		with RedirectStdStreams(stdout = open("output", 'ab')):
			res = func(*args, **kwargs)
		return res
	return wrapper

def log(*args):
	for arg in args:
		div()
		print arg
		div()

def div():
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


