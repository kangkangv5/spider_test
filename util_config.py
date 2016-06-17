# _*_ coding: utf-8 _*_

__all__ = [
    "config_user_agent_pc",
    "config_user_agent_phone",
    "config_user_agent_all"
]


# user_agent list, include pc user_agent, phone user_agent and all user_agent
config_user_agent_pc = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"
]

config_user_agent_phone = [
    "Dalvik/1.4.0 (Linux; U; Android 2.3.6; GT-I9108 Build/GINGERBREAD)",
    "Dalvik/1.6.0 (Linux; U; Android 4.0.3; HTC T328d Build/IML74K)",
    "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-S7568 Build/IMM76D)",
    "Dalvik/1.6.0 (Linux; U; Android 4.0.4; HS-EG906 Build/IMM76D)",
    "Dalvik/1.6.0 (Linux; U; Android 4.0.4; Lenovo A630t Build/IMM76D)",
    "Dalvik/1.6.0 (Linux; U; Android 4.0.4; T29 Build/IMM76D)",
    "Dalvik/1.6.0 (Linux; U; Android 4.1.1; MI 2 MIUI/JLB54.0)",
    "Dalvik/1.6.0 (Linux; U; Android 4.1.1; MI 2S MIUI/JLB50.0)",
    "Dalvik/1.6.0 (Linux; U; Android 4.1.2; baffin3gduosctc Build/A3244509)"
]

config_user_agent_all = config_user_agent_pc + config_user_agent_phone
