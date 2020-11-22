from api.api import  (
    api_blueprint,
    index,
    RegisterStudent
)

api_blueprint.add_url_rule('/', methods=['GET'], view_func=index)
api_blueprint.add_url_rule('/registerstudent', methods=['POST'], view_func=RegisterStudent)
