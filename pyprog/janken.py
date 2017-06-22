p1=raw_input("Player 1, please choose either rock, paper or scissors: ")
p2=raw_input("Player 2, please choose either rock, paper or scissors: ")


if p1==p2:
	print "It's a draw."
elif p1=="rock":
	if p2=="scissors":
		print "Player 1 wins!"
	else:
		print "Player 2 wins!"
elif p1=="paper":
	if p2=="rock":
		print "Player 1 wins!"
	else:
		print "Player 2 wins!"
elif p1=="scissors":
	if p2=="paper":
		print "Player 1 wins!"
	else:
		print "Player 2 wins!"