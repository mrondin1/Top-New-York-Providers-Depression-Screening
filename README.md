# Top-New-York-Providers-Depression-Screening
This code uses data collected for the Physician Quality Reporting System to identify the 10 best medical practices in NY at screening for depression. 

The data can be collected at the following URLs:
  * Physician Compare National Downloadable File - https://data.medicare.gov/Physician-Compare/Physician-Compare-National-Downloadable-File/mj5m-pzi6
  * Physician Compare 2014 Individual EP Public Reporting - https://data.medicare.gov/Physician-Compare/Physician-Compare-2014-Individual-EP-Public-Report/wbjt-9zks
  The data should be placed in the same directory as the python file to run.
  
  
Group Practice PAC ID	| Organization legal name |	Screening for depression and developing a follow-up plan. |	Contact
--- | --- | --- | --- 
1355395179	| FOX REHABILITATION PHYSICAL THERAPY SERVICES LLC	|	1045|	Robyn Kjar, DPT
9537213079|	GENERAL PHYSICIAN, PC	|	757|	Thomas McTernan, MD
8820070105|	ON-SITE PSYCHOLOGICAL SERVICES PC	|	700|	Stephen Buckley, PhD
5193800779|	AMHERST MEDICAL ASSOCIATES, LLP	|	470|	Steven Stone, MD
7416860572|	PSYCHOLOGICAL HEALTHCARE, PLLC	|	400|	Joel Richman, PhD
3375434970|	STONY BROOK ANAESTHESIOLOGY UNIVERSITY FACULTY...	|	344|	Tong Joo (TJ) Gan, MD
2365494861|	DAWN FRIEDLAND-PEREZ LCSW,PC|	300|	Dawn Friedland-Perez, LCSW, PC
9931164845|	EDWARD J. JACOBS, MD., SEAN Y. LEE, M.D. AND C...|	252|	Sean Y. Lee, MD
5597908202|	CNY SPINE AND PAIN MEDICINE LLC|	243|	Martin Schaeffer, MD
1557416997|	AHAVA MEDICAL AND REHABILITATION CENTER, LLC|	200|	June Mossop, PhD

The contact column in the results above is not an output of the code, and was added manually.

The results above show the top ten practices in New York based on screening for depression. The values in the “Screening for depression” column are calculated as the sum of the individual scores for each practitioner within the practice. Those individual scores (obtained from the individual EP Public Reporting Data) represent the percent of visits in which the practitioner screened the patient for depression. Thus, a practice-wide score of 400 may represent four practitioners that screen for depression 100% of the time, or eight practitioners that screen for depression 50% of the time. While I gave consideration to calculating practice-wide score based on average, not sum, I believe that using sum is the correct method to identify the practices that are screening the most patients for depression overall. 

I first looked a a different dataset that included data for depression screening on a group practice level (https://data.medicare.gov/Physician-Compare/Physician-Compare-2014-Group-Practice-Public-Repor/t6ug-wt53), but using this dataset was more limited than combining the two datasets above (only eight total practices had scores for depression screening). 

The code can easily be updated to alter the target state or amount of output. All of the data for specific practitioners can be identified using "screenProviderJoin2.loc[screenProviderJoin2['Group Practice PAC ID'] == 1355395179]" and changing the PAC ID to select the provider of interest.
