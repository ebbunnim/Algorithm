import re

def solution(new_id):
    answer = ''
    new_id=new_id.lower()
    new_id=re.sub('[^a-z0-9\-_.]','',new_id)
    new_id=re.sub('[.]+','.',new_id)
    new_id=re.sub('^[.]','',new_id)
    new_id=re.sub('[.]$','',new_id)
    if new_id=='':
        new_id='a'
    if len(new_id)>=16:
        new_id=new_id[:15]
        new_id=re.sub('[.]$','',new_id)
    elif len(new_id)<=2:
        while True:
            if len(new_id)==3:
                break
            new_id+=new_id[-1]
    return new_id