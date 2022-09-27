import random
import datetime


alpha = 10
miss_alpha = 2
count=0
max_count=5

alpha_list = [chr(ord("a")+i) for i in range(26)]

out_diss_alpha = []
#for i in range(alpha):
#    alpha_list.append(chr(random.randint(65,91)))
num = random.sample(alpha_list, k=alpha)
out_alpha=[j for j in num]
out_diss_alpha=random.sample(out_alpha, k=alpha-miss_alpha)


while count < max_count:
    print("=======================")
    print("対象文字:")
    print(out_alpha)
    print("表示文字")
    print(out_diss_alpha)
    print("=======================")

    ans1 = int(input("欠損文字はいくつあるでしょうか？"))
    if ans1 == miss_alpha:
        print("正解です。具体的に欠損文字を1つずつ入力してください。")
        ans2 = input("1つ目の文字を入力してください:")

        if ans2 not in out_diss_alpha:
            ans3 = input("２つ目の文字を入力してください:")

            if ans3 != ans2 and ans3 not in out_diss_alpha:
                print("正解です。やるな！")
                break       

            else:
                count += 1
                print("不正解です。")
        else:
            count += 1
            print("不正解です。")
    else:
        count += 1
        print("不正解です。")

    
        


