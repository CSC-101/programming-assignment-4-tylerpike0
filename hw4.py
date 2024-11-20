import sys
from errno import ECHILD

import county_demographics
import build_data
import hw3
from build_data import CountyDemographics
from data import CountyDemographics



def operate_line(line_index: int, line: str, current_data_set: list[CountyDemographics]) -> list[CountyDemographics]:
    print("Line:", line_index + 1)
    operation_and_args = line.split(":")

    operation = operation_and_args[0]
    if operation == '':
        return current_data_set
    fields = None

    category = None
    key = None
    value = None
    if len(operation_and_args) > 1:
        fields = operation_and_args[1].split(".")
        category = fields[0]
        key = fields[1]

    if len(operation_and_args) > 2:
        try:
            value = float(operation_and_args[2])
        except ValueError:
            print("Argument 2 could not be converted to a float")
            return current_data_set

    if len(operation_and_args) > 3:
        print("Too many arguments were passed in. At most there should be 2")
        return current_data_set


    if operation == "display":
        display(current_data_set)
        return current_data_set

    if operation == "display":
        if category:
            return filter_state(current_data_set, line.strip("filter-state:"))
        else:
            print("Not enough arguments were provided on line {}. 1 was expected".format(line_index + 1))
            return current_data_set

    if operation == "filter-gt":
        if category and key and value:
            return filter_gt(current_data_set, category, key, value)
        else:
            print("Not enough arguments were provided on line {}. 2 were expected".format(line_index + 1))
            return current_data_set

    if operation == "filter-lt":
        if category and key and value:
            return filter_lt(current_data_set, category, key, value)
        else:
            print("Not enough arguments were provided on line {}. 2 were expected".format(line_index + 1))
            return current_data_set

    if operation == "population-total":
        population_total(current_data_set)
        return current_data_set

    if operation == "population":
        if category and key:
            population_subtotal(current_data_set, category, key)
            return current_data_set
        else:
            print("Not enough arguments were provided on line {}. 1 was expected".format(line_index + 1))
            return current_data_set

    if operation == "percent":
        if category and key:
            population_subtotal_percentage(current_data_set, category, key)
            return current_data_set
        else:
            print("Not enough arguments were provided on line {}. 1 was expected".format(line_index + 1))
            return current_data_set

    print("Operation keyword '{}' matched no defined operation".format(operation))
    return current_data_set



def display(data_set: list[CountyDemographics]) -> None:
    for county in data_set:
        print("{}, {}".format(county.county,county.state))
        print("\tPopulation: {}".format(county.population["2014 Population"]))
        print("\tAge:")
        for key in county.age.keys():
            print("\t\t{}: {}%".format(key, county.age[key]))

        print("\tEducation:")
        for key in county.education.keys():
            print("\t\t{}: {}%".format(key, county.education[key]))

        print("\tEthnicity Percentages:")
        for key in county.ethnicities.keys():
            print("\t\t{}: {}%".format(key, county.ethnicities[key]))

        print("\tIncome:")
        for key in county.income.keys():
            print("\t\t{}: {}%".format(key, county.income[key]))

        print()

def filter_state(data_set: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    filtered_demographics = []
    for county in data_set:
        if county.state == state:
            filtered_demographics.append(county)
    print("Filter: state == {} ({} entries)".format(state, len(filtered_demographics)))
    return filtered_demographics

def filter_gt(data_set: list[CountyDemographics], category: str, key: str, number:float) -> list[CountyDemographics]:

    filtered_demographics = []
    for county in data_set:
        if category == "Age":
            if county.age[key] > number:
                filtered_demographics.append(county)
        elif category == "Education":
            if county.education[key] > number:
                filtered_demographics.append(county)
        elif category == "Ethnicities":
            if county.ethnicities[key] > number:
                filtered_demographics.append(county)
        elif category == "Income":
            if county.income[key] > number:
                filtered_demographics.append(county)

    print("Filter: {} gt {} ({} entries)".format(key, number, len(filtered_demographics)))
    return filtered_demographics

def filter_lt(data_set: list[CountyDemographics], category: str, key:str, number: float) -> list[CountyDemographics]:
    filtered_demographics = []

    for county in data_set:
        if category == "Age":
            if key in county.age:
                if county.age[key] < number:
                    filtered_demographics.append(county)
            else:
                print("Invalid key '{}'".format(key))
                return data_set
        elif category == "Education":
            if key in county.education:
                if county.education[key] < number:
                    filtered_demographics.append(county)
            else:
                print("Invalid key '{}'".format(key))
                return data_set
        elif category == "Ethnicities":
            if key in county.ethnicities:
                if county.ethnicities[key] < number:
                    filtered_demographics.append(county)
            else:
                print("Invalid key '{}'".format(key))
                return data_set
        elif category == "Income":
            if key in county.income:
                if county.income[key] < number:
                    filtered_demographics.append(county)
            else:
                print("Invalid key '{}'".format(key))
                return data_set

    print("Filter: {} lt {} ({} entries)".format(category, number, len(filtered_demographics)))
    return filtered_demographics

def population_total(data_set: list[CountyDemographics]) -> None:
    print("2014 Population: {}".format(hw3.population_total(data_set)))

def population_subtotal(data_set: list[CountyDemographics], category: str, key: str) -> None:
    if category == "Education":
        print("2014 Education.{} population: {}".format(key,hw3.population_by_education(data_set, key)))
    elif category == "Ethnicities":
        print("2014 Ethnicities.{} population: {}".format(key,hw3.population_by_ethnicity(data_set, key)))
    elif category == "Income":
        print("2014 Income.{} population: {}".format(key,hw3.population_by_income(data_set, key)))

def population_subtotal_percentage(data_set: list[CountyDemographics], category: str, key: str) -> None:
    if category == "Education":
        print("2014 {} percentage: {}%".format(key, round(hw3.percent_by_education(data_set, key),2)))
    elif category == "Ethnicities":
        print("2014 {} percentage: {}%".format(key, round(hw3.percent_by_ethnicity(data_set, key),2)))
    elif category == "Income":
        print("2014 {} percentage: {}%".format(key, round(hw3.percent_by_income(data_set, key),2)))


demographics = build_data.get_data()
print("{} records loaded".format(len(demographics)))

args = sys.argv
if len(args) == 1:
    print("There where 0 arguments when 1 was expected")
    sys.exit()
file_name = args[1]

try:
    with open(file_name,"r") as ops_file:
        lines = ops_file.readlines()
        for line_index in range(len(lines)):
            current_line = lines[line_index].strip("\n")
            demographics = operate_line(line_index, current_line, demographics)


        

except FileNotFoundError:
    print("File of name {} could not be found".format(file_name))
    sys.exit()




