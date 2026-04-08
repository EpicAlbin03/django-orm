def course_list(request):
    # TODO: get all courses, render course_list.html
    pass


def course_detail(request, course_id):
    # TODO: get_object_or_404(Course, id=course_id)
    # TODO: pass course and course.students.all() to template
    pass


def delete_student(request, student_id):
    # TODO: get student, delete it, redirect to student_list
    pass


def edit_student(request, student_id):
    # TODO: GET — render edit form pre-filled with student data + all courses
    # TODO: POST — update fields from request.POST, save(), redirect to detail
    pass
