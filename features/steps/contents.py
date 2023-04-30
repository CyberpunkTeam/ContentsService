import mongomock
from behave import *


@given("que no estoy registrado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when(
    'completo el registro, con nombre "{name}", apellido "{lastname}", ubicaciones "{location}" y email "{email}"'
)
def step_impl(context, name, lastname, location, email):
    """
    ""
    :param name:
    :param lastname:
    :param location:
    :param email:
    :type context: behave.runner.Context
    """

    body = {"name": name, "lastname": lastname, "location": location, "email": email}
    context.vars["user_to_save"] = body


@step("confirmo el registro")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/users"

    context.response = context.client.post(
        url, json=context.vars["user_to_save"], headers=headers
    )


@then("se me informa que se registro exitosamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201


@given('que quiero crear un contenido para el equipo "{team_name}"')
def step_impl(context, team_name):
    """
    :type context: behave.runner.Context
    """
    context.vars["tid"] = len(team_name)


@when('escribo la publicacion "{title}"')
def step_impl(context, title):
    """
    :type context: behave.runner.Context
    """
    context.vars["title"] = title


@step("la publico")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/contents"
    body = {
        "author_uid": "1",
        "title": context.vars["title"],
        "href": "mock",
        "cover_image": context.vars["cover"],
    }
    tid = context.vars.get("tid")
    if tid is not None:
        body["tid"] = tid

    context.response = context.client.post(url, json=body, headers=headers)


@then("se me informa que se publico exitosamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 201


@step('portada con la imagen "{url}"')
def step_impl(context, url):
    """
    :type context: behave.runner.Context
    """
    context.vars["cover"] = url


@given('que existe un contenido con titulo "{title}", portada "{cover}"')
def step_impl(context, title, cover):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = "/contents"
    body = {"author_uid": "1", "title": title, "href": "mock", "cover_image": cover}
    tid = context.vars.get("tid")
    if tid is not None:
        body["tid"] = tid

    response = context.client.post(url, json=body, headers=headers)
    assert response.status_code == 201
    context.vars["cid"] = response.json()["cid"]


@when('edito el titulo a "{new_title}"')
def step_impl(context, new_title):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = f"/contents/{context.vars['cid']}"
    body = {
        "title": new_title,
    }
    tid = context.vars.get("tid")
    if tid is not None:
        body["tid"] = tid

    context.response = context.client.put(url, json=body, headers=headers)


@then('veo que se cambio el titulo a "{new_title}"')
def step_impl(context, new_title):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200
    content = context.response.json()
    assert content["title"] == new_title


@when("elimino el contenido")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mimetype = "application/json"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    url = f"/contents/{context.vars['cid']}"

    context.response = context.client.delete(url, headers=headers)


@then("se me informa que se elimino correctamente")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.response.status_code == 200
