import scheduler
import Queue
class Quanta:
	def __init__(self, idx, Qs, T, jobs, prev=None):
		self.id = idx
		self.period = T
		self.capacity = float(Qs)
		self.jobs = jobs
		self.prev = prev
		self.next = None
		self.created = False
		# update the linked list
		if self.prev:
			if self.prev.next:
				self.next = self.prev.next
			self.prev.set_next(self)
		return

	def __str__(self):
		s = "QUANTA :{:3.0f}  ".format(self.id)
		s += "n:{:2.0f}  ".format(len(self.jobs))
		s += "cap:{:3.1f}% ".format(len(self.jobs) / self.capacity * 100)
		s += "Qs:{:2.3f} ".format(self.capacity)

		if self.created:
			s += "CREATED"
		# jobs = ", ".join([str(j) for j in self.jobs])
		# s += jobs
		return s 

	def schedule(self):

		if not self.is_over_capacity():
			return []

		self.jobs = scheduler.to_commands(self.jobs, priority_type = "pdf")
		
		dead_jobs = self.jobs[int(self.capacity):]
		# print dead_jobs
		dead_jobs = [self.shuffle(j) for j in dead_jobs]		
			

		return dead_jobs

	def is_over_capacity(self):
		return len(self.jobs) / self.capacity > 1

	def is_full(self):
		return len(self.jobs) / self.capacity >= 1

	def shuffle(self, query):
		# print self.id, query
		quanta_a, job_a = self.closest(query, -1)
		quanta_b, job_b = self.closest(query, 1)
		
		# print quanta_a or quanta_b
		if not (quanta_a or quanta_b):
			query.metadata.hardhit = True
			return query


		d = abs(quanta_a.id - self.id) if job_a else abs(quanta_b.id - self.id)
		is_full = quanta_a.is_full() if job_a else quanta_b.is_full()
		direction = -1 if job_a else 1
		job = job_a if job_a else job_b


		# print job.q_str(self.period), "TWEENED: ", d, d > 1 or not is_full

		if d > 1 or not is_full: 
			j = query.tween(job, d, direction, self.period, True) # make tweened job at quanta - 1
			return j

		if d == 1:
			# tween in between, replace the neighbor with tween 
			j = query.tween(job, d, direction, self.period, False)
			j.metadata.hardhit = True
			return j

	

	def update(self, priority_type = "pdf"):
		# get alpha value
		q = Queue.PriorityQueue(maxsize=0)
		for job in self.jobs: 
			q.put(job.set_priority(priority_type))
			
		compiled_commands = []
		while not q.empty():
			compiled_commands.append(q.get())

		self.jobs = compiled_commands


	def reject(self):
		self.update()
		dead_jobs = self.jobs[int(self.capacity):]
		for j in dead_jobs:
			# print j.metadata
			self.jobs.remove(j)
		return True



	def set_next(self, next):
		self.next = next


	def closest(self, query, direction):
		if direction == 1:
			node = self.next

			while node:
				closest_job = node.find(query)
				if  closest_job:
					return node, closest_job
				else:
					node = node.next
			
		else:
			node = self.prev
			while node:
				closest_job = node.find(query)
				if  closest_job:
					return node, closest_job
				else:
					node = node.prev
		return None, None

	def find(self, query):
		for j in self.jobs:
			if j.metadata.addr == query.metadata.addr:
				return j;
		
		return None;
