from api.api import  (
    api_blueprint,
    index,
    RegisterStudent,
    AllStudents,
    Logout,
    CurrentClass,
    attendance,
    AddQuestion,
    AllQuestions,
    setSchedule,
    getSchedule
)

api_blueprint.add_url_rule('/', methods=['GET'], view_func=index)
api_blueprint.add_url_rule('/registerstudent', methods=['POST'], view_func=RegisterStudent)
api_blueprint.add_url_rule('/allstudents', methods=['GET', 'POST'], view_func=AllStudents)
api_blueprint.add_url_rule('/logout', methods=["POST", "GET"], view_func=Logout)
api_blueprint.add_url_rule('/current-class', methods=["POST", "GET"], view_func=CurrentClass)
api_blueprint.add_url_rule('/attendance/<int:id>', methods=["GET", "POST"], view_func=attendance)
api_blueprint.add_url_rule('/add-question', methods=["POST"], view_func=AddQuestion)
api_blueprint.add_url_rule('/all-questions', methods=["GET"], view_func=AllQuestions)
api_blueprint.add_url_rule('/set-schedule', methods=["POST"], view_func=setSchedule)
api_blueprint.add_url_rule('/get-schedule', methods=["GET"], view_func=getSchedule)