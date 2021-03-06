#import pydelicious
#pydelicious.get_popular(tag='programming')

#from deliciousrec import *
#delusers=initializeUserDict('programming')
#delusers['tsegaran']={}
#fillIteams(delusers)


import recommendations
#print recommendations.critics['Lisa Rose']['Lady in the Water']

print recommendations.critics['Lisa Rose']
print recommendations.critics['Gene Seymour']
print recommendations.sim_distance(recommendations.critics,'Lisa Rose','Gene Seymour')
print recommendations.sim_pearson(recommendations.critics,'Lisa Rose','Gene Seymour')

print recommendations.topMatches(recommendations.critics,'Toby',n=3)

print recommendations.topMatches(recommendations.critics,'Toby',n=3,similarity=recommendations.sim_distance)

recommendations.getRecommendations(recommendations.critics,'Toby')

recommendations.getRecommendations(recommendations.critics,'Toby',similarity=recommendations.sim_distance)

movies=recommendations.transformPrefs(recommendations.critics)

#print movies

recommendations.topMatches(movies,'Superman Returns')

recommendations.getRecommendations(movies,'Just My Luck')

recommendations.getRecommendations(movies,'Lady in the Water')

itemsim=recommendations.calculateSimilarItems(recommendations.critics,n=8)
itemsim

recommendations.getRecommendedItems(recommendations.critics,itemsim,'Toby')

prefs=recommendations.loadMovieLens()
prefs['87']


recommendations.getRecommendations(prefs,'87')[0:30]

itemsim1=recommendations.calculateSimilarItems(prefs,n=50)
recommendations.getRecommendedItems(prefs,itemsim1,'87')[0:30]
