import json

"""
takes an applicant in the form of a dictionary and calculates and returns
the overall weighted score
"""
def calculate_score(applicant):

    # indexing into application dictionary to get attribute dictionary assigning to variable
    attributes = applicant["attributes"]

    # indexing into attribute dictionary variable and calculating the weighted values of the attributes and assigning them to variables
    # weights determined by team data and the coder's personal opinion
    weighted_intelligence = attributes["intelligence"] * 4
    weighted_strength = attributes["strength"] * 3
    weighted_endurance = attributes["endurance"] * 4
    weighted_spicy = attributes["spicyFoodTolerance"] * 1

    # return overall weighted score of the applicant
    return round((weighted_intelligence + weighted_strength + weighted_endurance + weighted_spicy) / 120, 1)

"""
takes a list of applicants (dictionaries) and returns a list of applicants and their calculated overall score
"""
def take_applicants(applicants):

    # create a new list to return
    scoredApplicants = []

    # for every applicant in the applicant list, creates a new dictionary, adds name, and adds applicant's calculated overall score
    for applicant in applicants:

        # create new result dictionary for every applicant
        applicant_result = {}

        # indexing name from exisiting dictionary and calling calculate_score function
        name = applicant["name"]
        score = calculate_score(applicant)

        # add keys and values to dictionary
        applicant_result["name"] = name
        applicant_result["score"] = score

        # add result dictionary to return list
        scoredApplicants.append(applicant_result)

    return scoredApplicants


# open json file
cool_file = open('datahouse_data.json')

input_data = json.load(cool_file)

# calls our function and gets the results
scores_result = take_applicants(input_data["applicants"])

# create dictionary for json to write
json_dict = {}
json_dict["scoreApplicants"] = scores_result

# write into outfile
json_object = json.dumps(json_dict, indent=4)

with open("datahouse_output.json", "w") as outfile:
    outfile.write(json_object)