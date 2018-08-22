positive_num = 0
negative_num = 0

for p in positive:
    positive_num += tokens.count(p)

for n in negative:
    negative_num += tokens.count(n)

positive_score_list.append(str(positive_num))

negative_score_list.append(str(negative_num))

