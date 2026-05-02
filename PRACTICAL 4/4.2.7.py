import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']
data['IsAlone'] = np.where(data['FamilySize'] > 0, 0, 1)
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 1. Calculate the survival rate by class


# 2. Calculate the survival rate by embarked location


# 3. Calculate the survival rate by family size


# 4. Calculate the survival rate by being alone


# 5. Get the average fare by class


# 6. Get the average age by class


# 7. Get the average age by survival status


# 8. Get the average fare by survival status


# 9. Get the number of survivors by class


# 10. Get the number of non-survivors by class
import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data['FamilySize'] = data['SibSp'] + data['Parch']
data['IsAlone'] = np.where(data['FamilySize'] > 0, 0, 1)
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)


print(data.groupby ('Pclass') ['Survived'].mean())

print(data.groupby('Embarked_S') ['Survived'].mean())


print(data.groupby('FamilySize') ['Survived'].mean())

print(data.groupby ('IsAlone') ['Survived'].mean())


print(data.groupby ('Pclass') ['Fare'].mean())


print(data.groupby ('Pclass') ['Age'].mean())


print(data.groupby('Survived')['Age'].mean())

print(data.groupby('Survived') ['Fare'].mean())

print(data[data['Survived'] == 1] ['Pclass'].value_counts())


print(data[data['Survived']==0]['Pclass'].value_counts())
