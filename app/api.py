import re

import fastapi as fa
from database import collection
from fastapi.responses import JSONResponse


apps = fa.FastAPI()


validation_rules = {
    "date": re.compile(r"^\d{4}-\d{2}-\d{2}$")
    or re.compile(r"^\d{2}\.\d{2}\.\d{4}$"),
    "phone": re.compile(r"^\+7 \d{3} \d{3} \d{2} \d{2}$"),
    "email": re.compile(r"^[\w\.-]+@[\w\.-]+$"),
    "text": re.compile(r"\w+"),
}


def validate(rule, data):
    return re.match(rule, data)


@apps.post(
    "/get_form/",
    response_class=JSONResponse,
    status_code=fa.status.HTTP_200_OK,
)
async def submit_form(form_data: fa.Request):
    data = await form_data.json()
    template_name = ""

    for template in collection.find():
        count = 0
        for name, value in template.items():

            if name in data and validate(validation_rules[value], data[name]):
                count += 1

            if count >= len(data):
                template_name = template["form_name"]
                break

    if template_name == "":
        return JSONResponse(
            content={"template": data},
            status_code=fa.status.HTTP_404_NOT_FOUND,
        )

    return JSONResponse(
        content={"template": template_name}, status_code=fa.status.HTTP_200_OK
    )
