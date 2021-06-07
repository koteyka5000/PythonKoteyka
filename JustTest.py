class Test:
	def __init__(self, i, q):
		self.i = i
		self.q = q
	def info(self):
		return {'i': self.i,  'q': self.q}
	def lol(self):
		g = (1, 2, 3, 4, 5, 6, 7, 8)
		l = []
		for gg in g:
			if gg % 2 == 0:
				l.append(gg)
			else:
				l.append(g[gg]-1)
		return l
			
