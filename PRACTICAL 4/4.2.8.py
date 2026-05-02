import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 1. Get the number of survivors by gender


# 2. Get the number of non-survivors by gender


# 3. Get the number of survivors by embarked location


# 4. Get the number of non-survivors by embarked location


# 5. Calculate the percentage of children (Age < 18) who survived


# 6. Calculate the percentage of adults (Age >= 18) who survived


# 7. Get the median age of survivors


# 8. Get the median age of non-survivors


# 9. Get the median fare of survivors

import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)



print(data[data['Survived'] == 1] ['Sex'].value_counts())

print(data[data['Survived'] == 0] ['Sex'].value_counts())

print(data[data['Survived'] == 1]['Embarked_S'].value_counts())

print(data[data['Survived'] == 0]['Embarked_S'].value_counts())


children=data[data['Age'] < 18]
per=children['Survived'].mean()
print(per)
children['Survived'].mean()

adults=data[data['Age'] >= 18]['Survived'].mean()
print(adults)

print(data[data['Survived'] == 1] ['Age'].median())

print(data[data['Survived'] == 0] ['Age'].median())


print(data[data['Survived'] == 1] ['Fare'].median())

print(data[data['Survived']== 0]['Fare'].median())


# import pandas as pd
# import numpy as np

# # Load the Titanic dataset
# data = pd.read_csv('Titanic-Dataset.csv')
# data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)


# # 1. Get the number of survivors by gender


# # 2. Get the number of non-survivors by gender


# # 3. Get the number of survivors by embarked location


# # 4. Get the number of non-survivors by embarked location


# # 5. Calculate the percentage of children (Age < 18) who survived


# # 6. Calculate the percentage of adults (Age >= 18) who survived


# # 7. Get the median age of survivors


# # 8. Get the median age of non-survivors


# # 9. Get the median fare of survivors


# # 10. Get the median fare of non-survivors


# 10. Get the median fare of non-survivors

