VALID_EYE_COLORS = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validBirthYear(byr):
    return 1920 <= int(byr) <= 2002

def validIssueYear(iyr):
    return 2010 <= int(iyr) <= 2020

def validExpirationYear(eyr):
    return 2020 <= int(eyr) <= 2030

def validHeight(hgt):
    units = hgt[-2:]
    if units == "cm":
        return 150 <= int(hgt[:-2]) <= 193
    elif units == "in":
        return 59 <= int(hgt[:-2]) <= 76

def validHairColor(hcl):  
    if hcl[0] != '#' or len(hcl[1:]) != 6:
        return False
    for character in hcl[1:]:
        if not character.isnumeric() and character > 'f':
            return False
    return True

def validEyeColor(ecl):
    return True if ecl in VALID_EYE_COLORS else False

def validPassportID(pid):
    return pid.isnumeric() and len(pid) == 9

    
REQUIRED_FIELDS = {'byr':validBirthYear, 'iyr':validIssueYear, 'eyr':validExpirationYear, 'hgt':validHeight, 'hcl':validHairColor, 'ecl':validEyeColor, 'pid':validPassportID}

def inputStringToDict(inStr):
    retDict = {}
    categories = inStr.split()
    for category in categories:
        key,value = category.split(":")
        retDict[key] = value
    return retDict

def cleanRawData(rawData):
    passportList = []
    passport = {}
    for line in rawData:
        if not line.keys():
            passportList.append(passport)
            passport = {}
        else:
            passport.update(line)
    return passportList
            

def isValidDay1(passport):
    for field in REQUIRED_FIELDS:
        if field not in passport:
            return 0
    return 1

def isValidDay2(passport):
    for field in REQUIRED_FIELDS:
        if field not in passport or not REQUIRED_FIELDS[field](passport[field]):
            return 0
    return 1



def countValid(passportList, isValid):
    return sum([isValid(passport) for passport in passportList])


        

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        rawData = [inputStringToDict(x.strip()) for x in f.readlines()]
    passportList = cleanRawData(rawData)
    print(countValid(passportList, isValidDay2))