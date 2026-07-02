from thefuzz import fuzz, process

def similarity_check(item, check, no_similarity_msg="[Couldn't recognise a similarity.]", similarity_needed=85):
    match, score = process.extractOne(item, check, scorer=fuzz.ratio)
    if score > similarity_needed:
        return match
    print(no_similarity_msg)
    return "error"

def similarity_compare(item1, item2, similarity_needed=85, no_similarity_msg="[Couldn't recognise a similarity.]"):
    similarity = fuzz.ratio(item1, item2)
    if similarity >= similarity_needed:
        return item2
    print(no_similarity_msg)
    return "error"
