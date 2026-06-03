import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)


###################################################################
# Step 1 : Load the data
###################################################################

Border  = "-"*45
print(Border)
print("Loading The Dataset ...")
print(Border)

Datasetpath = "iris.csv"

df = pd.read_csv(Datasetpath)

print("Data Gets Loaded Successfully")
print("Intial Entries From Dataset")
print(df.head())

##########################################################################
#  STEP 2 : Analysize The DataSet
##########################################################################

print(Border)
print("Step 2 : Analysize The Dataset")
print(Border)

print(df.shape)             # 150 * 5
print("Column Names : ", list(df.columns))  # list of colummns
print("Missing Values Per Column")
print(df.isnull().sum())            # Summaton of empty fields per colunmn
print("Class Destribution (Species Count)")
print(df["species"].value_counts())     # Count Values of species (setosa,versicolor,verginica)

##########################################################################
#  STEP 3 : Decide Independant And Dependant Varaiables
##########################################################################

print(Border)
print("Step 3 : Decide Independant and Dependant Variables")
print(Border)

# X = Independant Variables / features
# Y = Dependant Variables / labels

feature_cols = [
    "sepal.length (cm)",
    "sepal.width (cm)",
    "petal.length (cm)",
    "petal.width (cm)"
]

X = df[feature_cols]        # Seperated features / Independant Variables
Y = df["species"]           # Seperated labels / dependant Variables

print("X shape :", X.shape) # 150 , 4
print("Y: ",Y.shape)        # 150, 

##########################################################################
#  STEP 4 : Visualiasation Of Dataset
##########################################################################

print(Border)
print("Step 4 : Visualisation of dataset")
print(Border)

plt.figure(figsize = (7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal.length (cm)"],temp["petal.width (cm)"], label = sp)  # First Property autmatically is on Xaxis

plt.title("Iris : Petal Length vs Petal Width") # Gives Title to the chart

plt.xlabel("petal.length (cm)")       # Name of xaxis
plt.ylabel("petal.width (cm)")        # Name of yaxis

plt.legend()
plt.grid(True)      # For gird lines
plt.show()

##########################################################################
#  STEP 5 : Split The Dataset of Training And Testing
##########################################################################

print(Border)
print("Step 5 : Spliting Dataset of Training And Testing")
print(Border)

# Total Dataset = 150, 5

# X = 150,4
# Y = 150,

# Testing Size = 20%
# Training Size = 80%

Xtrain, Xtest, Ytrain, Ytest = train_test_split(
    X,
    Y,
    test_size= 0.5,             # Ytest = 30 records
    random_state= 42        # Shuffle the data
)

print("Data Spliting Activity Done")

print("X - Independant Variable", X.shape) # 150,4
print("Y - dependant Variable : ", Y.shape) #150

print("Values after Spliting")
print("X_train : ", Xtrain.shape)   # (120,4)
print("X_test : ", Xtest.shape)     # (30,4)

print("Y_test : ", Ytrain.shape)    # (120,)
print("Y_test : ", Ytest.shape)     # (30,)

##########################################################################
#  STEP 6 : Build The Model
##########################################################################

print(Border)
print("Step 6 : Building the Model")
print(Border)

model = DecisionTreeClassifier(
    criterion = "gini",
    max_depth = 5,
    random_state = 42
)

print("Model Successfully Created")

##########################################################################
#  STEP 7 : Train The Model
##########################################################################

print(Border)
print("Step 7 : Train The Model")
print(Border)

model.fit(Xtrain,Ytrain)
print("Model Training Completed")

##########################################################################
#  STEP 8 : Test The Model (Evaluate)
##########################################################################

print(Border)
print("Step 8 : Evaluate The Model")
print(Border)

Ypred = model.predict(Xtest)
print("Model Evaluation is completed")

print("Expected Answers : ")
print(list(Ytest))

print("Predicted Answers : ")
print(Ypred)

##########################################################################
#  STEP 9 : Evaluate The Model Performance
##########################################################################

print(Border)
print("Step 9 : Evaluate The Model Performance")
print(Border)

accuracy = accuracy_score(Ytest,Ypred)

print("The Model Accuracy is : ", accuracy*100)

cm = confusion_matrix(Ytest,Ypred)

print("Confusion Matrix")

print("Classification Report")
print(classification_report(Ytest,Ypred))

##########################################################################
#  STEP 10 : Plot Confusion Matrix
##########################################################################

print(Border)
print("Step 10 : Plot The Confusion Matrix")
print(Border)

data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
data.plot()
plt.title("Confusion Matrix Of Iris")
plt.show()