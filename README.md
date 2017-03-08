# Top-New-York-Providers-Depression-Screening
This code uses data collected for the Physician Quality Reporting System to identify the 10 best medical practices in NY at screening for depression. 

The data can be collected at the following URLs:
  * Physician Compare National Downloadable File - https://data.medicare.gov/Physician-Compare/Physician-Compare-National-Downloadable-File/mj5m-pzi6
  * Physician Compare 2014 Individual EP Public Reporting - https://data.medicare.gov/Physician-Compare/Physician-Compare-2014-Individual-EP-Public-Report/wbjt-9zks

The data should be placed in the same directory as the python file to run.
  
  
Group Practice PAC ID	| Organization legal name |	Screening for depression and developing a follow-up plan. |	Contact | Contact Info
--- | --- | --- | --- | ---
1355395179	| FOX REHABILITATION PHYSICAL THERAPY SERVICES LLC	|	1045|	Robyn Kjar, DPT | 877-407-3422 
9537213079|	GENERAL PHYSICIAN, PC	|	757|	Thomas McTernan, MD | 716-363-6960
8820070105|	ON-SITE PSYCHOLOGICAL SERVICES PC	|	700|	Stephen Buckley, PhD | onsitepsy@cshore.com, 203-438-7565
5193800779|	AMHERST MEDICAL ASSOCIATES, LLP	|	470|	Steven Stone, MD | 716-834-4266
7416860572|	PSYCHOLOGICAL HEALTHCARE, PLLC	|	400|	Joel Richman, PhD | hr@phcny.com, 315-422-0300 
3375434970|	STONY BROOK ANAESTHESIOLOGY UNIVERSITY FACULTY...	|	344|	Tong Joo (TJ) Gan, MD | Tong.Gan@stonybrookmedicine.edu, 631-444-2975
2365494861|	DAWN FRIEDLAND-PEREZ LCSW,PC|	300|	Dawn Friedland-Perez, LCSW, PC | 631-331-2690
9931164845|	EDWARD J. JACOBS, MD., SEAN Y. LEE, M.D. AND C...|	252|	Sean Y. Lee, MD | 518-465-3318 
5597908202|	CNY SPINE AND PAIN MEDICINE LLC|	243|	Martin Schaeffer, MD | 315-451-5400
1557416997|	AHAVA MEDICAL AND REHABILITATION CENTER, LLC|	200|	June Mossop, PhD | 718-951-8800

The contact column in the results above is not an output of the code, and was added manually.

The results above show the top ten practices in New York based on screening for depression. The values in the “Screening for depression” column are calculated as the sum of the individual scores for each practitioner within the practice. Those individual scores (obtained from the individual EP Public Reporting Data) represent the percent of visits in which the practitioner screened the patient for depression. Thus, a practice-wide score of 400 may represent four practitioners that screen for depression 100% of the time, or eight practitioners that screen for depression 50% of the time. While I gave consideration to calculating practice-wide score based on average, not sum, I believe that using sum is the correct method to identify the practices that are screening the most patients for depression overall. 

I first looked at a different dataset that included data for depression screening on a group practice level (https://data.medicare.gov/Physician-Compare/Physician-Compare-2014-Group-Practice-Public-Repor/t6ug-wt53), but using this dataset was more limited than combining the two datasets above (only eight total practices had scores for depression screening). 

The code can easily be updated to alter the target state or amount of output. All of the data for specific practitioners can be identified using "screenProviderJoin2.loc[screenProviderJoin2['Group Practice PAC ID'] == 1355395179]" and changing the PAC ID to select the provider of interest.

# Follow up

Email Draft:

Hi ______,

My name is Mike Rondinaro and I am reaching out on behalf of Spring Care, Inc. (www.spring.care). We are a behavioral healthcare start-up that uses machine learning technology to assist clinicians in making depression treatment decisions with a ten minute questionnaire. Founded out of Yale University, our work has been featured in The Lancet and Crain's, among other publications. We identified your practice as a top performer in depression screening using data from the Medicare Physician Quality Reporting System. Please let me know if you are free for a phone call to discuss your depression screening procedures and your needs, if any, for improving this process. 

Sincerely,

Mike


