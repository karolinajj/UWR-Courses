# dp[i] - the best possible score for segmenting first i characters
# dp[i] = max (dp[j] + (i - j)^2), where j is a start of a valid word
# prev[i] - the starting index of the last word ending at position i

def segment(line, words_max_len, words):
    dp = [0] * (len(line) + 1)
    prev = [-1] * (len(line) + 1)
    prev[0] = 0

    # checking if the first few characters can form valid words
    for i in range(1, min(len(line) + 1, words_max_len + 1)):
        if line[0:i] in words:
            if dp[i] < i * i:
                dp[i] = i * i
                prev[i] = 0
    
    for j in range(1, len(line)): # j - the starting postion of a valid word
        if prev[j] > -1:
            for i in range(j + 1, min(len(line) + 1, j + words_max_len + 1)):
                if line[j:i] in words:
                    if dp[i] < dp[j] + (i - j) * (i - j):
                        dp[i] = dp[j] + (i - j) * (i - j)
                        prev[i] = j
    return dp,prev

def retract(line,dp,prev):
    i = len(line)
    words = []

    while i > 0:
        words.append(line[prev[i]:i])
        i = prev[i]

    return " ".join(reversed(words))


def main():
    words = set()
    words_max_len = 0

    with open('words_for_ai1.txt', 'rb') as dictionary:
        for line in dictionary:
            line = line.decode('utf-8').strip()
            if line:  
                words.add(line)
                words_max_len = max(words_max_len, len(line))

    results = open('zad2_output.txt','w', encoding='utf-8')  
    with open('zad2_input.txt', 'rb') as lines:
        for line in lines:
            line = line.decode('utf-8').strip()
            if line:
                dp, prev = segment(line, words_max_len, words)
                result = retract(line,dp,prev)
                results.write(result)
                results.write('\n')
                # print(result)
    results.close()
main()