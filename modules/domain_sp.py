# static params
domains_dict = {
    "mod.gov.my": "webmail.mod.gov.my",
    "navy.mil.ph": "mail.navy.mil.ph",
    "mindef.gov.sg": "mail.defence.gov.sg",
    "afp.mil.ph": "mail3.afp.mil.ph",
    "dnd.gov.ph": "mail.dnd.gov.ph",
    "coa.gov.ph": "mail1.coa.gov.ph",
    "crdb.gov.kh": "exchange.crdb.gov.kh",
    "dfa.gov.ph": "mail.google.com",
    "mfa.gov.cn": "mail.mfa.gov.cn",
    "songjiang.gov.cn": "mailexchange.songjiang.gov.cn",
    "airforce.mil.my": "mail.airforce.mil.my",
    "navy.mil.my": "mailgw01.navy.mil.my",
    "mfaic.gov.kh": "mail.mfaic.gov.kh:2096",
    "ccccltd.cn": "mail.ccccltd.cn",
    "cetc.com.cn": "mail.cetc.com.cn",
    "icoremail.net": "hwcdn.icoremail.net",
    "hainan.gov.cn": "mail.hainan.gov.cn",
    "faohn.gov.cn": "mail.hainan.gov.cn",
    "sanya.gov.cn": "mail.sanya.gov.cn",
    "danzhou.gov.cn": "mail.hainan.gov.cn",
    "hifda.gov.cn": "mail.hainan.gov.cn",
    "lingshui.gov.cn": "mail.hainan.gov.cn",
    "yangpu.gov.cn": "mail.hainan.gov.cn",
    "changjiang.gov.cn": "mail.hainan.gov.cn",
    "dzic.gov.cn": "mail.hainan.gov.cn",
    "mef.gov.kh": "webmail.mef.gov.kh",
    "moc.gov.kh": "mail.mov.gov.kh",
    "navy.mil.my": "webmail.navy.mil.my"
}


def get_domain(mail):
    global domains_dict
    try:
        domain = mail.split("@")[-1]
        if domain in domains_dict:
            return domains_dict[domain]
        else:
            return domain
    except:
        return ""
