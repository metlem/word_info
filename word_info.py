class CountLetter:
	def __init__(self):
		self.vowel = "aeıioöuü"
		self.consonant = "bcçdfgğhjklmnprsştvyz"
		self.word_count = 0
		self.vowel_count = 0
		self.consonant_count = 0

	def question_word(self):
		return input("Please write word : ")

	def is_vowel(self, letter):
		return letter in self.vowel

	def is_consonant(self, letter):
		return letter in self.consonant

	def count_letter(self):
		for letter in self.word:
			if self.is_vowel(letter):
				self.vowel_count +=1
			if self.is_consonant(letter):
				self.consonant_count +=1
		return (self.vowel_count, self.consonant_count)

	
	def reverse_word(self):
		self.word_count = len(self.word)
		self.reverse_word = []
		for letter in range(0,self.word_count):
			self.word_count -=1
			self.reverse_word.append(self.word[self.word_count])
		return "".join(self.reverse_word)
		
	def print_result(self):
		vowel_letter, consonant_letter = self.count_letter()
		reverse_word = self.reverse_word()
		result = {}
		result["word"], result["vowel_count"], result["consonant_count"], result["reverse_word"] = self.word, vowel_letter, consonant_letter, reverse_word
		print(result)
		

	def run_app(self):
		self.word = self.question_word()
		self.print_result()

if __name__ == '__main__':
	countletter = CountLetter()
	countletter.run_app()


