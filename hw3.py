from collections.abc import Iterable
from itertools import count

from county_demographics import *
from data import CountyDemographics

# Part 1

# returns the total population of a list of demographics
def population_total(county_demographics: list[CountyDemographics]) -> float:
    if  county_demographics is None:
        return 0
    total = 0
    for county_demographic in county_demographics:
        total += county_demographic.population["2014 Population"]
    return total


# Part 2

# returns a new list that has all the demographics in a given list that are from a given state
def filter_by_state(demographics: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    if demographics is None:
        return []
    demographics_in_state = []
    for demographic in demographics:
        if demographic.state == state:
            demographics_in_state.append(demographic)
    return  demographics_in_state


# Part 3

# returns the total population in a given list of demographics, which has at least a given education
def population_by_education(demographics: list[CountyDemographics],education_key: str ) -> float:
    if demographics is None:
        return 0
    total = 0
    for demographic in demographics:
        if education_key in demographic.education.keys():
            percentage = demographic.education[education_key]
            total += percentage * demographic.population["2014 Population"] * 0.01
    return total

# returns the total population fo a given ethnicity in a given list of demographics
def population_by_ethnicity(demographics: list[CountyDemographics],ethnicity_key: str ) -> float:
    if demographics is None:
        return 0
    total = 0
    for demographic in demographics:
        if ethnicity_key in demographic.ethnicities.keys():
            percentage = demographic.ethnicities[ethnicity_key]
            total += percentage * demographic.population["2014 Population"] * 0.01
    return total

# returns the total population fo a given ethnicity in a given list of demographics
def population_by_income(demographics: list[CountyDemographics],income_key: str ) -> float:
    if demographics is None:
        return 0
    total = 0
    for demographic in demographics:
        if income_key in demographic.income.keys():
            percentage = demographic.income[income_key]
            total += percentage * demographic.population["2014 Population"] * 0.01
    return total

# returns the total population below the poverty level in a given list of demographics
def population_below_poverty_level(demographics: list[CountyDemographics]) -> float:
    if demographics is None:
        return 0
    total = 0
    for demographic in demographics:
        percentage = demographic.income["Persons Below Poverty Level"]
        total += percentage * demographic.population["2014 Population"] * 0.01
    return total

# Part 4

# returns the percent of a population of given demographics which has at least a given education level
def percent_by_education(demographics: list[CountyDemographics], education_key: str) -> float:
    if len(demographics) == 0:
        return 0
    return population_by_education(demographics, education_key) / population_total(demographics) * 100

# returns the percent of a population of given demographics which are of a given ethnicity
def percent_by_ethnicity(demographics: list[CountyDemographics], ethnicity_key: str) -> float:
    if len(demographics) == 0:
        return 0
    return population_by_ethnicity(demographics, ethnicity_key) / population_total(demographics) * 100

# returns the percent of a population of given demographics which are of a given ethnicity
def percent_by_income(demographics: list[CountyDemographics], income_key: str) -> float:
    if len(demographics) == 0:
        return 0
    return population_by_income(demographics, income_key) / population_total(demographics) * 100


# returns the percent a population of given demographics which is below the poverty level
def percent_below_poverty_level(demographics: list[CountyDemographics]) -> float:
    if len(demographics) == 0:
        return 0
    total_population = population_total(demographics)
    if total_population == 0:
        return 0
    return  population_below_poverty_level(demographics) / total_population * 100

# Part 5

# returns a list of demographics in a list from a given list which have an education level greater than a given threshold
def education_greater_than(demographics: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    if demographics is None:
        return []
    greater_demographics = []
    for demographic in demographics:
        if threshold < demographic.education[education_key]:
            greater_demographics.append(demographic)
    return greater_demographics

# returns a list of demographics in a list from a given list which have an education level less than a given threshold
def education_less_than(demographics: list[CountyDemographics], education_key: str, threshold: float) -> list[CountyDemographics]:
    if demographics is None:
        return []
    smaller_demographics = []
    for demographic in demographics:
        if threshold > demographic.education[education_key]:
            smaller_demographics.append(demographic)
    return smaller_demographics


# returns a list of demographics in a list from a given list which have a given ethnicity percentage greater than a given threshold
def ethnicity_greater_than(demographics: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    if demographics is None:
        return []
    greater_demographics = []
    for demographic in demographics:
        if threshold < demographic.ethnicities[ethnicity_key]:
            greater_demographics.append(demographic)
    return greater_demographics

# returns a list of demographics in a list from a given list which have a given ethnicity percentage less than a given threshold
def ethnicity_less_than(demographics: list[CountyDemographics], ethnicity_key: str, threshold: float) -> list[CountyDemographics]:
    if demographics is None:
        return []
    smaller_demographics = []
    for demographic in demographics:
        if threshold > demographic.ethnicities[ethnicity_key]:
            smaller_demographics.append(demographic)
    return smaller_demographics

# returns a list of demographics in a list from a given list which have a poverty level above a given threshold
def below_poverty_level_greater_than(demographics: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    if demographics is None:
        return []
    greater_demographics = []
    for demographic in demographics:
        if threshold < demographic.income["Persons Below Poverty Level"]:
            greater_demographics.append(demographic)
    return greater_demographics

# returns a list of demographics in a list from a given list which have a poverty level below a given threshold
def below_poverty_level_less_than(demographics: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    if demographics is None:
        return []
    smaller_demographics = []
    for demographic in demographics:
        if threshold > demographic.income["Persons Below Poverty Level"]:
            smaller_demographics.append(demographic)
    return smaller_demographics