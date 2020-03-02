# Problem 7 Efficiency Analysis

Router tries have time complexity of O(n) where n is the number of parts (strings between slashes) in the url being searched or inserted and space complexity of O(m) where m is the number of url parts.  We use them for the same reason that we use tries for spell check and / or autocomplete - that is they are an efficient data store because we do not need to duplicate the same parts that already exist which decreases considerably the space complexity.
