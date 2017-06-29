words = open("spell.words.txt", "r").readlines()

words = map(lambda x: x.strip(), words)

#print words
#print len(words)
#print words[0]
#print words[-1]

#print("zygotic" in words)
#print("mistasdas" in words)
class SpellChecker:
	def __init__(self):
		self.words = []
		
	def load_words(self, file_name):
		self.words = open(file_name).readlines()
		self.words = map(lambda x: x.strip(), self.words)

	def check_word(self, word):
		return word.strip(".").lower() in self.words

	def check_words(self, sentence):
		words_to_check = sentence.split(' ')
		failed_words = []
		for word in words_to_check:
			if not self.check_word(word):
				print('Word is misspelt : ' + word)
				failed_words.append(word)
		return failed_words
	
if __name__ == '__main__':	
	spell_check = SpellChecker()
	spell_check.load_words("spell.words.txt")
	print spell_check.check_word('zygotic')
	print spell_check.check_word('mistasdas')
	print spell_check.check_words('zygotic mistasdas elementary')
	