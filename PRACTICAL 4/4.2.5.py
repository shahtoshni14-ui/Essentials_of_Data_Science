# import pandas as pd
# import numpy as np

# # Load the Titanic dataset
# data = pd.read_csv('Titanic-Dataset.csv')

import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')


print(data.head())


print(data.tail())



print(data.shape)

print(data.info())



print(data.describe())

print(data.isnull().sum())


data['Age'].fillna(data['Age'].median(),inplace=True)


data['Embarked'].fillna(data['Embarked'].mode(),inplace=True)


data.drop('Cabin',axis=1,inplace=True)


data['FamilySize']=data['SibSp'] + data['Parch']


# import pandas as pd
# import numpy as np

# # Load the Titanic dataset
# data = pd.read_csv('Titanic-Dataset.csv')

# # 1. Display the first 5 rows of the dataset


# # 2. Display the last 5 rows of the dataset


# # 3. Get the shape of the dataset


# # 4. Get a summary of the dataset (info)


# # 5. Get basic statistics of the dataset


# # 6. Check for missing values


# # 7. Fill missing values in the ‘Age’ column with the median age


# # 8. Fill missing values in the ‘Embarked’ column with the mode


# # 9. Drop the ‘Cabin’ column due to many missing values


# # 10. Create a new column 'FamilySize’ by adding ‘SibSp' and ‘Parch'
