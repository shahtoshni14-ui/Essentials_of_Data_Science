import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']


# # 1. Create a new column ‘IsAlone' (1 if alone, 0 otherwise)


# # 2. Convert ‘Sex' to numeric (male: 0, female: 1)


# # 3. One-hot encode the ‘Embarked' column


# # 4. Get the mean age of passengers



# # 5. Get the median fare of passengers



# # 6. Get the number of passengers by class



# # 7. Get the number of passengers by gender



# # 8. Get the number of passengers by survival status



# # 9. Calculate the survival rate



# # 10. Calculate the survival rate by gender



# # 1. Create a new column ‘IsAlone' (1 if alone, 0 otherwise)


# # 2. Convert ‘Sex' to numeric (male: 0, female: 1)


# # 3. One-hot encode the ‘Embarked' column


# # 4. Get the mean age of passengers



# # 5. Get the median fare of passengers



# # 6. Get the number of passengers by class



# # 7. Get the number of passengers by gender



# # 8. Get the number of passengers by survival status



# # 9. Calculate the survival rate



# # 10. Calculate the survival rate by gender





import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']


data['IsAlone']= np.where(data['FamilySize'] > 0, 0, 1)


data['Sex']=data['Sex'].map({'male': 0, 'female': 1})



data=pd.get_dummies (data, columns=['Embarked'], drop_first=True)


print(data['Age'].mean())


print(data['Fare'].median())

print(data['Pclass'].value_counts())

print(data['Sex'].value_counts())



print(data['Survived'].value_counts())



print(data['Survived'].mean())


print(data.groupby('Sex') ['Survived'].mean())




# import pandas as pd
# import numpy as np

# # Load the Titanic dataset
# data = pd.read_csv('Titanic-Dataset.csv')
# data['FamilySize'] = data['SibSp'] + data['Parch']

# # 1. Create a new column ‘IsAlone' (1 if alone, 0 otherwise)


# # 2. Convert ‘Sex' to numeric (male: 0, female: 1)


# # 3. One-hot encode the ‘Embarked' column


# # 4. Get the mean age of passengers



# # 5. Get the median fare of passengers



# # 6. Get the number of passengers by class



# # 7. Get the number of passengers by gender



# # 8. Get the number of passengers by survival status



# # 9. Calculate the survival rate



# # 10. Calculate the survival rate by gender


