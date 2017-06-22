forename=raw_input("Please input your first name: ").lower()
surname=raw_input("Please input your second name: ").lower()

username=surname[:6]+forename[:2]
print "Your user name is: ", username