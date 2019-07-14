from flask_restful import reqparse


def only(params: list) -> dict:
    parser = reqparse.RequestParser()

    for param in params:
        parser.add_argument(param, type=dict, action='append')

    return parser.parse_args()
