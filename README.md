# yelp-data-analytics

## Part 1
Simple data analysis using pandas
* restaurantCategoryDist: a frequency distribution of the number of restaurants  in each categoryof  restaurants(e.g.,  Chinese,  Japanese,  Korean,  Greek,  etc.)in  a  descending  order  of popularity (from the most popular category to the least popular). The output should be one line per pair of values as follows: 
  - category:#restaurants
  - for example: Korean:120, Italian:110... 

* restaurantReviewDist: a frequency distribution  of the  number  of reviews submitted  for each category of restaurants (e.g., Chinese, Japanese, Korean, Greek, etc.) in a descending order (from  the  most  reviewed  category  to  the  least  reviewed),  along  with  the  average  number  of stars received per category. The output should be one line per triplet as follows:        

  - category:#reviews:avg_stars 
  - for example: Korean:580:4.5, Italian:110:3.8...

* creates a  bar  chart  that  shows  the top-10of restaurantCategoryDistfound earlier, where the x-axis represents the restaurant  category andthe y-axisrepresentsits  frequency (#restaurants).
  
  
* to run script "python3 dist-stats.py yelp_business.csv Toronto"
  can also use analysis on different city
  
  
## Part 2
Employs Hadoop Map reduce for Distributed Text Analytics
* computing n-grams
  - compute the  number  of  occurrences  of  each unigramin the tips collection (umapper.py, ureducer.py)and output the results in a file called unigrams.txt
  - compute the  number  of  occurrences  of  each bigramin the tipscollection(bmapper.py, breducer.py)and output the results in a file called bigrams.txt
  - compute the  number  of  occurrences  of  each trigraminthe tipscollection  (tmapper.py, treducer.py)and output the results in a file called trigrams.txt
  
  - running script : ./mapper.py < input.txt | sort | ./reducer.py

* Distributed Construction of an Inverted Index
  -  build  an inverted index  that  mapscategories (of businesses)to businesses. In other words, given a collection of businesses(as provided by Yelp), an inverted index  is a dictionary where each category is associated with a list of the business ids that belong to that category
  - compute the inverted index ofthe categoriesto businesses(iimaper.py, iireducer.py) and output the results in a file called inverted-index.txt
  - running script : ./iimaper.py < input.txt | sort | ./iireducer.py > inverted-index.txt
