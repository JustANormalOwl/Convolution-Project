"""All works created here are open for the public to use and modify. Feel free to make changes and/or modifications
to this program. This program was made by owlthechill#3266 for the Deep Divers Industrial Diving Company, but you can
use it for other things too

--- Function ---
This program is intended to provide a more in depth feel to characters.
You can set each item to a random value (unless explicitly told you can't).

"""

import random

import names

import convolutionLibrary

# --- Introductions --- #
print("Welcome to Deep Divers Industrial Diving Company. Before we put you into the field, we have a couple of "
      "questions we need to ask you.")
print("Let's get started")
# --- Name --- #
name = input("[male] or [female] or [custom]")

if name == "male":
    firstName = names.get_first_name(gender='male')
    lastName = names.get_last_name()
    gender = "male"
if name == "female":
    firstName = names.get_first_name(gender='female')
    lastName = names.get_last_name()
    gender = "female"
if name == "custom":
    firstName = input("First Name")
    lastName = input("Last Name: ")
    nickName = input("Do you have any nickname?")
    gender = input("What's your gender?")
# Checks for custom input, if not sets the nickname to nothing
if name == "male" or name == "female":
    nickName = "None"

# --- Birthday --- #
birthDate = convolutionLibrary.getBirthDate()
# --- Birthplace --- #
birthPlaceQuestion = input("Where were you born? ([e]arth, [s]tation,[j]upiter,[m]oon,[eu]ropa,or [custom])")

if birthPlaceQuestion == "e":
    birthPlace = convolutionLibrary.getBirthPlace(bPlace="earth")

elif birthPlaceQuestion == "s":
    birthPlace = convolutionLibrary.getBirthPlace(bPlace="station")

elif birthPlaceQuestion == "j":
    birthPlace = convolutionLibrary.getBirthPlace(bPlace="jupiter")

elif birthPlaceQuestion == "m":
    birthPlace = "Earth's Moon"

elif birthPlaceQuestion == "eu":
    birthPlace = "Europa"

elif birthPlaceQuestion == "custom":
    birthPlace = input("Where are you from?")

# --- Religion --- #
religionQuestion = input("Do you have any religious beliefs? ([y]es, [n]o or [custom])")
if religionQuestion == "y":
    religion = random.choice(
        ["Christianity", "Islam", "Catholicism", "Hinduism", "Agnosticism", "Buddhism", "Anglicanism", "Sikhism",
         "Judaism"])
elif religionQuestion == "n":
    religion = "Atheism"
elif religionQuestion == "custom":
    religion = input("What religion do you participate in?")

# --- Pets? --- #
petsQuestion = input("Have you got any pets? ([y]es, [n]o, or [custom]")
if petsQuestion == "y":
    pets = random.choice(
        ["dog", "cat", "bird", "ferret", "fish", "frog", "gecko", "gerbil", "horse", "iguana", "mantis", "mouse",
         "newt", "pig", "rabbit", "rat", "salamander", "sheep", "snake", "spider", "turtle"])
if petsQuestion == "y":
    pets = "None"
if petsQuestion == "custom":
    pets = input("What kind of pet do you have?")

# --- Occupation --- #
job = input("What job are you applying for here?(You'll need to manually input for this one)")
jobQuestion = input("Do you enjoy this job (breaking the fourth wall, sorry)?[y]es or [n]o")
if jobQuestion == "y":
    jobSatisfaction = "Satisfied"
elif jobQuestion == "n":
    jobSatisfaction = "Unsatisfied"

# --- Income --- #
incomeQuestion = input("Do you have an income level? [r]andom or [custom]")
if incomeQuestion == "custom":
    income = input("How would you describe your income level?")
elif incomeQuestion == "r":
    income = random.choice(["Working Class", "Middle Class", "Upper Class"])

# --- Education --- #
educationQuestion = input("What is your education level? [r]andom or [custom]")
if educationQuestion == "r":
    education = random.choice(["Highschool", "College"])
elif educationQuestion == "custom":
    education = input("What is your educational level? ")

# --- Sexuality --- #
sexualityQuestion = input("What is your sexuality? [r]andom or [custom]")
if sexualityQuestion == "r":
    sexuality = random.choice(["Heterosexual", "Homosexual", "Bisexual", "Asexual"])
elif sexualityQuestion == "custom":
    sexuality = input("What is your sexuality?")

# --- Marriage --- #
marriedQuestion = input("Are you married? ([y]es, [n]o or [r]andom)")
if marriedQuestion == "y":
    married = "Yes"
elif marriedQuestion == "n":
    married = "No"
elif marriedQuestion == "r":
    married = random.choice(["Yes", "No"])

# --- Height --- #
if not birthPlace == "United States of America (USA)":
    metricSystem = True
heightQuestion = input("Let's see your height, come up here for a second. ([r]andom or [custom])")
if heightQuestion == "r":
    if metricSystem:
        heightType = "cm"
        height = str(random.randint(160, 185))
    elif not metricSystem:
        heightType = "ft"
        height = str(random.randint(5, 6)) + str(random.randint(1, 11))
elif heightQuestion == "custom":
    heightType = input("Enter 'ft' or 'cm'")
    height = input("Ah! I see your height is ")

# --- Weight --- #
weightQuestion = input("Let's see how much you weigh. ([r]andom or [custom])")
if weightQuestion == "r":
    if metricSystem:
        weightType = "kg"
        weight = str(random.randint(80, 100))
    elif not metricSystem:
        weightType = "lbs"
        weight = str(random.randint(190, 250))
elif weightQuestion == "custom":
    weightType = input("What is your weight? [lb] or [kg]]?")
    weight = input("What is your weight? Enter the number here")

# --- Conditions --- #
conditions = input("If you have any conditions or illnesses, list them here")

# --- Habits --- #
habits = input("Do you have any habits worth mentioning?")

# --- Skills --- #
skills = input("Do you have any skills that could be useful in the field?")
unskills = input("Are there any skills in which you lack?")
print("I hope none of those skills are related to your profession, otherwise your ship might be in trouble.")

# --- Jail --- #
arrested = input("Have you ever been arrested for anything? You don't have to mention, only if you feel comfortable")
convictions = input("Have you ever been convicted for anything? Again, you don't have to mention anything")

# --- Family --- #
family = input("Have any family?[r]andom or [custom]")
if family == "r":
    father = random.choice(["Alive", "Dead"])
    mother = random.choice(["Alive", "Dead"])
    sistersNum = random.randint(0, 3)
    if sistersNum > 0:
        sisters = str(sistersNum) + " sisters"
    else:
        sisters = "None"
    brothersNum = random.randint(0, 3)
    if brothersNum > 0:
        brothers = str(brothersNum) + " brothers"
    else:
        brothers = "None"
elif family == "custom":
    mother = input("Is your mother still alive?")
    father = input("Is your father still alive?")
    sisters = input("How many sisters do you have?")
    brothers = input("How many brothers do you have?")

# --- Personality --- #
print("Now I'll have my therapist here examine you to determine your personality and whether you'll be a good fit here")
# --- Psychological Issues --- #
psychissues = input("Any psychological issues with your character?")

# --- Optimist/Pessimist --- #
optimist = input("Is your character an optimist or a pessimist?[r[andom or [custom]")
if optimist == "r":
    optimist = random.choice(["Optimist", "Pessimist"])
elif optimist == "custom":
    optimist = input("Are you an optimist or a pessimist?")

strengths = input("Do you have any strengths? [r]andom or [custom]")
if strengths == "r":
    strengths = convolutionLibrary.getStrengths()
elif strengths == "custom":
    strengths = input("What are your strengths?")

weakness = input("Do you have any weaknesses?[r]andom or [custom]")
if weakness == "r":
    weakness = convolutionLibrary.getWeaknesses()
elif weakness == "custom":
    weakness = input("What are your weaknesses?")

# --- Print Statements --- #
print("Name: " + firstName + " " + lastName)
print("Nickname: " + nickName)
print("Birthday: " + birthDate)
print("Birthplace: " + birthPlace)
print()
print("Religion: " + religion)
print("Pet: " + pets)
print("Job: " + job)
print("Job Satisfaction: " + jobSatisfaction)
print("Income Level: " + income)
print("Education: " + education)
print("Sexuality: " + sexuality)
print("Married: " + married)
print("Height: " + height + heightType)
print("Weight: " + weight + weightType)
print("Conditions and Illnesses: " + conditions)
print("Habits: " + habits)
print("Skills: " + skills)
print("Unskilled: " + skills)
print("Arrests: " + arrested)
print("Convictions: " + convictions)
print("Father: " + father)
print("Mother: " + mother)
print("Sisters: " + sisters)
print("Brothers: " + brothers)
print("Psychological Issues: " + psychissues)
print("Optimist/Pessimist: " + optimist)
