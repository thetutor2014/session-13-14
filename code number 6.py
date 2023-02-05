from collections import Counter
def firstRepeat(input):
	words = sentence.split(' ')
	dict = Counter(words)
	for key in words:
		if dict[key]>1:
			print (key)
			return
if __name__ == "__main__":
	sentence = input('Enter your data please: ')
	firstRepeat(sentence)
