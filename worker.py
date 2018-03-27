from threading import Thread

class ReadWorker(Thread):

	def __init__(self, dataQueue, dataFilenameQueue, numReadFiles):
		
		Thread.__init__(self)
		
		# read data and put into this queue
		self.dataQueue = dataQueue

		# read filenames of data from this queue
		self.dataFilenameQueue = dataFilenameQueue
		
		# read data if flag is set
		self.readData = True

		# number of data files to read at a time
		self.numReadFiles = numReadFiles

		# thread termination signal flag
		# when set the thread should terminate
		self.terminateThread = False

	def run(self):

		while True:
			# read data into queue if flag is set
			if self.readData:
				# read numReadFiles items into queue
				for i in range(self.numReadFiles):
					# if queue is not empty read data
					if not self.dataFilenameQueue.empty():
						# unpacking filepath and data class tuple
						filePath, dataClass = self.dataFilenameQueue.get()

						# TODO read data
						data = readData(filepath)

						# put the data and its class into dataQueue
						self.dataQueue.put((data, dataClass))

						# give task complete signal
						self.dataFilenameQueue.task_done()

				# set readData flag False, to indicate reading task is completed
				self.readData = False
			else:
				self.sleep(100)

			# terminate thread on receivin signal
			if terminateThread:
				break

	# setter function to set readData flag True
	def setReadDataFlag(True):
		self.readData = True

def readData(filepath):
	return filepath