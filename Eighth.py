# --------გრძელი ვარიანტი--------
# import sqlite3
#
# conn = sqlite3.connect("Titanic.sqlite")
# conn.row_factory = sqlite3.Row
# cursor = conn.cursor()
#
#
# def select_female():
#     cursor.execute("SELECT COUNT(Sex) FROM Passengers WHERE Sex = 'female'")
#     for each in cursor.fetchall():
#         print("ქალების რაოდენობა:", tuple(each))
#     cursor.execute("SELECT round(((1.0 * COUNT(Sex)) / 891) * 100, 2) FROM Passengers WHERE Sex = 'female'")
#     for each in cursor.fetchall():
#         print("ქალების პროცენტული რაოდენობა:", tuple(each), "%")
#
#
# def select_male():
#     cursor.execute("SELECT COUNT(Sex) FROM Passengers WHERE Sex = 'male'")
#     for each in cursor.fetchall():
#         print("კაცების რაოდენობა:", tuple(each))
#     cursor.execute("SELECT round(((1.0 * COUNT(Sex)) / 891) * 100, 2) FROM Passengers WHERE Sex = 'male'")
#     for each in cursor.fetchall():
#         print("კაცების პროცენტული რაოდენობა:", tuple(each), "%")
#
#
# def survived_female():
#     cursor.execute("SELECT COUNT(Survived) FROM Passengers WHERE Survived = 1 and Sex = 'female'")
#     for each in cursor.fetchall():
#         print("გადარჩენილი ქალების რაოდენობა:", tuple(each))
#     cursor.execute(
#         "SELECT round(((1.0 * COUNT(Survived)) / 891) * 100, 2) FROM Passengers WHERE Survived = 1 and Sex = 'female'")
#     for each in cursor.fetchall():
#         print("გადარჩენილი ქალების პროცენტული რაოდენობა:", tuple(each), "%")
#
#
# def not_survived_female():
#     cursor.execute("SELECT COUNT(Survived) FROM Passengers WHERE Survived = 0 and Sex = 'female'")
#     for each in cursor.fetchall():
#         print("გარდაცვლილი ქალების რაოდენობა:", tuple(each))
#     cursor.execute(
#         "SELECT round(((1.0 * COUNT(Survived)) / 891) * 100, 2) FROM Passengers WHERE Survived = 0 and Sex = 'female'")
#     for each in cursor.fetchall():
#         print("გარდაცვლილი ქალების პროცენტული რაოდენობა:", tuple(each), "%")
#
#
# def survived_male():
#     cursor.execute("SELECT COUNT(Survived) FROM Passengers WHERE Survived = 1 and Sex = 'male'")
#     for each in cursor.fetchall():
#         print("გადარჩენილი კაცების რაოდენობა:", tuple(each))
#     cursor.execute(
#         "SELECT round(((1.0 * COUNT(Survived)) / 891) * 100, 2) FROM Passengers WHERE Survived = 1 and Sex = 'male'")
#     for each in cursor.fetchall():
#         print("გადარჩენილი კაცების პროცენტული რაოდენობა:", tuple(each), "%")
#
#
# def not_survived_male():
#     cursor.execute("SELECT COUNT(Survived) FROM Passengers WHERE Survived = 0 and Sex = 'male'")
#     for each in cursor.fetchall():
#         print("გარდაცვლილი კაცების რაოდენობა:", tuple(each))
#     cursor.execute(
#         "SELECT round(((1.0 * COUNT(Survived)) / 891) * 100, 2) FROM Passengers WHERE Survived = 0 and Sex = 'male'")
#     for each in cursor.fetchall():
#         print("გარდაცვლილი კაცების პროცენტული რაოდენობა:", tuple(each), "%")
#
#
# def P_class3():
#     cursor.execute("SELECT COUNT(Pclass) FROM Passengers where Pclass = 3")
#     for each in cursor.fetchall():
#         print("მესამე კლასის ბილეთების რაოდენობა:", tuple(each))
#     cursor.execute("SELECT round(((1.0 * COUNT(Pclass)) / 891) * 100, 2) FROM Passengers WHERE Pclass = 3")
#     for each in cursor.fetchall():
#         print("მესამე კლასის ბილეთების რაოდენობა პროცენტულად:", tuple(each), "%")
#
#
# def P_class2():
#     cursor.execute("SELECT COUNT(Pclass) FROM Passengers where Pclass = 2")
#     for each in cursor.fetchall():
#         print("მეორე კლასის ბილეთების რაოდენობა:", tuple(each))
#     cursor.execute("SELECT round(((1.0 * COUNT(Pclass)) / 891) * 100, 2) FROM Passengers WHERE Pclass = 3")
#     for each in cursor.fetchall():
#         print("მეორე კლასის ბილეთების რაოდენობა პროცენტულად:", tuple(each), "%")
#
#
# def P_class1():
#     cursor.execute("SELECT COUNT(Pclass) FROM Passengers where Pclass = 1")
#     for each in cursor.fetchall():
#         print("პირველი კლასის ბილეთების რაოდენობა:", tuple(each))
#     cursor.execute("SELECT round(((1.0 * COUNT(Pclass)) / 891) * 100, 2) FROM Passengers WHERE Pclass = 3")
#     for each in cursor.fetchall():
#         print("პირველი კლასის ბილეთების რაოდენობა პროცენტულად:", tuple(each), "%")
#
#
# def average3():
#     cursor.execute("SELECT ROUND(AVG(Fare), 2) AS average FROM Passengers WHERE Pclass = 3")
#     for each in cursor.fetchall():
#         print("მესამე კლასის ბილეთების საშუალო ფასი:", tuple(each))
#
#
# def average2():
#     cursor.execute("SELECT ROUND(AVG(Fare), 2) AS average FROM Passengers WHERE Pclass = 2")
#     for each in cursor.fetchall():
#         print("მეორე კლასის ბილეთების საშუალო ფასი:", tuple(each))
#
#
# def average1():
#     cursor.execute("SELECT ROUND(AVG(Fare), 2) AS average FROM Passengers WHERE Pclass = 1")
#     for each in cursor.fetchall():
#         print("პირველი კლასის ბილეთების საშუალო ფასი:", tuple(each))
#
#
# select_female()
# select_male()
# survived_female()
# not_survived_female()
# survived_male()
# not_survived_male()
# P_class3()
# P_class2()
# P_class1()
# average3()
# average2()
# average1()
#
# conn.commit()
# conn.close()

# სავარჯიშო 1
import sqlite3


def connect_db(name):
    return sqlite3.connect(name)


def count_by_gender_surv(gender, surv):
    cursor.execute("SELECT COUNT(*) FROM passengers WHERE sex = ? AND survived = ?", (gender, surv))
    res = cursor.fetchone()[0]
    print("Gender: {}; Survived: {}; რაოდენობა: {}".format(gender, surv, res))
    return res


def percent(n1, n2=891):
    return (n1 / n2) * 100


total = 891
print('გემზე იმყოფებოდა {} ადამიანი'.format(total))

conn = connect_db("titanic.sqlite")
cursor = conn.cursor()

n_female_surv = count_by_gender_surv("female", 1)
n_female_not_surv = count_by_gender_surv("female", 0)
n_male_surv = count_by_gender_surv("male", 1)
n_male_not_surv = count_by_gender_surv("male", 0)

p_female_surv = percent(n_female_surv, total)
p_female_not_surv = percent(n_female_not_surv, total)
p_male_surv = percent(n_male_surv, total)
p_male_not_surv = percent(n_male_not_surv, total)

print('ქალების % რაოდენობა (გადარჩა): {:.1f}%'.format(p_female_surv))
print('ქალების % რაოდენობა (ვერ გადარჩა): {:.1f}%'.format(p_female_not_surv))
print('კაცების % რაოდენობა (გადარჩა): {:.1f}%'.format(p_male_surv))
print('კაცების % რაოდენობა (ვერ გადარჩა): {:.1f}%'.format(p_male_not_surv))

conn.close()
# სავარჯიშო 2 (pie chart)
# from matplotlib import pyplot as plt
#
# labels = ["ქალები გადარჩნენ", "ქალები ვერ გადარჩნენ", "კაცები გადარჩნენ", "კაცები ვერ გადარჩნენ"]
# sizes = [p_female_surv, p_female_not_surv, p_male_surv, p_male_not_surv]
#
# plt.pie(sizes, labels=labels, startangle=90, radius=0.8, autopct="%1.1f%%")
# plt.savefig("diagrama1.png")
# plt.show()

# სავარჯიში 3 (Histogram)
# from matplotlib import pyplot as plt
# import numpy as np
#
#
# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         plt.annotate('{}'.format(height),
#                      xy=(rect.get_x() + rect.get_width() / 2, height),
#                      xytext=(0, 3),  # 3 points vertical offset
#                      textcoords="offset points",
#                      ha='center', va='bottom')
#
#
# labels = ["გადარჩა", "ვერ გადარჩა"]
# men_means = [n_male_surv, n_male_not_surv]
# woman_means = [n_female_surv, n_female_not_surv]
#
# ind = np.arange(len(labels))
# print(ind)
# width = 0.4
#
# rect1 = plt.bar(ind, men_means, width, label="კაცი")
# rect2 = plt.bar(ind + width, woman_means, width, label="ქალი")
# autolabel(rect1)
# autolabel(rect2)
#
# plt.xticks(ind + width / 2, labels)
# plt.title("მგზავრების სტატისტიკა")
# plt.ylabel("რაოდენობა")
# plt.legend()
# plt.show()

# სავარჯიშო 4 (შობადობის სტატისტიკა საქართველოში)
from matplotlib import pyplot as plt

x_points = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y1_total = [52_442, 56_568, 55_230, 51_565, 49_969, 49_657, 60_635, 59_249, 56_569, 53_293, 51_138, 48_296]

y2_boys = [27698, 29660, 28787, 26942, 26138, 25747, 31325,  30902, 28887, 27658, 26538, 24600]
y3_girls = [24744, 26908, 26443, 24623, 23831, 23910, 29310,  28347, 27682, 25635, 24600, 23267]

plt.plot(x_points, y1_total, marker="o", ls="--", color="g", label="სულ")
plt.plot(x_points, y2_boys, marker="1", ls="-.", label="ბიჭი")
plt.plot(x_points, y3_girls, marker="d", ls=":", label="გოგო")

plt.title("შობადობის მაჩვენებელი")
plt.xlabel("წელი")
plt.ylabel("რაოდენობა")
plt.xticks(x_points)
plt.legend()

plt.show()
