f = open('file/one.txt', encoding='utf8')
data = f.readlines()
f.close()

# get states. set of tags
states = []
for line in data:
    line = line.split()
    for word in line:
        word = word.split('|')
        if word[1] not in states:
            states.append(word[1])

# find start probability Pi for each tag
start_probability = []
for state in states:
    count = 0
    for line in data:
        line = line.split()
        if (line[0].split('|'))[1] == state:
            count += 1
    val = []
    start = count / len(data)
    val.append(state)
    val.append(start)
    start_probability.append(val)

# find transition probability from tag Ti ti tag Tj
transition_probability = []

for state in states:
    eachProb = []
    for eachState in states:
        count_transition = 0
        count_state = 0
        for line in data:
            line = line.split()
            for x in range(len(line) - 1):
                first = line[x].split('|')
                second = line[x+1].split('|')
                if first[1] == state:
                    count_state += 1
                    if second[1] == eachState:
                        count_transition += 1

        prob = count_transition / count_state
        eachProb.append(prob)

    transition_probability.append(eachProb)

# print(states)
# for state, prob in zip(states, transition_probability):
#     print(state, prob)


# find emission probability
emission_probability = []

# find list of all words
words_list = []
for line in data:
    line = line.split()
    for word in line:
        word = word.split('|')
        if word[0] not in words_list:
            words_list.append(word[0])

# find total occurrences of each tag
occurances_of_tags = []
for state in states:
    count = 0
    for line in data:
        line = line.split()
        for word in line:
            word = word.split('|')
            if word[1] == state:
                count += 1
    occurances_of_tags.append(count)
print(occurances_of_tags)

# calculate emission probability
for tag, occurances in zip(states, occurances_of_tags):
    emission_probability_of_tag = []
    for word in words_list:
        count = 0
        for line in data:
            line = line.split()
            for eachWord in line:
                eachWord = eachWord.split('|')
                if eachWord[0] == word and eachWord[1] == tag:
                    count += 1
        try:
            emission_probability_of_tag.append(count / occurances)
        except ZeroDivisionError:
            continue
    emission_probability.append(emission_probability_of_tag)

# print(words_list)
# for tag, emission_probability_of_tag_for_word in zip(states, emission_probability):
#     print(tag, emission_probability_of_tag_for_word)
