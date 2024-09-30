calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    return print(len(string), string.upper(), string.lower())


def is_contains(string, lst):
    count_calls()
    return string.lower() in (item.lower() for item in lst)



string_info("bulka s makom")
string_info("banana")
string_info("apple")
result = is_contains("pizza", ["burger", "tea", "pizza"])
print(result)
result = is_contains("rocket", ["car", "burger", "cofe"])
print(result)
print(calls)