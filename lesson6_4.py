import random
def play_game():
    min = 1
    max = 100
    target = random.randint(min,max)
    count = 0
    print(target)
    print("=========猜數字遊戲=========\n\n")
    while True:
        keyin = int(input(f"猜數字的範圍{min}~{max}:"))
        count += 1
        if keyin >=min and keyin <=max:
            if keyin == target:
                print(f"賓果!猜對了,答案是:{keyin}")
                print(f"您總共猜了多少次{count}次")
                break
            elif keyin > target:
                print("再小一點")
                max = keyin-1
            elif keyin < target:
                print("再大一點")
                min = keyin+1

            print(f"您已經猜了{count}")

        else:
            print("超出範圍")
while True:
    play_game()
    paly_again = input("您還要繼續嗎?(y or n):")
    if paly_again == "n":
        break
    else:
        print("繼續遊戲")

print("遊戲結束")