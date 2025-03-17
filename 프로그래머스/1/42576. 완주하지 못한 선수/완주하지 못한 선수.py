def solution(participant, completion):
    comp_dic = {}
    part_dic = {}
    for comp in completion:
        if comp in comp_dic:
            comp_dic[comp] += 1
        else:
            comp_dic[comp] = 1
    for part in participant:
        if part in part_dic:
            part_dic[part] += 1
        else:
            part_dic[part] = 1
    for key, value in part_dic.items():
        if key not in comp_dic:
            return key
        if part_dic[key] != comp_dic[key]:
            return key
