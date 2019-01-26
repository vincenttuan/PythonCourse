exam = {'數學':90, '英文':80, '國文':55}
print(len(exam))
print(exam.get('數學'))

sum = 0
for key in exam:
    score = exam.get(key)
    sum += score
    print("{} 分數= {} {}".format(key, score, '及格' if score >= 60 else '不及格'))

print(sum)
print(sum/len(exam))