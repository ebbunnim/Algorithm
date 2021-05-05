from collections import defaultdict

table=["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages=["JAVA", "JAVASCRIPT"]
preference=[7, 5, 5]

# initial requirements
score_dict=defaultdict(dict)
ans_dict=defaultdict(int)

# split input, and matching with language, and write within preference
def preprocessing()->dict:
    for ele in table:
        job,l5,l4,l3,l2,l1=ele.split()
        score=5
        for language in (l5,l4,l3,l2,l1):
            score_dict[job][language]=score
            score-=1
    return score_dict

# match given language with preprocessed list, multiply and get sum of preference and score
def match(score_dict:dict,languages:list,preference:list)->None:
    for job in score_dict.keys():
        for i in range(len(languages)):
            ans_dict[job]+=score_dict[job].get(languages[i],0)*preference[i]

match(preprocessing(),languages,preference)
anslist=list(ans_dict.items())
anslist.sort(key=lambda x : (-x[1],x[0]))
print(anslist[0][0])



