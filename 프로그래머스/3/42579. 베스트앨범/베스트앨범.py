from collections import defaultdict

def solution(genres, plays):
    genre_total = defaultdict(int)
    genre_list = defaultdict(list)
    genre_arr = []
    
    length = len(genres)
    
    for i in range(0, length):
        genre = genres[i]
        play = plays[i]
        
        genre_total[genre] += play
        genre_list[genre].append((play, i))
    
    for key, value in genre_list.items():
        genre_list[key] = sorted(value, reverse=True, key=lambda x: x[0])
    for key, value in genre_total.items():
        genre_arr.append((key, value))

    genre_arr.sort(reverse=True, key=lambda x: x[1])
    
    answer = []
    for g in genre_arr:
        g = g[0]
        for song in genre_list[g][:2]:
            answer.append(song[1])
    
    return answer