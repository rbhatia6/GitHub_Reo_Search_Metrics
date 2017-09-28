# GitHub_Repo_Search_Metrics

#### rbhatia$ python github_repo_search_metrics.py

1. Top 5 most frequently issued queries = 
 [('/search?q=crop', 21), ('/search?q=entosphere', 19), ('/search?q=kerchunk', 16), ('/search?q=hemosalpinx', 16), ('/search?q=operette', 16)]

2. Top 5 queries in terms of the total number of results clicked = 
 [('/search?q=crop', 58), ('/search?q=hemosalpinx', 47), ('/search?q=kerchunk', 46), ('/search?q=entosphere', 45), ('/search?q=contrabandage', 44)]

3. Average length of a search session = 60845.36


#### Imagine that you need to answer question number 1 from above, but over a dataset containing hundreds of billions of rows, split across many files. What techniques would you use to accomplish this?

##### With hundreds of billions of rows split across many files, a viable solution is to use MapReduce.  Let's take the example of calculating the top 5 most frequently issued queries:

1. Several instances of the mapper function are created on the different machines in our cluster.

2. Each instance receives a different input file 

3. The mapper tokenizes the document and emits an intermediate k-v pair. The k-v pair will be (search-term, 1) pair.

4. Combiner class are run on every node that has run map tasks.

5. The Combiner will receive as input all data emitted by the Mapper instances on a given node. The Combiner is a "mini-reduce" process which operates only on data generated by one machine. It will aggregate the values for a search-term which are then forwarded to the reducers.

6. For each key in the partition assigned to a Reducer, the Reducer's reduce() method is called once. This receives a key as well as an iterator over all the values associated with the key. It will aggregate the values which will be output to the output fules.
