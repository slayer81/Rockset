#!/usr/bin/env python
# coding: utf-8
from rockset import Client, ParamDict
import os, sys
from datetime import datetime

# #### Description:
# Follow Rockset's Quickstart guide to import the sample movies dataset into a
# trial Rockset account and build <snip!> the following:
# **(I chose command-line python)**
#
# An app that takes a calendar year as the only input and prints the following:
# 1. Top 10 most popular movies in that year (based on "popularity" field).
#     1. **Rank | Title | Popularity**
#
# 2. Top 10 highest grossing movies in that year along with % of revenue that
# movie grossed over the total revenue grossed over all movies made in that
# calendar year (based on "revenue" field).
# (ie: if that year the top movie grossed 5M USD and the total revenue grossed
# by all movies is 50M USD, then number 10 should be printed in "\% of Revenue".
#     2. **Rank | Title | Revenue | \% of Revenue**
#
# 3. Top 10 Genres in that year (based on "genre" field).
#     3. **Rank | Genre | Movie Count**
#
# 4. Based on the most popular Genre of that year, find the top 10 Production Companies
# (based on "production_companies" field) that made the most number of movies in that Genre.
#     4. **Rank | Production Company | Popular Genre | Movie Count**


# Replace the following with your Query Lambda version IDs
quickstart_versionID = '1f9ffc091014b427'
task1_versionID = 'dc244ad0560879ce'
task2_versionID = 'd8e92bbb82fcf4a6'
task3_versionID = '45c50ea7af3200fa'
task4_versionID = '3edd11b40e4277aa'



start_time = datetime.now()

if len(sys.argv) == 1:
	print('ERROR: You have specified too few arguments. ARGS: {}'.format(len(sys.argv)))
	sys.exit()

if len(sys.argv) > 2:
	print('ERROR: You have specified too many arguments. ARGS: {}'.format(len(sys.argv)))
	sys.exit()

rs = Client(api_key=os.getenv('ROCKSET_APIKEY', None), api_server='https://api.euc1a1.rockset.com')
year = sys.argv[1]



def quickstart_example():
    # Keeping the Quickstart example in here, well, just for fun ;)
    # retrieve Query Lambda
    qlambda = rs.QueryLambda.retrieve(
        'getRecommendedMovies',
        version = quickstart_versionID,
        workspace = 'commons')

    params = ParamDict()
    params['genre'] = "Action"
    params['userId'] = "100"
    myResults = qlambda.execute(parameters=params)

    return myResults.results


# UDF for Task 1
def years_top10_most_popular(year):
    qlambda = rs.QueryLambda.retrieve(
        'PopularityTop10_byYear',
        version = task1_versionID,
        workspace = 'commons')
    params = ParamDict()
    params['myYear'] = year
    myResults = qlambda.execute(parameters=params)

    return myResults.results


# UDF for Task 2
def getTop10HighestGross_withRevPercentage(year):
    qlambda = rs.QueryLambda.retrieve(
        'getTop10HighestGross_withRevPercentage',
        version = task2_versionID,
        workspace = 'commons')
    params = ParamDict()
    params['myYear'] = year
    myResults = qlambda.execute(parameters=params)

    return myResults.results


# UDF for Task 3
def years_top10_genres(year):
    # retrieve Query Lambda
    qlambda = rs.QueryLambda.retrieve(
        'Top10Genres_byYear',
        version = task3_versionID,
        workspace = 'commons')
    params = ParamDict()
    params['myYear'] = year
    myResults = qlambda.execute(parameters=params)

    return myResults.results


# UDF for Task 4
def Top10ProductionCompanies_byReleaseCount_TopGenre(year):
    qlambda = rs.QueryLambda.retrieve(
        'Top10ProductionCompanies_byReleaseCount_TopGenre',
        version = task4_versionID,
        workspace = 'commons')
    params = ParamDict()
    params['myYear'] = year
    myResults = qlambda.execute(parameters=params)

    return myResults.results



# myQuickstart = quickstart_example()
# print(myQuickstart)
# End of QuickStart example portion


# Task #1
# Top 10 most popular movies in that year (based on "popularity" field)
task1Results = years_top10_most_popular(year)
print("\n\n")
print("Top 10 most popular movies for the year: \'{}\'".format(year))
print('Rank | Title | Popularity')
for i in task1Results:
    print(i)
print("\n\n")



# Task #2
# Top 10 highest grossing movies in that year along with % of revenue that movie grossed
# over the total revenue grossed over all movies made in that calendar year (based on "revenue" field)
task2Results = getTop10HighestGross_withRevPercentage(year)
print("Top 10 highest grossing movies with RevPercentage for the year: \'{}\'".format(year))
print('Rank | Title | Revenue | % of Revenue')
for i in task2Results:
    print(i)
print("\n\n")



# Task #3
# Top 10 Genres in that year (based on "genre" field)
task3Results = years_top10_genres(year)
print("Top Genres, by release count, for \"{}\"".format(year))
print('Rank | Genre | Movie Count')
for i in task3Results:
    print(i)
print("\n\n")



# Task #4
# Based on the most popular Genre of that year, find the top 10 Production Companies
# (based on "production_companies" field) that made the most number of movies in that Genre
task4Results = Top10ProductionCompanies_byReleaseCount_TopGenre(year)
print("Top Production Companies, by release count in top genre, for \"{}\"".format(year))
print('Rank | Production Company | Popular Genre | Movie Count')
for i in task4Results:
    print(i)
print("\n")
print("And that's all, folks!")
print("\nTotal execution time: {}".format(datetime.now() - start_time))
print("\n\n")
