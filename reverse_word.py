def solution(s):
    return " ".join([elem for elem in s.split(" ") if elem!=""][::-1])
print(solution("apple is          red           "))