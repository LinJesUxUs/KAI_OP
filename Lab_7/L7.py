import time
import threading
import random
import string
import shutil
from datetime import datetime

class TrashWords:
	def __init__(self):
		self.strings_list = []
		self.lock = threading.Lock()
		self.running = True
		self.__screen_width = shutil.get_terminal_size().columns
		self.chars = string.ascii_letters + string.digits + ' ' + string.punctuation

	def get_random_length(self):
		return random.randint( 1, self.__screen_width )

	def get_random_char(self):
		return random.choice( self.chars )

	def get_random_string(self):
		return ''.join( self.get_random_char() for _ in range( self.get_random_length() ) )

obj = TrashWords()
print( obj.get_random_string() )