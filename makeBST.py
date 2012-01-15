import sys

def makeBST(s):
	if len(s) != 0:
		try:
			x = int(s[0])
		except ValueError:
			print "ERROR ON ELEMENT", s[0]
			sys.exit(1)

	if len(s) >= 2:
		left = []
		right = []
		for i in range(len(s)-1):
			try:
				if int(s[i+1]) > int(s[0]):
					right.append(s[i+1])
				else:
					left.append(s[i+1])
			except ValueError:
				print "ERROR ON ELEMENT", s[i+1]
				sys.exit(1)
				
		s[1:len(s)] = []
		s.append(left)
		s.append(right)
		

		makeBST(s[1])
		makeBST(s[2])
	
	return s
	

def main():
	seq = sys.argv[1:len(sys.argv)]
	
	if len(seq) != 0:
		tree = makeBST(seq)
		print tree
	else:
		print >> sys.stderr, "Usage: makeBST.py numbers"


if __name__ == '__main__':
	main()

	
	
	
