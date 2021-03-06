import pandas as pd
import seaborn as sns

titanic_train = pd.read_csv("C:/Users/Algorithmica/Downloads/all/train.csv")
print(titanic_train.shape)
print(titanic_train.info())

##univariate plots
#categorical columns: count plot
#x: categories of feature, y: frequency
sns.countplot(x='Survived',data=titanic_train)
sns.countplot(x='Pclass',data=titanic_train)
sns.countplot(x='Sex',data=titanic_train)

#histogram to undertand continuous feature
#x: bins of continuous data, y: frequency
#issue: how do you select number of bins?
sns.distplot(titanic_train['Fare'], kde=False)
sns.distplot(titanic_train['Fare'], bins=20, rug=True, kde=False)
sns.distplot(titanic_train['Fare'], bins=100, kde=False)
#denseplot to understand continuous feature
#it doesnt require bins argument
sns.distplot(titanic_train['Fare'], hist=False)
sns.distplot(titanic_train['Fare'])
#box-whisker plot to understand continuous feature
sns.boxplot(x='Fare',data=titanic_train)

##bivariate plots
#categorical vs categorical 
sns.factorplot(x="Sex", hue="Survived", data=titanic_train, kind="count", size=6)
sns.factorplot(x="Pclass", hue="Survived", data=titanic_train, kind="count", size=6)
sns.factorplot(x="Embarked", hue="Survived", data=titanic_train, kind="count", size=6)

#continuous vs categorical
sns.FacetGrid(titanic_train, hue="Survived",size=8).map(sns.kdeplot, "Fare").add_legend()
sns.FacetGrid(titanic_train, hue="Survived",size=8).map(sns.kdeplot, "Age").add_legend()

#understand grid cell formation
#grid cells along column
g = sns.FacetGrid(titanic_train, col="Sex") 
g.map(sns.kdeplot, "Age")
#grid cells along row
g = sns.FacetGrid(titanic_train, row="Sex") 
g.map(sns.kdeplot, "Age")
#single grid cell but color separation
g = sns.FacetGrid(titanic_train, hue="Sex") 
g.map(sns.kdeplot, "Age")
#grid cells along row and column 
g = sns.FacetGrid(titanic_train, row="Sex", col="Pclass") 

##multi-variate plots
#3-categorical features
g = sns.FacetGrid(titanic_train, row="Sex", col="Pclass") 
g.map(sns.countplot, "Survived")
g = sns.FacetGrid(titanic_train, row="Sex", col="Embarked") 
g.map(sns.countplot, "Survived")

#2-categorical variables & 1-continuous
g = sns.FacetGrid(titanic_train, row="Pclass", col="Sex", hue="Survived") 
g.map(sns.kdeplot, "Fare")

#is age have an impact on survived for each pclass and sex group?
g = sns.FacetGrid(titanic_train, row="Pclass", col="Sex", hue="Survived") 
g.map(sns.kdeplot, "Age")

titanic_test = pd.read_csv("C:/Users/Algorithmica/Downloads/all/test.csv")
print(titanic_test.shape)
titanic_test['Survived'] = 0
titanic_test.loc[titanic_test['Sex'] == 'female', 'Survived'] = 1
titanic_test.loc[titanic_test['Age'] <= 15, 'Survived'] = 1
titanic_test.loc[titanic_test['Fare'] >= 30, 'Survived'] = 1

titanic_test.to_csv("C:/Users/Algorithmica/Downloads/all/submission.csv", columns=['PassengerId', 'Survived'], index=False)
