# Top-New-York-Providers-Depression-Screening
This code uses data collected for the Physician Quality Reporting System to identify the best medical practices in NY at screening for depression. 

The data can be collected at the following URLs:
  Physician Compare National Downloadable File - https://data.medicare.gov/Physician-Compare/Physician-Compare-National-Downloadable-File/mj5m-pzi6
  Physician Compare 2014 Individual EP Public Reporting - https://data.medicare.gov/Physician-Compare/Physician-Compare-2014-Individual-EP-Public-Report/wbjt-9zks
  
The code prints out the top 10 providers in NY by the total amount of depression screening according to number of practitioners that screen and the percentage of patients they screen. This can easily be updated to alter the target state or amount of output. All of the data for specific practitioners can be identified using "screenProviderJoin2.loc[screenProviderJoin2['Group Practice PAC ID'] == 1355395179]" and changing the PAC ID to select the provider of interest.
