sid = None
class Headers:
    def __init__(self, data = None, type = None):
        headers = {
            "NDCDEVICEID": "01B592EF5658F82E1339B39AA893FF661D7E8B8F1D16227E396EF4B1BF60F33D25566A35AB1514DAB5",
            "NDC-MSG-SIG": "AaauX/ZA2gM3ozqk1U5j6ek89SMu",
            "Accept-Language": "en-US",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)",
            "Host": "service.narvii.com",
            "Accept-Encoding": "gzip",
            "Connection": "Keep-Alive"
        }
        if data: headers["Content-Length"] = str(len(data))
        if sid: headers["NDCAUTH"] = f"sid={sid}"
        if type: headers["Content-Type"] = type
        self.headers = headers
