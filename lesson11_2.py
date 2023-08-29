import random
def get_score()->list:
    score = []
    for i in range(5):
        score.append(random.randint(50,100))
    return score

def get_names(nums:int)->list:
    with open("names.txt",encoding='utf-8',newline='') as file:
        names_txt = file.read()
        all_names = names_txt.split(sep="\n")
        names_list = random.choices(all_names,k=nums) #取出一定數量的姓名
    return names_list


nums_int = int(input("請輸入學生數:"))
#取得nums_int個姓名
names_list = get_names(nums_int)

students = []
for i in range(nums_int):
    scores = get_score()
    new_list = [names_list[i]] + scores
    students.append(new_list)
print(students)    