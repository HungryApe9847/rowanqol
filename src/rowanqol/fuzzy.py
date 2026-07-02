from thefuzz import fuzz

def similarity_check(item, check, no_similarity_msg="[Couldn't recognise a similarity.]", similarity_needed=85):
    for i in range(len(check)):
        similarity = fuzz.ratio(item, check[i])
        if similarity > similarity_needed:
            return check[i]
    print(no_similarity_msg)
    return "error"

def similarity_compare(item1, item2, similarity_needed=85, no_similarity_msg="[Couldn't recognise a similarity.]"):
    similarity = fuzz.ratio(item1, item2)
    if similarity >= similarity_needed:
        return similarity
    print(no_similarity_msg)
    return "error"
