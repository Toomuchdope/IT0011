A = {"b", "e", "d", "c", "h", "a", "j", "l"}
B = {"j", "k", "h"}
C = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"}

AB_union = A | B
print("Elements in A and B:", AB_union, "Count:", len(AB_union))

B_only = B - (A | C)
print("Elements in B that are not in A or C:", B_only, "Count:", len(B_only))

output_sets = {
    "i": {"b", "e", "d", "c", "h", "a", "j", "l"},
    "ii": {"j", "k", "h"},
    "iii": {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"},
    "iv": {"k"},
    "v": {"f", "g"},
    "vi": {"i"},
    "vii": {"m", "o", "l"}
}

for key, value in output_sets.items():
    print(f"{key}: {value}")

