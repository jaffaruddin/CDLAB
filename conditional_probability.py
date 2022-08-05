# conditional probablity
import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/KMITDS/CS601PC/main/individual.csv")
print("P(recreation=golf)")
print(df[(df.recreation=='golf')].shape[0]/df.shape[0])
print("P(status=single/credit-worthiness=medRisk)")
print(df[(df.status=='single') & (df.cw=='medRisk')].shape[0]/df[(df.cw=='medRisk')].shape[0])

-> o/p:

P(recreation=golf)
0.4
P(status=single/credit-worthiness=medRisk)
0.6666666666666666
