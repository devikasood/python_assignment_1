def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs = lcs[::-1]
    
    return ''.join(lcs)

def find_consonant_subsequence(input_string):
    consonants = ''.join([c for c in input_string if c.isalpha() and c.lower() not in 'aeiou'])

    return consonants

def main():
    input_string = input("Enter a string: ")
    
    consonant_sequence = find_consonant_subsequence(input_string)
    
    if len(consonant_sequence) < 2:
        print("No common subsequence of consonants found.")
    else:
        lcs = longest_common_subsequence(consonant_sequence, consonant_sequence[::-1])
        print("Longest Common Subsequence of Consonants:", lcs)

if __name__ == "__main__":
    main()
