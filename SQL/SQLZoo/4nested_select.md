1. List each country name where the population is larger than that of 'Russia'.
```
SELECT name 
from world 
where population > 
      (Select population
       from world where name='Russia');
```

2. Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.
```
SELECT name
from world
where continent = 'Europe' and gdp/population >
 (Select gdp/population 
  from world
  where name='United Kingdom');
  ```
  
3. Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.
```
select name, continent
from world
where continent IN (select continent from world 
where name in ('Argentina', 'Australia'));
```

4. Which country has a population that is more than United Kingom but less than Germany? Show the name and the population.
```
select name, population 
from world
where population > (select population from world where name='United Kingdom')
  and population < (select population from world where name='Germany')
```

5. Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.
```
select name, 
str((population*100)/(select population from world where name='Germany'))+'%'
from world
where continent='Europe';
```

6. Which countries have a GDP greater than every country in Europe? [Give the name only.] (Some countries may have NULL gdp values)
```
SELECT name
from world 
where gdp > ALL(select max(GDP) from world where continent='Europe');
```

7. Find the largest country (by area) in each continent, show the continent, the name and the area:
```

```
