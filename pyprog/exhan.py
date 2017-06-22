# testException.py

invalid = 1	

while invalid == 1:
	try:
		invalid = 0
		instr = raw_input("Please enter integer: ")
		inint = int(instr)
	except ValueError:
		print "oops..."
		invalid = 1
	except EOFError:
		print "Fuck you too ya prick 8=====D--,..."
	except:
		print "I have NO IDEA what's happeing!"