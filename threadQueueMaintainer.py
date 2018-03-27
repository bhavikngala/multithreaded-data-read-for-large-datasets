from queue import Queue
from worker import ReadWorker

class ThreadQueueMaintainer():

	def __init__(self, numWorkerThreads, numReadFiles):

		# number of worker threads
		self.numWorkerThreads = numWorkerThreads

		# number of files workers can read at a time
		self.numReadFiles = numReadFiles

		# list to store worker thread objects
		self.workerThreadsList = []

		# data Queue
		self.dataQueue = Queue()

		# data filename and class queue
		# TODO: implement loadDataFilenameClassIntoQueue()
		self.dataFilenameQueue = self.loadDataFilenameClassIntoQueue()

		# spawn numWorkerThreads threads
		for i in range(self.numWorkerThreads):
			# worker thread object
			readWorker = ReadWorker(
				self.dataQueue, 
				self.dataFilenameQueue, 
				self.numReadFiles)

			# set daemon True to avoid blocking main thread
			readWorker.daemon = True

			# start thread
			readWorker.start()

			# append the worker to the list of worker threads
			self.workerThreadsList.append(readWorker)

		self.dataQueue.join()
		self.dataFilenameQueue.join()