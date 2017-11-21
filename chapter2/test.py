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

#import pydelicious
#
#pydelicious.get_popular(tag='usa')


recommendations.getRecommendations(recommendations.critics,'Toby')

recommendations.getRecommendations(recommendations.critics,'Toby',similarity=recommendations.sim_distance)

movies=recommendations.transformPrefs(recommendations.critics)

recommendations.topMatches(movies,'Superman Returns')

recommendations.getRecommendations(movies,'Just My Luck')


recommendations.topMatches(movies,'Just My Luck')

recommendations.getRecommendations(movies,'Lady in the Water')
