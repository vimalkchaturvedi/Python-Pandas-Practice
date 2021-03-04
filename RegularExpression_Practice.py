import re

def logs():
    example_dict = dict()
    example_list = list()
    with open("assets/logdata.txt", "r") as file:
        for line in file:
            m = re.search('''([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)\s*-\s*([a-z0-9]*|-)\s*\[(.*)\]\s*\"(.*)\"''', line)
            #print(m.group(4))
            example_dict["host"] = m.group(1)   #groups are marked with () # m.group(0) matches the complete line 
            example_dict["user_name"] = m.group(2)
            example_dict["time"] = m.group(3)
            example_dict["request"] = m.group(4)
            example_list.append(example_dict.copy())  #example_list.append(example_dict) will pass by reference and all the items in the list will havve the item of the loop
            #print(example_list)
            
    return example_list


assert len(logs()) == 979

one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"


#-----------------------------------------------


146.204.224.152 - feest6811 [21/Jun/2019:15:45:24 -0700] "POST /incentivize HTTP/1.1" 302 4622
197.109.77.178 - kertzmann3129 [21/Jun/2019:15:45:25 -0700] "DELETE /virtual/solutions/target/web+services HTTP/2.0" 203 26554
156.127.178.177 - okuneva5222 [21/Jun/2019:15:45:27 -0700] "DELETE /interactive/transparent/niches/revolutionize HTTP/1.1" 416 14701
100.32.205.59 - ortiz8891 [21/Jun/2019:15:45:28 -0700] "PATCH /architectures HTTP/1.0" 204 6048
168.95.156.240 - stark2413 [21/Jun/2019:15:45:31 -0700] "GET /engage HTTP/2.0" 201 9645
71.172.239.195 - dooley1853 [21/Jun/2019:15:45:32 -0700] "PUT /cutting-edge HTTP/2.0" 406 24498
180.95.121.94 - mohr6893 [21/Jun/2019:15:45:34 -0700] "PATCH /extensible/reinvent HTTP/1.1" 201 27330
144.23.247.108 - auer7552 [21/Jun/2019:15:45:35 -0700] "POST /extensible/infrastructures/one-to-one/enterprise HTTP/1.1" 100 22921
2.179.103.97 - lind8584 [21/Jun/2019:15:45:36 -0700] "POST /grow/front-end/e-commerce/robust HTTP/2.0" 304 14641
241.114.184.133 - tromp8355 [21/Jun/2019:15:45:37 -0700] "GET /redefine/orchestrate HTTP/1.0" 204 29059
224.188.38.4 - keebler1423 [21/Jun/2019:15:45:40 -0700] "PUT /orchestrate/out-of-the-box/unleash/syndicate HTTP/1.1" 404 28211
94.11.36.112 - klein8508 [21/Jun/2019:15:45:41 -0700] "POST /enhance/solutions/bricks-and-clicks HTTP/1.1" 404 24768
126.196.238.197 - gusikowski9864 [21/Jun/2019:15:45:45 -0700] "DELETE /rich/reinvent HTTP/2.0" 405 7894
103.247.168.212 - medhurst2732 [21/Jun/2019:15:45:49 -0700] "HEAD /scale/global/leverage HTTP/1.0" 203 15844
57.86.153.68 - dubuque8645 [21/Jun/2019:15:45:50 -0700] "POST /innovative/roi/robust/systems HTTP/1.1" 406 29046
231.220.8.214 - luettgen1860 [21/Jun/2019:15:45:52 -0700] "HEAD /systems/sexy HTTP/1.1" 201 2578
219.133.7.154 - price5585 [21/Jun/2019:15:45:53 -0700] "GET /incubate/incubate HTTP/1.1" 201 12126
159.252.184.44 - fay7852 [21/Jun/2019:15:45:54 -0700] "GET /convergence HTTP/2.0" 404 23856
40.167.172.66 - kshlerin3090 [21/Jun/2019:15:45:57 -0700] "HEAD /convergence HTTP/2.0" 501 16287
167.153.239.72 - schaden8853 [21/Jun/2019:15:45:58 -0700] "DELETE /bandwidth/reintermediate/engage HTTP/2.0" 302 17774
115.214.173.248 - hauck8214 [21/Jun/2019:15:46:00 -0700] "PUT /optimize HTTP/1.1" 401 13160
21.43.188.186 - kunze2653 [21/Jun/2019:15:46:02 -0700] "DELETE /bandwidth/turn-key/users HTTP/2.0" 201 2248

#-----------------------------------------------



import pandas as pd
import numpy as np
def proportion_of_education():    
    data = pd.read_csv('assets/NISPUF17.csv')
    data_new = data.loc[:, ['EDUC1']]   # new dataframe has only the required field
    count =  len(data_new['EDUC1'])     # number of records in the file
    unique_values_in_col = data_new['EDUC1'].unique() # unique values in the field
    
    mother_education = {}    
    mother_education_num = {}
    
    for vals in list(unique_values_in_col):
        mother_education_num[vals] = len(data_new[data_new['EDUC1'] == vals]) / len(data_new['EDUC1'])
        
    mother_education["less than high school"] = mother_education_num[1]
    mother_education["high school"] = mother_education_num[2]
    mother_education["more than high school but not college"] = mother_education_num[3]
    mother_education["college"] = mother_education_num[4]
        
    return mother_education

      
proportion_of_education()


#---------------------------------------

EDUC1 coulmn has value from 1, 2,3 ,4

    "less than high school" = 	1
    "high school" = 		2
    "more than high school but not college" = 	3
    "college" = 				4


#---------------------------------------

import pandas as pd
import numpy as np
    
def average_influenza_doses():    
    data = pd.read_csv('assets/NISPUF17.csv')
    data.head()
    data_new = data.loc[:, ['CBF_01', 'P_NUMFLU']]
    #data_new['P_NUMFLU'].unique()
    count_breastfed = len(data_new[data_new['CBF_01'] ==1].dropna())
    count_not_breastfed = len(data_new[data_new['CBF_01'] ==2].dropna())
    doses_breastfed = data_new[data_new['CBF_01'] ==1].dropna()['P_NUMFLU'].sum()
    doses_not_breastfed = data_new[data_new['CBF_01'] ==2].dropna()['P_NUMFLU'].sum()
    return (doses_breastfed/count_breastfed , doses_not_breastfed/count_not_breastfed)
    
    
    
average_influenza_doses()


#---------------------------------------


import pandas as pd
import numpy as np

def chickenpox_by_sex():
    data = pd.read_csv('assets/NISPUF17.csv')
    data.head()
    data_new = data.loc[:, ['HAD_CPOX', 'P_NUMVRC', 'SEX']]
    
    contracted_chick = {}
    
    male_contracted_vaccinated = len ( data_new[data_new['SEX'].eq(1) & data_new['HAD_CPOX'].eq(2) & data_new['P_NUMVRC'].gt(0.0) ].dropna() )
    male_not_contracted_vaccinated = len ( data_new[data_new['SEX'].eq(1) & data_new['HAD_CPOX'].eq(1) & data_new['P_NUMVRC'].gt(0.0) ].dropna() )
    
    female_contracted_vaccinated = len ( data_new[data_new['SEX'].eq(2) & data_new['HAD_CPOX'].eq(2) & data_new['P_NUMVRC'].gt(0.0) ].dropna() )
    female_not_contracted_vaccinated = len ( data_new[data_new['SEX'].eq(2) & data_new['HAD_CPOX'].eq(1) & data_new['P_NUMVRC'].gt(0.0) ].dropna() )
    contracted_chick['male'] = male_contracted_vaccinated / male_not_contracted_vaccinated
    contracted_chick['female'] = female_contracted_vaccinated / female_not_contracted_vaccinated
    
    return contracted_chick

chickenpox_by_sex()


#----------------------------------------

def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    
    data = pd.read_csv('assets/NISPUF17.csv')
    data.head()
    data_new = data.loc[:, ['HAD_CPOX', 'P_NUMVRC']].dropna()
    
    
    # this is just an example dataframe
    #df=pd.DataFrame({"had_chickenpox_column":np.random.randint(1,3,size=(100)),
    #               "num_chickenpox_vaccine_column":np.random.randint(0,6,size=(100))})
    
    #return df.head()

    # here is some stub code to actually run the correlation
    corr, pval=stats.pearsonr(data_new["HAD_CPOX"],data_new["P_NUMVRC"])
    
    # just return the correlation
    return corr

    # YOUR CODE HERE
corr_chickenpox()  


A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the correlation between the use of the vaccine and whether it results in prevention of the infection or disease [1]. In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).

Some notes on interpreting the answer. The `had_chickenpox_column` is either `1` (for yes) or `2` (for no), and the `num_chickenpox_vaccine_column` is the number of doses a child has been given of the varicella vaccine. A positive correlation (e.g., `corr > 0`) means that an increase in `had_chickenpox_column` (which means more no’s) would also increase the values of `num_chickenpox_vaccine_column` (which means more doses of vaccine). If there is a negative correlation (e.g., `corr < 0`), it indicates that having had chickenpox is related to an increase in the number of vaccine doses.

Also, `pval` is the probability that we observe a correlation between `had_chickenpox_column` and `num_chickenpox_vaccine_column` which is greater than or equal to a particular value occurred by chance. A small `pval` means that the observed correlation is highly unlikely to occur by chance. In this case, `pval` should be very small (will end in `e-18` indicating a very small number).

import pandas as pd
import numpy as np[1] This isn’t really the full picture, since we are not looking at when the dose was given. It’s possible that children had chickenpox and then their parents went to get them the vaccine. Does this dataset have the data we would need to investigate the timing of the dose?
