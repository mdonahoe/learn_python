
from random import *
from math import *
from Gui import *
import string

a = range(1,17)
letters = []
words = []
winners = []

## extra is a function used to find all the blocks of a certain letter
extra = lambda search_list, elem:[i for i, x in enumerate(search_list) if x ==elem]


##a dictionary of the block connections
connect = {0:[1,4,5],1:[0,2,4,5,6],2:[1,3,5,6,7],3:[2,6,7],4:[0,1,5,8,9],
	5:[0,1,2,4,6,8,9,10],6:[1,2,3,5,7,9,10,11],7:[6,3,2,10,11],8:[4,5,9,12,13],
	9:[8,10,4,5,6,12,13,14],10:[5,6,7,9,11,13,14,15],11:[10,6,7,14,15],
	12:[8,9,13],13:[12,8,9,10,14],14:[13,9,10,11,15],15:[14,10,11]}

class Boggle(Gui):
    def __init__(self):
		Gui.__init__(self)
		self.setup()

##the boggle gui setup, still need to fix the 'shake' cmd so that it resets the board		
    def setup(self):
		global a
		
		shuffle(a)
		self.ca_width = 40
		self.ca_height = 40
		self.gr(4, side=LEFT, bd=10)
        # left frame
		for i in range(0,16):
			self.fr(side=LEFT, bd=5)
			self.canvas = self.ca(width=self.ca_width, height=self.ca_height, bg='white')
			item1 = self.canvas.text([0,0], self.shake(i), font = 24) 
			self.endfr()

		self.endgr()

		self.fr(RIGHT, bd=5)
		self.bu(text='Shake', command=self.setup)
		self.bu(text='Words', command=proc_words)
		self.endfr()
		

    def shake(self,b):
        global a
        global letters


##the letter blocks of a standard boggle game
        blocks = {1:['M','H','QU','U','I','N'],2:['E','E','N','G','A','A'],
              3:['A','S','F','P','F','K'],4:['E','N','U','I','E','S'],
              5:['O','B','J','O','A','B'],6:['L','T','Y','E','R','T'],
              7:['A','S','H','P','O','C'],8:['G','E','W','H','E','N'],
              9:['Y','T','D','T','S','I'],10:['A','O','T','W','T','O'],
              11:['L','N','H','N','Z','R'],12:['I','L','R','E','X','D'],
              13:['V','Y','D','R','E','L'],14:['W','R','T','E','H','V'],
              15:['S','S','I','O','T','E'],16:['O','U','M','C','I','T']}


        block = a[b]
        side = blocks[block]
        letter = choice(side)
        letters.append(letter)
        if len(letters) > 16:
            del letters[0]
        return letter

				
def proc_words():
	global letters
	print letters
	fil = 'C:\Users\provo\SD\Boggle\words.txt'
	try:
		 doc = open(fil, 'r')
	except KeyError:
		return "file not found"

##opens the dictionary file, processes words, eliminates 2 letter words and words > 16 letters
		
	for word in doc:
		word = string.rstrip(word)
		word = string.upper(word)
		
		if len(word) < 3 or len(word)>16:
			continue

##this takes each word and checks to see if it's letters match those in the grid, special handling for the 'qu' block  			
		else:
			lets = list(letters)
			q_test = 0
			wrd = []
			qt = False
			for letter in word:
				if letter =='Q':
					letter = 'QU'
					q_test = 1
					qt = True
				elif letter =='U' and qt:
					qt = False
					continue
				if letter in lets:
					lets.remove(letter)
					wrd.append(letter)
				else:
					break

#if all the words letters are in the grid, send it the pathing function

			if len(wrd) + q_test == len(word):
				nodes = extra(letters,wrd[0])
				for node in nodes:
					if find_words(wrd, node,[node]):
						winners.append(word)
						break
			
	print winners, len(winners)


##pathing function that takes the word as a list of letters, the node of the first letter and the path traversed			
def find_words(word, node, path):
	global letters
	global connect
	touches = connect[node]
	dist = len(path)
	stop = len(word)
	if dist == stop:
		return True
	c = word[dist]
	blocks = extra(letters,c)
	for b in blocks:
		if b in touches and b not in path:
			path.append(b)
			if find_words(word,b,path):
				return True

##if one node doesn't work, delete it from the path and try the others
			else:
				del path[-1]
	return False


	
if __name__=='__main__':
	game = Boggle()
	game.mainloop()
	