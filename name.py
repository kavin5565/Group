import pandas as pd
import numpy as nm

A = pd.DataFrame(
    {"ROLL NO": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
                 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133],
     "STUDENT NAME": ["Anitha H", "Arjun G", "Babu T", "Baskar K", "Careena B", "Chinnu E", "Dheeran D", "Dhivya S",
                      "Eesha A", "Emily J", "Fasil S", "Geetha R", "Gobi M", "Hari P", "Hassan V", "Ilango B", "Isha N",
                      "Jameer K", "Janvi V", "Kathir K", "Kesav U", "Manoj G", "Mithran S", "Navin P", "Nivas V",
                      "Pavithra G", "Priya T", "Rahul D", "Raj K", "Sneha P", "Suresh S", "Tripathi M"],
     "DATE OF BIRTH": ["12/6/2004", "4/7/2003", "7/8/2004", "19/9/2004", "24/10/2004", "30/11/2004", "12/12/2004",
                       "1/1/2005", "2/2/2005", "7/3/2005", "24/4/2004", "17/7/2005", "15/9/2004", "20/10/2004",
                       "13/12/2004", "16/7/2005", "8/8/2004", "16/3/2005", "17/4/2005", "18/5/2005", "19/6/2005",
                       "20/7/2005", "21/8/2005", "25/9/2005", "3/5/2004", "4/4/2004", "5/5/2004", "17/7/2004",
                       "18/8/2004", "19/9/2004", "20/10/2004", "21/11/2004"],

     "LANGUAGE": [34, 97, 56, 85, 92, 74, 75, 64, 53, 95, 74, 94, 73, 63, 62, 59, 14, 84, 64, 74, 82, 93, 74, 49, 94,
                  39, 65, 47, 75, 53, 72, 59],
     "ENGLISH": [67, 73, 84, 47, 94, 53, 74, 93, 24, 48, 54, 73, 87, 74, 93, 26, 75, 94, 86, 59, 47, 65, 94, 58, 75, 54,
                 85, 83, 85, 64, 95, 84],
     "MATHS": [85, 92, 74, 75, 64, 53, 95, 74, 94, 73, 63, 62, 59, 74, 84, 64, 74, 82, 93, 74, 49, 94, 39, 65, 47, 75,
               53, 72, 59, 64, 95, 84],
     "PHYSICS": [84, 97, 56, 85, 92, 74, 75, 64, 53, 34, 74, 94, 73, 63, 62, 59, 74, 84, 64, 74, 82, 93, 74, 49, 94, 39,
                 65, 47, 75, 53, 72, 59],
     "CHEMISTRY": [68, 73, 84, 47, 94, 53, 74, 93, 24, 48, 54, 73, 87, 74, 93, 26, 75, 94, 86, 59, 47, 65, 94, 58, 75,
                   54, 85, 83, 85, 64, 95, 84],
     "BIOLOGY": [87, 74, 93, 26, 75, 94, 86, 59, 47, 65, 94, 58, 75, 54, 85, 83, 85, 64, 95, 84, 84, 97, 56, 85, 92, 74,
                 75, 64, 53, 95, 65, 86],

     },
    columns=(
    "ROLL NO", "STUDENT NAME", "DATE OF BIRTH", "LANGUAGE", "ENGLISH", "MATHS", "PHYSICS", "CHEMISTRY", "BIOLOGY"),
)
A["TOTAL"] = A["LANGUAGE"] + A["ENGLISH"] + A["MATHS"] + A["PHYSICS"] + A["CHEMISTRY"] + A["BIOLOGY"]
A["AVERAGE"] = A["TOTAL"].mean()


detail_cols = ['ROLL NO', 'STUDENT NAME', 'DATE OF BIRTH']
marks_cols = [ 'LANGUAGE', 'ENGLISH','MATHS', 'PHYSICS', 'CHEMISTRY', 'BIOLOGY',"TOTAL","AVERAGE"]


detail_ind = pd.MultiIndex.from_product([["DETAILS"], detail_cols])
marks_ind  = pd.MultiIndex.from_product([['SUBJECT'],marks_cols])

ind = detail_ind.append(marks_ind)


A.columns = ind

print(A)
