#1 Create a folder on the desktop, open your vs code then go to file, open folder and select the folder you created.
#2 Create the virtual environment: python -m venv venv
#3 Activate the scripts: venv/Scripts/activate
#4 install the modules, e.g numpy or  scikit-learn: pip install numpy 
# pip install scikit-learn

#5 Create requirements file: pip freeze > requirements.txt
#6 install the requirements: pip install -r requirements.txt

#7 Since we are working with python, create a file name then put the extension .py. Example model.py
from sklearn.cluster import KMeans
#Preparing Data
students=[
    [1,2],
    [2,1],
    [2,3],
    [5,6],
    [6,5],
    [6,7],
    [9,9],
    [10,8],
    [9,10]
]

#Create Model
models=KMeans(n_clusters=3)

#Train Model
models.fit(students)

#Predict the clusters
predictions=models.predict(students)
print("clusters in assignments:", predictions)

#create readable
for i in range(len(students)):
    print('students',i+1, 'belongs to cluster', predictions[i])