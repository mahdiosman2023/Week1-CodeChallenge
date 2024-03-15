# 1. Craete dictionary that will store single letters position.
# 2. Loop through array for each letter string and single letters.
# 3. Appened each single letter that has been encountered.
# 4. Create new entry for first occurance.
# 5. Find strings with common letters.
# 6. Return empty array if no common letters found. 


def soultion (S):
    lettSequence = {}
    for i, str in enumerate(S):
        for j, singleLett in enumerate(str):
            if singleLett in lettSequence:
                lettSequence[singleLett].append((i, j))
            else:
                lettSequence[singleLett] = [(i, j)]

    for positions in lettSequence.values():
        if len(positions) > 1:
            return [positions [0][0], positions [1][0], positions [0][1]]

    return []




print(soultion(["abc","bca","dbe"])) # Output: [0, 2, 1]
print(soultion(['zzz', 'ferz', 'zdsr', 'fgtd']))  # Output: [0, 1, 3] or [1, 3, 0]
print(soultion(['gr', 'sd', 'rg']))  # Output: []
print(soultion(['bdafg', 'ceagi']))  # Output: [0, 1, 2]