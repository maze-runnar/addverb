from api.api import  (
    api_blueprint,
    index,
    RegisterStudent,
    AllStudents,
    Logout,
    CurrentClass,
    attendance
)

api_blueprint.add_url_rule('/', methods=['GET'], view_func=index)
api_blueprint.add_url_rule('/registerstudent', methods=['POST'], view_func=RegisterStudent)
api_blueprint.add_url_rule('/allstudents', methods=['GET', 'POST'], view_func=AllStudents)
api_blueprint.add_url_rule('/logout', methods=["POST", "GET"], view_func=Logout)
api_blueprint.add_url_rule('/current-class', methods=["POST", "GET"], view_func=CurrentClass)
api_blueprint.add_url_rule('/attendance/<int:id>', methods=["GET", "POST"], view_func=attendance)
