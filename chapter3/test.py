import clusters
blognames,words,data=clusters.readfile('blogdata1.txt')
clust=clusters.hcluster(data)

print clust

clusters.printclust(clust,labels=blognames)

clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')

