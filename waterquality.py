import pandas as pd
from sklearn.linear_model import LogisticRegression
def fun(ans):
    df=pd.read_csv("water_potability.csv")
    df.head()
    df.shape

    df.info()

    df.isnull().sum()
    df.describe()
    fill=['ph','Sulfate','Trihalomethanes']
    for i in fill:
        df[i].fillna(value=df[i].mean(),inplace=True)
    df.isnull().sum()
    df.describe()

    df.hist(figsize=[10,10])
    X=['ph','Hardness','Solids','Chloramines','Sulfate','Conductivity','Organic_carbon','Trihalomethanes','Turbidity']
    Y=['Potability']

    model=LogisticRegression()

    model.fit(df[X],df[Y])
    return model.predict(ans)