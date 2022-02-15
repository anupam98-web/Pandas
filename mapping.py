import pandas as pd
import numpy as np
import glob
import os

path = os.getcwd()
excel_files = glob.glob(os.path.join(path, "*.xlsx"))
dff = []
final_shape = 0
for f in excel_files:
    # read the csv file
    df = pd.read_excel(f)
    #print(df.shape)
    final_shape = final_shape + int(df.shape[0])
    dff.append(df)

maindf = pd.concat(dff).drop_duplicates()
print(final_shape)
print(maindf.shape)

assignmentID = {}
assignment_count = 200000
for i in list(set(maindf['ASSIGNMENT_ID'])).sort():
    assignmentID[i] = assignment_count
    assignment_count = assignment_count + 1

clientID = {}
client_count = 10000
for i in list(set(maindf['CLIENT_ID'])).sort():
    clientID[i] = client_count
    client_count = client_count + 1


candidateID = {}
candidate_count = 600000
for i in list(set(maindf['CANDIDATE_ID'])).sort():
    candidateID[i] = candidate_count
    candidate_count = candidate_count + 1

jobID = {}
job_count = 50000
for i in list(set(maindf['JOB_ID'])).sort():
    jobID[i] = job_count
    job_count = job_count + 1

pd.DataFrame(jobID.items(), columns=['JOB_ID', 'DummyJobID']).to_csv('JM.csv',index=False)
pd.DataFrame(candidateID.items(), columns=['CANDIDATE_ID', 'DummyCandidateID']).to_csv('CaM.csv',index=False)
pd.DataFrame(clientID.items(), columns=['CLIENT_ID', 'DateValue']).to_csv('C.csv',index=False)
pd.DataFrame(assignmentID.items(), columns=['ASSIGNMENT_ID', 'DateValue']).to_csv('A.csv',index=False)
