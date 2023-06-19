courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

durations = [14, 20, 12, 20]

def popular_names(mentors):
    all_list = []
    i=0
    for m in mentors:
        all_list.extend(mentors[i])
        i+=1
    all_names_list = []
    for mentor in all_list:
        name = mentor.split(" ")#разбиваем список общий на списки из двух элементов["имя", "фамилия"]
        all_names_list.append(name[0])#Добавляем в общий список 0-й элемент(имя)
    unique_names = set(all_names_list)
    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])
        popular.sort(key=lambda x:x[1], reverse=True)
    top_3 = popular[0:3]
    return top_3

def mentors_in_learnnig_two_courses(mentors):
    mentors_names = []
    for m in mentors:
        course_names = []
        for name in m:
            course_names.append(name.split(" ")[0])
        mentors_names.append(course_names)
    pairs = []
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 != id2:
                intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
                if len(intersection_set) > 0:
                    pair = (courses[id1], courses[id2])
                    pair1 = (courses[id2], courses[id1])
                    if pair and pair1 not in pairs:
                        pairs.append(pair)
    return sorted(intersection_set)

def duratuons_courses(courses, durations):
    courses_list = []
    for title, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title":title, "mentors":mentor, "duration":duration}
        courses_list.append(course_dict)

    mins = min(durations)
    maxs = max(durations)

    minis = []
    maxes = []
    for a, duration in enumerate(durations):
        if durations[a] == maxs:
            maxes.append(a)
        elif durations[a] == mins:
            minis.append(a)

    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]["title"]) # допишите код, который берет по id нужный курс из courses_list и получает название курса из ключа "title"
    for id in maxes:
        courses_max.append(courses_list[id]["title"])
    return courses_max
