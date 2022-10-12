import os

def get_mails(app, status_type="login-mail"):
    app_dir = "log/{}/{}".format(app, status_type)
    app_dir_names = os.listdir(app_dir)
    
    mails = []
    for name in app_dir_names:
        path = app_dir + "/" + name
        try:
            with open(path) as f:
                lines = f.read().split("\n")
            for idx in range(len(lines)):
                if "PASSWORD: " not in lines[idx]:
                    continue
                pwd = lines[idx].split("PASSWORD: ")[1]
                if " " in pwd:
                    continue
                usr = lines[idx-1].split("USERNAME: ")[1]
                mails.append(usr.split("@")[0])
        except:
            continue
    mails = set(mails)
    return mails
