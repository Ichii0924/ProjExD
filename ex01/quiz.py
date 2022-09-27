import random

q1 ="サザエの旦那の名前は？"
q2 ="カツオの妹の名前は？"
q3 ="タラオはカツオから見てどんな間柄？"
a1 = ["ますお","マスオ","ますおさん","マスオさん"]
a2 = ["ワカメ","わかめ","昆布"]
a3 = ["甥","おい","甥っ子","おいっこ"]

q_dic = {q1:a1, q2:a2, q3:a3}

out_q = random.choice(list(q_dic.keys()))

ans = ((input(out_q)))

if ans in q_dic[out_q]:
    print("正解")
else:
    print("はずれだよ")