from fuzzywuzzy import fuzz

from sample import canonical_names, name_variants


for variant in name_variants:
    best_match, max_score = None, None
    for candidate in canonical_names:
        score = fuzz.ratio(variant, candidate)
        if max_score and max_score > score:
            continue
        best_match, max_score = candidate, score
    print(f"{variant},{best_match},{max_score / 100.0}")


if __name__ == "__main__":
    pass
