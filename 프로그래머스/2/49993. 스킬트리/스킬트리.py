def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        word = ''
        for s in tree:
            if s in skill:
                word = word + s
                
        if skill.startswith(word):
            answer+=1
                
            
                
    
    return answer