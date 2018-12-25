from __future__ import absolute_import
from __future__ import print_function
import cmd

class HelloWorld(cmd.Cmd):
	"""Simple command processor example."""
	def do_greet(self, line):
		print("hello")
	def do_EOF(self, line):
		return True
	def do_martin(self, line):
		print("Hallo Martin")
		
if __name__ == '__main__':
    HelloWorld().cmdloop()

