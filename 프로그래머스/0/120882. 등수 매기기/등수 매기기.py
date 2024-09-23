def solution(score):

    avg_scores = [(s[0] + s[1]) / 2 for s in score]

    sorted_avg_scores = sorted(avg_scores, reverse=True)

    return [sorted_avg_scores.index(avg) + 1 for avg in avg_scores]