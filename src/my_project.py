import re

def log2(login, passw, A_passw ):
    res_err = ""
    res = False

    try:
        black_list = ['89515972720', 'sofiadubinkina18@gmail.com', '89999999999']
        login_ok = True

        if len(login)< 5:
            res_err = 'Login too short'
            login_ok = False
        elif login in black_list:
            res_err = 'Login is bad(blacklist)'
            login_ok = False
        elif login_ok:
            if "@" in login:
                if re.fullmatch(r"^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$", login):
                    login_ok = True
                else:
                    res_err = 'Non correct email format "exsample@exampl.com"'
                    login_ok = False
            elif login[0] in "8":
                if re.fullmatch(r"^8\d{10}$", login):
                    login_ok = True
                else:
                    res_err = 'Non correct number format "8xxxxxxxxxx"'
                    login_ok = False
            elif login[0] in "+":
                if re.fullmatch(r"^\+7-\d{3}-\d{3}-\d{2}\d{2}$", login):
                    login_ok = True
                else:
                    res_err = 'Non correct number format "+7-xxx-xxx-xxxx"'
                    login_ok = False
            else:
                a = b = c = err = False
                for i in login:
                    if re.fullmatch(r"[A-Za-z]",i):
                        a = True
                    elif re.fullmatch(r"\d",i):
                        b = True
                    elif re.fullmatch(r"_",i):
                        c = True
                    else:
                        err = True
                if not a :
                    res_err = 'Login without letter'
                    login_ok = False
                elif not b :
                    res_err = 'Login without numbers'
                    login_ok = False
                elif not c :
                    res_err = 'Login without "_" simbols'
                    login_ok = False
                elif err :
                    res_err = 'Login with cirilic letter'
                    login_ok = False
                else:
                    login_ok = True
        if not login_ok and res_err == "":
            res_err = 'Login no pattern matched'
        elif res_err != "":
            res = False
        else:
            if len(passw) < 7:
                res_err = 'Password too short'
            else:
                a = b = c = d = err = False
                for i in passw:
                    if re.fullmatch(r"[А-ЯЁ]", i):
                        a = True
                    elif re.fullmatch(r"[а-яё]", i):
                        b = True
                    elif re.fullmatch(r"\d", i):
                        c = True
                    elif re.fullmatch(r"[^A-Za-z0-9А-Яа-яЁё]", i):
                        d = True
                    else:
                        err = True
                if err : res_err = 'Password with Latin letter'
                elif not a : res_err = 'Password not big letter'
                elif not b : res_err = 'Password not small letter'
                elif not c : res_err = 'Password not numbers'
                elif not d : res_err = 'Password not special simbols'
                elif passw != A_passw : res_err = 'Second password not matched'
                if res_err == '':
                    res = True
    except Exception:
        res = False
        res_err = 'Internal error'
    # print(res)
    # print(res_err)
    return res, res_err