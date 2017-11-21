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


