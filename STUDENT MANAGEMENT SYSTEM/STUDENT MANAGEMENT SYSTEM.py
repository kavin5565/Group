import pandas as pd

B_df =         pd.DataFrame({'Names': ['Rohan', 'Bhuvan', 'Surya', 'Rahul', 'Roshan', 'Daniel', 'Tashiq', 'Ranbir',
                                       'Rishab', 'Akshay', 'Wasim', 'Vishal', 'Chethan', 'Dhruv', 'Eeshan', 'Priyanka',
                                       'Deepika', 'Alia', 'Rishika', 'Aarohi', 'Shraddha', 'Vrindha', 'Vidhya',
                                       'Urvashi', 'Preethi', 'Shahnaz', 'Divya', 'Trisha', 'Anushka', 'Riya'],
                             'Roll.no': [501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516,
                                         517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530],
                             'Location': ['Bangalore', 'Mumbai', 'Bhopal', 'Delhi', 'Chennai', 'Pune', 'Rajkot',
                                          'Ahemdabad', 'Jaipur', 'Raipur', 'Gangtok', 'Patna', 'Dehradhun', 'Hyderabad',
                                          'Mysore', 'Lucknow', 'Bhubaneshwar', 'Kolkata', 'Aurangabad', 'Amravathi',
                                          'Belgaum', 'Mathura', 'Erode', 'Madurai', 'Shimla', 'Panaji', 'Aizwal',
                                          'Imphal', 'Dispur', 'Agartala'],
                             'Age': [18, 18, 18, 18, 19, 18, 19, 18, 18, 19, 19, 20, 18, 18, 18, 19, 18, 18, 19, 19, 18,
                                     18, 19, 18, 19, 20, 18, 18, 18, 19],
                             'Gender': ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'F',
                                        'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'],
                             'English': [75, 72, 65, 70, 62, 66, 64, 45, 56, 66, 39, 56, 67, 79, 74, 72, 63, 61, 58, 55,
                                         65, 66, 70, 73, 72, 65, 64, 65, 67, 63],
                             'Hindi': [65, 66, 52, 57, 74, 72, 71, 70, 63, 65, 69, 60, 63, 64, 68, 59, 55, 64, 65, 66,
                                       66, 68, 73, 74, 71, 63, 71, 72, 64, 65],
                             'Physics': [72, 73, 76, 82, 66, 64, 72, 66, 53, 79, 84, 92, 94, 91, 90, 64, 76, 63, 91, 59,
                                         84, 83, 81, 80, 75, 79, 59, 72, 74, 83],
                             'Chemistry': [73, 74, 69, 68, 83, 79, 74, 83, 90, 93, 94, 89, 78, 84, 76, 76, 68, 72, 93,
                                           86, 74, 92, 54, 65, 74, 77, 74, 82, 88, 79],
                             'Mathematics': [81, 75, 82, 73, 78, 95, 99, 84, 88, 95, 92, 80, 65, 88, 75, 74, 94, 88, 87,
                                             83, 75, 77, 74, 65, 72, 74, 88, 74, 84, 90],
                             'Computer Science': [84, 83, 75, 74, 28, 74, 65, 54, 65, 88, 98, 87, 85, 93, 97, 86, 65,
                                                  64, 93, 74, 88, 75, 73, 83, 74, 65, 74, 75, 79, 80],
                             'Environmental Science': [35, 27, 33, 45, 44, 41, 49, 46, 45, 39, 38, 34, 27, 48, 45, 44,
                                                       42, 36, 38, 35, 46, 44, 49, 50, 43, 42, 39, 42, 48, 35],

                             })

print(B_df)


B_df.index=range(1,31)
print(B_df)
B_dfMarks=['English','Hindi','Physics','Chemistry','Mathematics','Computer Science','Environmental Science']
B_df['Marks']=B_df[B_dfMarks].sum(axis=1)
print(B_df)
B_df['Max Marks']=[650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650,650]
print(B_df)
import numpy as np
B_df['Percentage']=(B_df['Marks']/B_df['Max Marks'])*100
print(B_df)
B_df['Grade']=B_df['Percentage'].apply(lambda x:'First Class' if x<75 else 'Distinction')
print(B_df)
B_df['Result']=B_df['Percentage'].apply(lambda x:'Pass' if x>35 else 'Fail')
print(B_df)
B_df=B_df.sort_values('Names',ascending=True)
print(B_df)
B_df.reset_index(drop=True, inplace=True)
print(B_df)
B_df.index=range(1,31)
print(B_df)
print(B_df['Grade'].value_counts())
print(B_df['Result'].value_counts())
print(B_df['Percentage'].value_counts())
print(B_df.columns)
print(B_df.groupby('Gender')['Percentage'].agg(['mean','count']))
print(B_df.groupby('Grade')['Percentage'].agg(['mean','count']))
print(pd.crosstab(index=B_df['Gender'],columns=B_df['Grade']))
