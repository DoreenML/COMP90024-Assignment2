def returnURL():
    adminName = "admin"
    adminPasswd = "adminPass"
    url = "172.26.134.245:5984/"
    # define couch
    couch_url = "http://" + adminName + ":" + adminPasswd + "@" + url
    return couch_url