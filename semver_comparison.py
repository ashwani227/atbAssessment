import re


def convert_text(text):
    # Convert string to integer if it is a number otherwise returns the same text
    return int(text) if re.match("^[0-9]+$", text) else text


def split(key):
    # Split the string into a list with dot as seperator
    # Return array of converted integers or strings
    return [convert_text(x) for x in key.split(".")]


def compare_two_strings(a, b):
    # Return the result as integer. True is considered as 1 and false as 0
    return (a > b) - (a < b)


def compare_version(a, b):
    # Split the string into list using split function defined above
    a_split, b_split = split(a), split(b)
    for sub_a, sub_b in zip(a_split, b_split):
        # Compare each substring with one another
        result = compare_two_strings(sub_a, sub_b)
        if result != 0:
            # If result is a number other than 0, comparison is already clear and no need to check other parts
            return result


def hyphen_seperator(version):
    # Split the string based on '-'. If string doesn't have - then append an empty element to show
    if '-' in version:
        return version.split('-')
    else:
        return [version, '']


def determinePrecedence(v1, v2):
    # Get both the parts separately for both versions
    before_hyphen_v1, after_hyphen_v1 = hyphen_seperator(v1)
    before_hyphen_v2, after_hyphen_v2 = hyphen_seperator(v2)

    # Compare Major, Minor and Patch. If it is not None, compare pre_release_result.
    major_minor_patch_result = compare_version(before_hyphen_v1, before_hyphen_v2)
    if major_minor_patch_result:
        return major_minor_patch_result

    pre_release_result = compare_two_strings(after_hyphen_v1, after_hyphen_v2)
    return pre_release_result


def get_highest_precedence(semver_list):
    # Return the semver with highest priority 
    most_prior = semver_list[0]
    for semver in semver_list:
        if determinePrecedence(semver, most_prior)==1:
            most_prior = semver
    return most_prior



def main():
    # List of semvers to be compared
    semver_list = ['1.0.0', '1.1.0-beta.10', '1.1.0-beta.10']

    # Determining precedence between 2 versions
    result = determinePrecedence('2.1.9-beta.10', '2.1.9-beta.1')

    # If result is 1 then return True as you can go ahead with the new updates
    # If result is 0 which means it is the same version as before and no need for the update
    # If result < 0 then before version is of higher precedence
    if result > 0:
        decision = True
    else:
        decision = False
    print(decision)

    high_precedence_version = get_highest_precedence(semver_list)
    print(high_precedence_version)
    
    return decision

if __name__ == '__main__':
    main()
