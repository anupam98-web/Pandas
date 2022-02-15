import pandas as pd
import numpy as np
import os
import glob
from datetime import datetime
from dateutil.relativedelta import relativedelta


path = os.getcwd()
excel_files = glob.glob(os.path.join(path, "*.xlsx"))
dff = []
for f in excel_files:
    # read the csv file
    df = pd.read_excel(f)
    dff.append(df)

maindf = pd.concat(dff).drop_duplicates()
print(maindf.shape)
a = list(set(maindf['ASSIGNMENT_ID']))
a.sort
assignmentID = {}
assignment_count = 40000
for i in a:
    assignmentID[i] = assignment_count
    assignment_count = assignment_count + 1



pd.DataFrame(assignmentID.items(), columns=['ASSIGNMENT_ID', 'DateValue']).to_csv('assignmentIDmathcingNonMPG.csv',index=False)
# #clientmap = pd.read_csv('clientidmathcing.csv')
candmap = pd.read_csv('candidmathcing.csv')
canddict = dict(zip(candmap.CANDIDATE_ID, candmap.DummyCandidateID))
# #jobdict = dict(zip(jobmap.JOB_ID, jobmap.DummyJobID))


def dataframe(df, name):
        df['Dummy_ASSIGNMENT_ID'] = df['ASSIGNMENT_ID'].map(assignmentID)
        # #df['Dummy_CLIENT_ID'] = df['CLIENT_ID'].map(clientdict)
        # #df['Dummy_JOB_ID'] = df['JOB_ID'].map(jobdict)
        df['Dummy_CANDIDATE_ID'] = df['CANDIDATE_ID'].map(canddict)

        df.drop(columns=['ASSIGNMENT_ID', 'CANDIDATE_ID'], inplace = True)
        df.rename(columns = {'Dummy_ASSIGNMENT_ID': 'ASSIGNMENT_ID','Dummy_CANDIDATE_ID':'CANDIDATE_ID'}, inplace = True)
        df['DATE_OF_BIRTH'] = pd.to_datetime(df['DATE_OF_BIRTH'])
        for i, r in df.iterrows():
                if r['DATE_OF_BIRTH'].year > 2022:
                        #print(r['DATE_OF_BIRTH'])
                        df.at[i, 'DATE_OF_BIRTH'] = r['DATE_OF_BIRTH'].replace(year=r['DATE_OF_BIRTH'].year-100)
                        #print(r['DATE_OF_BIRTH'])
        df['Current Date'] = datetime.today().date()
        df['Current Date'] = pd.to_datetime(df['Current Date'])
        df['age'] = np.floor((df['Current Date'] - df['DATE_OF_BIRTH']).dt.days/365.25)
        #df['age'] = (np.floor(df['Age'].dt.days / 365.25)).astype(int)
        def myround(x, base=5):
                 return base * round(x/base)
        df = df.assign(Age = lambda x: myround(x['age']))        
        print(df[['DATE_OF_BIRTH','Current Date','Age','age']])
        df.drop(columns=['DATE_OF_BIRTH', 'Current Date', 'age'], inplace = True)


        # df['Age'] = df['Age'].apply(lambda x: myround(x))
        df.to_excel(name, index = False)


path = os.getcwd()
excel_files = glob.glob(os.path.join(path, "*.xlsx"))
dff = []
for f in excel_files:
    # read the csv file
    df = pd.read_excel(f)
    dataframe(df,'Dummy_'+str(f.split("\\")[-1]))
    # need to pass according to the folder
