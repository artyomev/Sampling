from drf_yasg import openapi

team_response_schema_dict = {
        "200": openapi.Response(
            description="Get simple team view",
            examples={
                "application/json":
                    {
                        "project_id": "0",
                        'team': [
                            {'id': '1',
                             'login': 'username'},
                            {'id': '2',
                             'login': 'username'}
                        ]
                    },
                }
        )
    }

team_detailed_response_schema_dict = {
        "200": openapi.Response(
            description="Get detailed team view",
            examples={
                "application/json":
                    {
                        "project_id": "0",
                        "partner": {
                            "id": 1,
                            "username": "partner1",
                            "first_name": "",
                            "last_name": "",
                            "email": ""
                        },
                        "manager": {
                            "id": 2,
                            "username": "manager1",
                            "first_name": "",
                            "last_name": "",
                            "email": ""
                        },
                        "incharge": {
                            "id": 3,
                            "username": "incharge1",
                            "first_name": "",
                            "last_name": "",
                            "email": ""
                        },
                        "staff": [
                            {
                                "id": 4,
                                "username": "staff1",
                                "first_name": "",
                                "last_name": "",
                                "email": ""
                            },
{
                                "id": 5,
                                "username": "staff2",
                                "first_name": "",
                                "last_name": "",
                                "email": ""
                            }
                        ]
                    }
                }
        )
    }

userprojects_response_schema_dict = {"200": openapi.Response(
            description="Get users project by id",
            examples={
                "application/json":{
                    'user': 1,
                    'projects': [
                                    {
                                      "id": 0,
                                      "title": "string"
                                    },
                                    {
                                      "id": 1,
                                      "title": "string"
                                    }
                    ]

                }
            }
    )
}