from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

find = db.movies.find_one({'title':'매트릭스'})
print(find['star'])
st = find['star']
same_star = list(db.movies.find({'star':st}))
for sm in same_star:   # list 형태니까 for 구문으로 반복해서 나열해줘야함
    print(sm['star'] + sm['title'])

db.movies.update_many({'star':st},{'$set':{'star':0}})