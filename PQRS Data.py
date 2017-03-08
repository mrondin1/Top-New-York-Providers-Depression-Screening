import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

#read in data on all practitioners and their affiliated practices 
#available for download here: https://data.medicare.gov/Physician-Compare/Physician-Compare-National-Downloadable-File/mj5m-pzi6
providerData = pd.read_csv(dir_path+'/Physician_Compare_National_Downloadable_File.csv')

#select all providers based in NY
providerDataNY = providerData.loc[providerData['State']=='NY']

#read in data on practitioners and what they screen for 
#available for download here: https://data.medicare.gov/Physician-Compare/Physician-Compare-2014-Individual-EP-Public-Report/wbjt-9zks
screeningData = pd.read_csv(dir_path+'/Physician_Compare_2014_Individual_EP_Public_Reporting_-_Clinical_Quality_Of_Care.csv')

#select all providers who have depression screening data
screeningDataDepression = screeningData.loc[screeningData['Screening for depression and developing a follow-up plan.']>0]

#select all providers based in NY who have depression screening data 
screeningDataNY = screeningDataDepression[screeningDataDepression['NPI'].isin(providerDataNY['NPI'])]

#join invididual practitioner data to group practice data on 'NPI' 
screenProviderJoin = screeningDataNY.join(providerDataNY.set_index(['NPI','PAC ID','Last Name','First Name']),on=['NPI','PAC ID','Last Name','First Name'],how='left')

#drop duplicates of same practitioner, same practice (but keep duplicates of same practitioner, different practice)
screenProviderJoin2 = screenProviderJoin.drop_duplicates(subset=['NPI','Group Practice PAC ID'])

#sum the screening number for each person at the same practice
#(the logic here being that a practice with two practitioners who each screen for depression 60% of the time
#is better than one practitioner who screens 100% of the time)
screenProviderDepressionSum = screenProviderJoin2.groupby(['Group Practice PAC ID','Organization legal name','State'], as_index=False)['Screening for depression and developing a follow-up plan.'].sum()

#order by top depression screening
screenProviderDepressionSumRank = screenProviderDepressionSum.sort(columns='Screening for depression and developing a follow-up plan.',ascending=False)

#grab top 10 practices 
screenProviderDepressionTop10 = screenProviderDepressionSumRank[0:10]

print screenProviderDepressionTop10






