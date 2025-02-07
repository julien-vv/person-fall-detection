FILE INFORMATION

	- README.txt: to know more about our project
	- falltracker.h5: this is our final model created by training that will be use to see the final result of our project
	- FallDetection.ipynb & FallFetection.py: these are Python file to run with or without Jupyter Notebook to see our final result
	- .ipynb_checkpoints: this file is important to run FallDetection.ipynb in Jupyter Notebook
	- ModelCreation.ipynb: this file is show to you to understand how we have train our model 
	- Data: there are files for images and labels
	- aug_data: This is a file that you will be use for create your trainning model
	- bonus with the file CSV_ACCELERATION and CSV_ELDERLY: two bonus file which are studies that we have done in parallel to our fall recognition 
	  by deep learning. We did not keep these studies because the data are too perfect and prevent us from an interesting analysis for the CSV_ELDERLY file 
	  and for the second file, we did not push the study enough to do the main work


SEE OUR RESULT

	1) Install OpenCV, Tensorflow and Numpy in the command shell:
		$ pip install opencv-python
		$ pip install tensorflow
		$ pip install numpy

	2) Setup your webcam

	3) Open the file FallDetection.py or FallDetection.ipynb and run it, a window will be open

	4) This window show you what your webcam see by a rectangle around the person: 
		- a red rectangle if the person is fall
		- a green rectangle if the person is not fall

	5) If you want to stop the program, press 'q'


