import clusters

blognames,words,data=clusters.readfile('blogdata.txt')
#print len(data)
#print data[41]

#clust=clusters.hcluster(data)

#print clust

#clusters.printclust(clust,labels=blognames)

#clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')


#转置，对词语进行聚类
rdata=clusters.rotatematrix(data)
wordclust=clusters.hcluster(rdata)
clusters.drawdendrogram(wordclust,labels=words,jpeg='blogclust3.jpg')

