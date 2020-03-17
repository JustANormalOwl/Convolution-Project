# this program uses random to make the random lists. all this stuff had to be manually put in because I couldn't find
# any of this online (obviously)
import random


def getBirthPlace(bPlace):
    if bPlace is "earth":
        countries = ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla",
                     "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria",
                     "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize",
                     "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Bouvet Island",
                     "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso",
                     "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands",
                     "Central African Republic", "Chad", "Chile", "China", "Christmas Island",
                     "Cocos (Keeling Islands)", "Colombia", "Comoros", "Congo", "Cook Islands", "Costa Rica",
                     "Cote D'Ivoire (Ivory Coast)", "Croatia (Hrvatska", "Cuba", "Cyprus", "Czech Republic", "Denmark",
                     "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador",
                     "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)",
                     "Faroe Islands", "Fiji", "Finland", "France", "France", "Metropolitan", "French Guiana",
                     "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany",
                     "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala",
                     "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and McDonald Islands", "Honduras",
                     "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
                     "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea (North)",
                     "Korea (South)", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia",
                     "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia", "Madagascar", "Malawi",
                     "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania",
                     "Mauritius", "Mayotte", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montserrat",
                     "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
                     "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue",
                     "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama",
                     "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal",
                     "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda",
                     "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and The Grenadines", "Samoa", "San Marino",
                     "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore",
                     "Slovak Republic", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
                     "S. Georgia and S. Sandwich Isls.", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon",
                     "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland",
                     "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tokelau", "Tonga",
                     "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu",
                     "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom (Britain / UK)",
                     "United States of America (USA)", "US Minor Outlying Islands", "Uruguay", "Uzbekistan", "Vanuatu",
                     "Vatican City State (Holy See)", "Venezuela", "Viet Nam", "Virgin Islands (British)",
                     "Virgin Islands (US)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia",
                     "Zaire", "Zambia", "Zimbabwe"]  # Developed by owlthechill#3266
        return random.choice(countries)
    elif bPlace is "station":
        stations = ["ISS", "Lunar Gateway", "Space Complex Alpha", "Space Complex Bravo", "Von Braun Station",
                    "Indian Space Station", "Lunar Orbital Station"]
        return random.choice(stations)
    elif bPlace is "jupiter":
        jupiters = ["Adrastea", "Aitne", "Amalthea", "Ananke", "Aoede", "Arche", "Autonoe", "Callirrhoe", "Callisto",
                    "Carme", "Carpo", "Chaldene", "Cyllene", "Dia", "Eirene", "Elara", "Erinome", "Ersa", "Euanthe",
                    "Eukelade", "Eupheme", "Euporie", "Europa", "Eurydome", "Ganymede", "Harpalyke", "Hegemone",
                    "Helike", "Hermippe", "Herse", "Himalia", "Io", "Iocaste", "Isonoe", "Kale", "Kallichore", "Kalyke",
                    "Kore", "Leda", "Lysithea", "Megaclite", "Metis", "Mneme", "Orthosie", "Pandia", "Pasiphae",
                    "Pasithee", "Philophrosyne", "Praxidike", "Sinope", "Sponde", "Taygete", "Thebe", "Thelxinoe",
                    "Themisto", "Thyone", "Valetudo"]
        return random.choice(jupiters)
    else:
        print("You messed up. Info will be incomplete unless you refill in your information properly")


def getBirthDate():
    month = random.randint(1, 12)
    if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        day = random.randint(1, 31)
    elif month == 4 or 6 or 9 or 11:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 28)

    year = random.randint(2170, 2200)

    return str(month) + "/" + str(day) + "/" + str(year)


def getPersonality():
    personalityList = ["Absent-minded", "Adaptable", "Aggressive", "Aloof", "Altruistic", "Angry", "Approval-seeking",
                       "Assertive", "Calm", "Charismatic", "Charming", "Cheerful", "Clever", "Compassionate",
                       "Compliant", "Confident", "Conforming", "Conscientious", "Considerate", "Contemplative",
                       "Courageous", "Creative", "Cruel", "Curious", "Cynical", "Decisive", "Dishonest", "Dramatic",
                       "Emotionally", "stable", "Empathetic", "Energetic", "Enthusiastic", "Extroverted", "Friendly",
                       "Forthright", "Gregarious", "Honest", "Impulsive", "Introverted", "Irritable", "Kind", "Loyal",
                       "Moody", "Narcissistic", "Neat", "Needy", "Nervous", "Neurotic", "Obedient", "Open", "to",
                       "experience", "Optimistic", "Orderly", "Resilient", "Rigid", "Risk-taking", "Self-control",
                       "Selfish", "Sensation-seeking", "Serious", "Shy", "Sociable", "Tidy", "Timid", "Trustworthy",
                       "Understanding", "Vindictive", "Warm"]
    return random.choice(personalityList)


def getStrengths():
    strengthList = ['Communicative', "Strong Work Ethic", "Good Organization", "Flexible", "Adaptable",
                    "Good Decision-Making", "Problem Solving", "Good at Analyzing", "Team Player", "Self Reliant",
                    "Self-Disciplined", "Persistent", "Resilient", "Persuasive", "Energetic", "Initiative"]
    return random.choice(strengthList)


def getWeaknesses():
    weaknessList = ['Shy', 'Bad Work Ethic', 'Bad Organization', 'Inflexible', 'Stubborn', 'Bad Decision-Making',
                    'Selfish', 'Reliant on Others', 'Non-Disciplined', 'Non-Energetic']
    return random.choice(weaknessList)
