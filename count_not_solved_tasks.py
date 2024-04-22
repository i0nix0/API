from yandex_lyceum_api import *

user = User().load_credentials().auth()
course_id, group_id = user.get_course()
lessons = user.get_all_lessons(course_id, group_id)

print("Ваши нерешённые задачи или незачтённые задачи:\n")

statuses = set()

for lesson in lessons:
    if lesson['msBeforeDeadline'] < 0:
        break
    if lesson['type'] != 'normal' or lesson['numPassed'] == lesson['numTasks']:
        continue
    lesson_id = lesson['id']
    tasks = user.get_all_tasks(lesson_id, course_id)
    for task_group in tasks:
        for task in task_group['tasks']:
            solution = task['solution']
            if solution is not None:
                statuses.add(tuple(solution['status'].values()))
            if solution is None or \
                    (not solution['score'] and solution['status']['type'] != 'review'):
                print(f"{lesson['title']}: {task['title']}")
