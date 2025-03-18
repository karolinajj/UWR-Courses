# dp[i] - the best possible score for segmenting first i characters
# dp[i] = max (dp[j] + (i - j)^2), where j is a start of a valid word
# prev[i] - the starting index of the last word ending at position i
import random
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

def segmentRandom(line, words_max_len, words):
    dp = [0] * (len(line) + 1)
    prev = [-1] * (len(line) + 1)
    prev[0] = 0

    # checking if the first few characters can form valid words
    for i in range(1, min(len(line) + 1, words_max_len + 1)):
        if line[0:i] in words:
            rand = random.random()
            if dp[i] < rand:
                dp[i] = rand
                prev[i] = 0
    
    for j in range(1, len(line)): # j - the starting postion of a valid word
        if prev[j] > -1:
            for i in range(j + 1, min(len(line) + 1, j + words_max_len + 1)):
                if line[j:i] in words:
                    rand = random.random()
                    if dp[i] < rand:
                        dp[i] = rand
                        prev[i] = j
    return dp,prev

def retract(line,dp,prev):
    i = len(line)
    words = []

    while i > 0:
        words.append(line[prev[i]:i])
        i = prev[i]

    return " ".join(reversed(words))


def generateSpaces():
    words = set()
    words_max_len = 0

    with open('words_for_ai1.txt', 'rb') as dictionary:
        for line in dictionary:
            line = line.decode('utf-8').strip()
            if line:  
                words.add(line)
                words_max_len = max(words_max_len, len(line))

    random.seed()
    results_smart = open('zad3cw_output_smart.txt','w', encoding='utf-8') 
    results_random = open('zad3cw_output_random.txt','w', encoding='utf-8') 

    with open('pan_tadeusz_bez_spacji.txt', 'rb') as lines:
        for line in lines:
            line = line.decode('utf-8').strip()
            if line:
                dp_smart, prev_smart = segment(line, words_max_len, words)
                dp_random, prev_random = segmentRandom(line, words_max_len, words)
                result_smart = retract(line,dp_smart,prev_smart)
                result_random = retract(line,dp_random,prev_random)
                results_smart.write(result_smart)
                results_smart.write("\n")
                results_random.write(result_random)
                results_random.write("\n")
    results_smart.close()
    results_random.close()

def main():
    generateSpaces()

    res_smart = 0
    res_random = 0
    res_correct = 0

    with open('zad3cw_output_smart.txt', 'rb') as smart_lines, \
         open('zad3cw_output_random.txt', 'rb') as random_lines, \
         open('pan_tadeusz_lowercase.txt', 'rb') as correct:
             
            for smart_line, random_line, correct_line in zip(smart_lines, random_lines, correct):
                smart_line = smart_line.decode('utf-8').strip()
                random_line = random_line.decode('utf-8').strip()
                correct_line = correct_line.decode('utf-8').strip()

                if res_correct == 0:
                    print(smart_line)
                if smart_line == correct_line:
                    res_smart += 1
                if random_line == correct_line:
                    res_random += 1
                res_correct += 1
    
    smart_lines.close()
    random_lines.close()
    correct.close()

    print(f"smart: {100 * res_smart / res_correct }\nrandom: {100 * res_random / res_correct }")



        

    

main()