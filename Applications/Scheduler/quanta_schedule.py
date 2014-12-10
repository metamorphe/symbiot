from quanta import Quanta
import operator

def histogram(elements):
	hist = {}
	for el in elements:
		if hist.has_key(el.priority):
			hist[el.priority].append(el)
		else:
			hist[el.priority] = [el]
	return hist

class QuantaSchedule:
	def __init__(self, jobs, Qs, Ts):
		self.jobs = jobs
		self.capacity = Qs
		self.period = Ts
		self.quantize();
		

	def quantize(self):
		for j in self.jobs:
			j.set_priority("cbs", self.period)


		quanta = histogram(self.jobs)
		quanta = sorted(quanta.items(), key=operator.itemgetter(0))

		linked_quanta = []

		prev = None
		for n, q in quanta:
			curr = Quanta(n, self.capacity, self.period ,q, prev)
			linked_quanta.append(curr)
			prev = curr

		self.quanta = linked_quanta

	def clean(self):
		# dead_jobs = self.quanta[-1].schedule()
		dead_jobs = [(q.id, q.schedule()) for q in self.quanta]
		
		# for id, j in dead_jobs:
		# 	print id, j

		dead_jobs = [q for i, q in dead_jobs]

		removed = [q.reject() for q in self.quanta]
			
		dead_jobs = sum(dead_jobs, [])
		# for j in dead_jobs:
		# 	print j
		
		# these need to be added
		# print "APPENDING"
		self.append(dead_jobs)
		# for q in self.quanta[0:80]: 
			# print q


	def find(self, id):
		results = filter(lambda q: q.id == id, self.quanta)
		if len(results) == 0:
			return None
		else:
			return results[0]
		
	def add_quanta(self, j):
		# print j.priority
		prev = min(self.quanta, key=lambda q: j.priority - q.id )
		q = Quanta(j.priority, self.capacity, self.period, [j], prev)
		q.created = True
		# print "Created ", q.id
		self.quanta.append(q)
		self.quanta = sorted(self.quanta,  key=lambda q: q.id)
				
	def append(self, jobs):
		# print self.period
		


		jobs = [j.set_priority("cbs", self.period) for j in jobs]

		for j in jobs:
			# print j
			q = self.find(j.priority)
			# print q
			if q:
				# print "Added to ", q.id
				q.jobs.append(j)
			else:
				self.add_quanta(j)

	def to_schedule(self):
		self.quanta = sorted(self.quanta,  key=lambda q: q.id)
		schedule = [q.jobs for q in self.quanta]
		return sum(schedule, [])

	def __str__(self):
		s = "SCHEDULE"
		# quanta = ", ".join([str(q) for q in self.quanta])
		for q in self.quanta:
			print q
		# s += quanta
		return s 

	