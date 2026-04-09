def solution(new_id):
    answer = ''
    flag = True
    while flag:
    #     1단계
        new_id = new_id.lower()
    #     2단계
        for i in new_id:
            if not ('a'<=i<='z') and not ('0'<=i<='9') and not (i in ['-','_','.']):
                new_id = new_id.replace(i,"")

    #             3단계
        while True:
            if '..' in new_id:
                new_id = new_id.replace('..', '.')
            else:
                break
    # 4단계
        if new_id.startswith('.'):
            new_id = new_id[1:]
        else:
            flag = False
        if new_id.endswith('.'):
            new_id = new_id[:len(new_id)-1]
        else:
            flag = False
    #         5단계
        if len(new_id) == 0:
            new_id+='a'
    #     6단계
        if len(new_id) >= 16:
            new_id = new_id[:15]
            if new_id.endswith('.'):
                new_id = new_id[:-1]
    #         7단계
        if len(new_id) <= 2:
            while len(new_id) <=2:
                new_id+=new_id[-1]

        
        
                
        
    return new_id