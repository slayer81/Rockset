# Rockset

### Description:
Follow Rockset's Quickstart guide to import the sample movies dataset into a
trial Rockset account and build <snip!> the following:
**(I chose command-line python)**

An app that takes a calendar year as the only input and prints the following:
1. Top 10 most popular movies in that year (based on "popularity" field).

    `**Rank | Title | Popularity**`


2. Top 10 highest grossing movies in that year along with % of revenue that
movie grossed over the total revenue grossed over all movies made in that
calendar year (based on "revenue" field).
(ie: if that year the top movie grossed 5M USD and the total revenue grossed
by all movies is 50M USD, then number 10 should be printed in "\% of Revenue".

`**Rank | Title | Revenue | % of Revenue**`


3. Top 10 Genres in that year (based on "genre" field).

`**Rank | Genre | Movie Count**`


4. Based on the most popular Genre of that year, find the top 10 Production Companies
(based on "production_companies" field) that made the most number of movies in that Genre.

`**Rank | Production Company | Popular Genre | Movie Count**`
