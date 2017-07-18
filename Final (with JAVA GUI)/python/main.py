from CNN import CNN
from DataSet import *
import os
cwd = os.getcwd()
print cwd
# A folder will contain multiple folders, each for one class of data.
# For those classes, name will be considered as class name



ds=DataSet.prepare_from_folder(cwd+"/dataset", height=40, width=40)



cnn=CNN(ds.__shape__, ds.__classes__)
cnn.load('model')




# Display

all_images = ['name', 'mob', 'dob', 'nid', 'mail']

file1 = open('output.txt','w') 


for str in all_images:
    pred = cnn.predict(DataSet.readImageToPhoto(40, 40, str+'.png'))
    for i in pred:
        file1.write(ds.classnames[i])
    
    file1.write('\n') 
	

file1.close()
