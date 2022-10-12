def get_args(request, param_name, defaul_value=""):
    value = ""
    value = request.args.get(param_name)
    if value == None:
        value = request.args.get("amp;" + param_name)
    if value == None:
        value = defaul_value
    return value
