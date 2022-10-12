import time
import os


def save_log(data, out_dirs, specific_domain=""):
    # process directory
    out_dir = ""
    for name in out_dirs:
        out_dir += name + "/"
        if not os.path.exists(out_dir):
            os.mkdir(out_dir)

    # path
    date = time.strftime("%Y-%m-%d")
    if specific_domain == "":
        try:
            out_path = "{}/{}_{}.txt".format(
                out_dir,
                date,
                data["USERNAME"].split("@")[-1]
            )
        except:
            out_path = "{}/{}_{}.txt".format(
                out_dir,
                date,
                "other"
            )
    else:
        out_path = "{}/{}_{}.txt".format(
            out_dir,
            date,
            specific_domain
        )

    # text
    text = "TIME: " + time.strftime("%Y/%m/%d %H:%M:%S")
    for key in data:
        text += "\n\t{}: {}".format(key, data[key])
    text += "\n\n"

    # save
    with open(out_path, "a", encoding="utf8") as f:
        f.write(text)


def init_log_dir(log_dir):
    if not os.path.exists(log_dir["dir_name"]):
        os.mkdir(log_dir["dir_name"])
    for dir_name in log_dir["sub_dirs"]:
        dir_path = log_dir["dir_name"] + "/" + dir_name
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        if not os.path.exists(dir_path + "/click-mail"):
            os.mkdir(dir_path + "/click-mail")
        if not os.path.exists(dir_path + "/login-mail"):
            os.mkdir(dir_path + "/login-mail")
        if not os.path.exists(dir_path + "/open-mail"):
            os.mkdir(dir_path + "/open-mail")
