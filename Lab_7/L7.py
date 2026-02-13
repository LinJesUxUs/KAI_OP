import time
import threading
import random
import string
import shutil
from datetime import datetime

class TrashWords:
	def __init__(self):
		self.__strings_list = []
		self.__lock = threading.Lock()
		self.__running = True
		self.__screen_width = shutil.get_terminal_size().columns
		self.__chars = string.ascii_letters + string.digits + ' ' + string.punctuation

	def get_random_length(self):
		return random.randint( 1, self.__screen_width )

	def get_random_char(self):
		return random.choice( self.__chars )

	def get_random_string(self):
		return ''.join( self.get_random_char() for _ in range( self.get_random_length() ) )

	def main_thread(self):
		self.__strings_list.append( self.get_random_string() )

	def get_string_list(self):
		return self.__strings_list

obj = TrashWords()
obj.main_thread()
print( *obj.get_string_list() )
obj.main_thread()
print( *obj.get_string_list(), sep='\n' )