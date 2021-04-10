# -*- coding: utf-8 -*-


from flask import Flask
from flask import request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config["test_case"] = []


class TestCaseServer(Resource):
    def get(self):
        if "id" in request.args:
            for case in app.config["test_case"]:
                if case["id"] == int(request.args["id"]):
                    return case
        else:
            return app.config["test_case"]

    def post(self):
        """
        id: 用例 id 必有字段
        description: 用例描述
        steps: 用例步骤
        """
        test_case = request.json
        if isinstance(test_case, dict):
            test_case = [test_case]
        for case in test_case:
            if "id" not in case:
                return {"result": "error", "error_code": 404, "error_message": "test case missed id"}
            app.config["test_case"].append(case)
        return {"result": "ok", "error_code": 0}


api.add_resource(TestCaseServer, "/test_case")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
