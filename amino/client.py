import json
import base64
import requests
from uuid import UUID
from os import urandom
from time import timezone
from typing import BinaryIO
from binascii import hexlify
from time import time as timestamp
from locale import getdefaultlocale as locale
from . import headers, objects
from .socket import Callbacks, SocketHandler


device_id = "01B592EF5658F82E1339B39AA893FF661D7E8B8F1D16227E396EF4B1BF60F33D25566A35AB1514DAB5"
device_id_sig = "AaauX/ZA2gM3ozqk1U5j6ek89SMu"
user_agent = "Dalvik/2.1.0 (Linux; U; Android 7.1; LG-UK495 Build/MRA58K; com.narvii.amino.master/3.3.33180)"

class Client:
    def __init__(self, callback = Callbacks, proxies: dict = None, certificatePath = None, socket_trace = False):
        self.api = "https://service.narvii.com/api/v1"
        self.authenticated = False
        self.configured = False
        self.user_agent = user_agent
        self.device_id = device_id
        self.device_id_sig = device_id_sig
        self.socket = SocketHandler(self, socket_trace=socket_trace)
        self.callbacks = callback(self)
        self.proxies = proxies
        self.certificatePath = certificatePath
        self.json = None
        self.sid = None
        self.userId = None
        self.account: objects.UserProfile = objects.UserProfile(None)
        self.profile: objects.UserProfile = objects.UserProfile(None)
        self.check_device(device_id)

    def login(self, email: str, password: str):
        data = json.dumps({
            "email": email,
            "v": 2,
            "secret": f"0 {password}",
            "deviceID": self.device_id,
            "clientType": 100,
            "action": "normal",
            "timestamp": int(timestamp() * 1000)
        })
        response = requests.post(f"{self.api}/g/s/auth/login", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else:
            self.authenticated = True
            self.json = json.loads(response.text)
            self.sid = self.json["sid"]
            self.userId = self.json["account"]["uid"]
            self.account: objects.UserProfile = objects.UserProfile(self.json["account"]).UserProfile
            self.profile: objects.UserProfile = objects.UserProfile(self.json["userProfile"]).UserProfile
            headers.sid = self.sid
            self.socket.start()
            return response.status_code

    def register(self, nickname: str, email: str, password: str, deviceId: str = device_id):
        data = json.dumps({
            "secret": f"0 {password}",
            "deviceID": deviceId,
            "email": email,
            "clientType": 100,
            "nickname": nickname,
            "latitude": 0,
            "longitude": 0,
            "address": None,
            "clientCallbackURL": "narviiapp://relogin",
            "type": 1,
            "identity": email,
            "timestamp": int(timestamp() * 1000)
        })
        response = requests.post(f"{self.api}/g/s/auth/register", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def restore(self, email: str, password: str):
        data = json.dumps({
            "secret": f"0 {password}",
            "deviceID": device_id,
            "email": email,
            "timestamp": int(timestamp() * 1000)
        })
        response = requests.post(f"{self.api}/g/s/account/delete-request/cancel", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def logout(self):
        data = json.dumps({
            "deviceID": self.device_id,
            "clientType": 100,
            "timestamp": int(timestamp() * 1000)
        })
        response = requests.post(f"{self.api}/g/s/auth/logout", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: self.authenticated = False; return response.status_code

    def configure(self, age: int, gender: str):
        if gender.lower() == "male": gender = 1
        elif gender.lower() == "female": gender = 2
        elif gender.lower() == "non-binary": gender = 255
        else: raise exceptions.SpecifyType
        if age <= 12: raise exceptions.AgeTooLow
        data = json.dumps({
            "age": age,
            "gender": gender,
            "timestamp": int(timestamp() * 1000)
        })
        response = requests.post(f"{self.api}/g/s/persona/profile/basic", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def verify(self, email: str, code: str):
        data = json.dumps({
            "validationContext": {
                "type": 1,
                "identity": email,
                "data": {"code": code}},
            "deviceID": device_id,
            "timestamp": int(timestamp() * 1000)
        })
        response = requests.post(f"{self.api}/g/s/auth/check-security-validation", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def request_verify_code(self, email: str, resetPassword: bool = False):
        data = {
            "identity": email,
            "type": 1,
            "deviceID": device_id
        }
        if resetPassword is True:
            data["level"] = 2
            data["purpose"] = "reset-password"
        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/auth/request-security-validation", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def activate_account(self, email: str, code: str):
        data = json.dumps({
            "type": 1,
            "identity": email,
            "data": {"code": code},
            "deviceID": device_id
        })
        response = requests.post(f"{self.api}/g/s/auth/activate-email", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def delete_account(self, password: str):
        data = json.dumps({
            "deviceID": device_id,
            "secret": f"0 {password}"
        })
        response = requests.post(f"{self.api}/g/s/account/delete-request", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def change_password(self, email: str, password: str, code: str):
        data = json.dumps({
            "updateSecret": f"0 {password}",
            "emailValidationContext": {
                "data": {
                    "code": code
                },
                "type": 1,
                "identity": email,
                "level": 2,
                "deviceID": device_id
            },
            "phoneNumberValidationContext": None,
            "deviceID": device_id
        })
        response = requests.post(f"{self.api}/g/s/auth/reset-password", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def check_device(self, deviceId: str):
        data = json.dumps({
            "deviceID": deviceId,
            "bundleID": "com.narvii.amino.master",
            "clientType": 100,
            "timezone": -timezone // 1000,
            "systemPushEnabled": True,
            "locale": locale()[0],
            "timestamp": int(timestamp() * 1000)
        })
        response = requests.post(f"{self.api}/g/s/device", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: self.configured = True; return response.status_code

    def upload_media(self, file: BinaryIO):
        data = file.read()
        response = requests.post(f"{self.api}/g/s/media/upload", data=data, headers=headers.Headers(type=f"image/jpg", data=data).headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return json.loads(response.text)["mediaValue"]

    def handle_socket_message(self, data):
        return self.callbacks.resolve(data)

    def sub_clients(self, start: int = 0, size: int = 25):
        if not self.authenticated: raise exceptions.NotLoggedIn
        response = requests.get(f"{self.api}/g/s/community/joined?v=1&start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.CommunityList(json.loads(response.text)["communityList"]).CommunityList

    def get_user_info(self, userId: str):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.UserProfile(json.loads(response.text)["userProfile"]).UserProfile

    def get_chat_threads(self, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/chat/thread?type=joined-me&start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.ThreadList(json.loads(response.text)["threadList"]).ThreadList

    def get_chat_thread(self, chatId: str):
        response = requests.get(f"{self.api}/g/s/chat/thread/{chatId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.Thread(json.loads(response.text)["thread"]).Thread

    def get_chat_users(self, chatId: str, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/chat/thread/{chatId}/member?start={start}&size={size}&type=default&cv=1.2", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.UserProfileList(json.loads(response.text)["memberList"]).UserProfileList

    def join_chat(self, chatId: str):
        response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/member/{self.userId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def leave_chat(self, chatId: str):
        response = requests.delete(f"{self.api}/g/s/chat/thread/{chatId}/member/{self.userId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def start_chat(self, userId: [str, list], message: str, title: str = None, content: str = None, isGlobal: bool = False, publishToGlobal: bool = False):
        if isinstance(userId, str): userIds = [userId]
        elif isinstance(userId, list): userIds = userId
        else: raise exceptions.WrongType
        data = {
            "title": title,
            "inviteeUids": userIds,
            "initialMessageContent": message,
            "content": content,
            "timestamp": int(timestamp() * 1000)
        }
        if isGlobal is True: data["type"] = 2; data["eventSource"] = "GlobalComposeMenu"
        else: data["type"] = 0
        if publishToGlobal is True: data["publishToGlobal"] = 1
        else: data["publishToGlobal"] = 0
        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/chat/thread", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def invite_to_chat(self, userId: [str, list], chatId: str):
        if isinstance(userId, str): userIds = [userId]
        elif isinstance(userId, list): userIds = userId
        else: raise exceptions.WrongType
        data = json.dumps({
            "uids": userIds,
            "timestamp": int(timestamp() * 1000)
        })
        response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/member/invite", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def get_chat_messages(self, chatId: str, size: int = 25, pageToken: str = None):
        if pageToken is not None: url = f"{self.api}/g/s/chat/thread/{chatId}/message?v=2&pagingType=t&pageToken={pageToken}&size={size}"
        else: url = f"{self.api}/g/s/chat/thread/{chatId}/message?v=2&pagingType=t&size={size}"
        response = requests.get(url, headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.GetMessages(json.loads(response.text)).GetMessages

    def get_message_info(self, chatId: str, messageId: str):
        response = requests.get(f"{self.api}/g/s/chat/thread/{chatId}/message/{messageId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.Message(json.loads(response.text)["message"]).Message

    def get_community_info(self, comId: str):
        response = requests.get(f"{self.api}/g/s-x{comId}/community/info?withInfluencerList=1&withTopicList=true&influencerListOrderStrategy=fansCount", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.Community(json.loads(response.text)["community"]).Community

    def search_community(self, aminoId: str):
        response = requests.get(f"{self.api}/g/s/search/amino-id-and-link?q={aminoId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else:
            response = json.loads(response.text)["resultList"]
            if len(response) == 0: raise exceptions.CommunityNotFound
            else: return objects.CommunityList([com["refObject"] for com in response]).CommunityList

    def get_user_following(self, userId: str, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/joined?start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.UserProfileList(json.loads(response.text)["userProfileList"]).UserProfileList

    def get_user_followers(self, userId: str, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/member?start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.UserProfileList(json.loads(response.text)["userProfileList"]).UserProfileList

    def get_user_visitors(self, userId: str, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/visitors?start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.VisitorsList(json.loads(response.text)).VisitorsList

    def get_blocked_users(self, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/block?start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.UserProfileList(json.loads(response.text)["userProfileList"]).UserProfileList

    def get_blog_info(self, blogId: str = None, wikiId: str = None, quizId: str = None, fileId: str = None):
        if blogId or quizId:
            if quizId is not None: blogId = quizId
            response = requests.get(f"{self.api}/g/s/blog/{blogId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
            if response.status_code != 200: return json.loads(response.text)
            else: return objects.GetBlogInfo(json.loads(response.text)).GetBlogInfo
        elif wikiId:
            response = requests.get(f"{self.api}/g/s/item/{wikiId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
            if response.status_code != 200: return json.loads(response.text)
            else: return objects.GetWikiInfo(json.loads(response.text)).GetWikiInfo
        elif fileId:
            response = requests.get(f"{self.api}/g/s/shared-folder/files/{fileId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
            if response.status_code != 200: return json.loads(response.text)
            else: return objects.SharedFolderFile(json.loads(response.text)["file"]).SharedFolderFile
        else: raise exceptions.SpecifyType()

    def get_blog_comments(self, blogId: str = None, wikiId: str = None, quizId: str = None, fileId: str = None, sorting: str = "newest", start: int = 0, size: int = 25):
        if sorting == "newest": sorting = "newest"
        elif sorting == "oldest": sorting = "oldest"
        elif sorting == "top": sorting = "vote"
        if blogId or quizId:
            if quizId is not None: blogId = quizId
            response = requests.get(f"{self.api}/g/s/blog/{blogId}/comment?sort={sorting}&start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        elif wikiId: response = requests.get(f"{self.api}/g/s/item/{wikiId}/comment?sort={sorting}&start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        elif fileId: response = requests.get(f"{self.api}/g/s/shared-folder/files/{fileId}/comment?sort={sorting}&start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        else: raise exceptions.SpecifyType()
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.CommentList(json.loads(response.text)["commentList"]).CommentList

    def get_blocker_users(self, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/block/full-list?start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return json.loads(response.text)["blockerUidList"]

    def get_wall_comments(self, userId: str, sorting: str, start: int = 0, size: int = 25):
        if sorting.lower() == "newest": sorting = "newest"
        elif sorting.lower() == "oldest": sorting = "oldest"
        elif sorting.lower() == "top": sorting = "vote"
        else: raise exceptions.SpecifyType
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/g-comment?sort={sorting}&start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.CommentList(json.loads(response.text)["commentList"]).CommentList

    def flag(self, reason: str, flagType: int, userId: str = None, blogId: str = None, wikiId: str = None, asGuest: bool = False):
        if reason is None: raise exceptions.ReasonNeeded
        if flagType is None: raise exceptions.FlagTypeNeeded
        data = {
            "flagType": flagType,
            "message": reason,
            "timestamp": int(timestamp() * 1000)
        }
        if userId:
            data["objectId"] = userId
            data["objectType"] = 0
        elif blogId:
            data["objectId"] = blogId
            data["objectType"] = 1
        elif wikiId:
            data["objectId"] = wikiId
            data["objectType"] = 2
        else: raise exceptions.SpecifyType
        if asGuest: flg = "g-flag"
        else: flg = "flag"
        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/{flg}", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def send_message(self, chatId: str, message: str = None, messageType: int = 0, file: BinaryIO = None, fileType: str = None, replyTo: str = None, mentionUserIds: list = None, stickerId: str = None, embedId: str = None, embedType: int = None, embedLink: str = None, embedTitle: str = None, embedContent: str = None, embedImage: BinaryIO = None):
        if message is not None and file is None:
            message = message.replace("<$", "‎‏").replace("$>", "‬‭")
        mentions = []
        if mentionUserIds:
            for mention_uid in mentionUserIds:
                mentions.append({"uid": mention_uid})
        if embedImage:
            embedImage = [[100, self.upload_media(embedImage), None]]
        data = {
            "type": messageType,
            "content": message,
            "clientRefId": int(timestamp() / 10 % 1000000000),
            "attachedObject": {
                "objectId": embedId,
                "objectType": embedType,
                "link": embedLink,
                "title": embedTitle,
                "content": embedContent,
                "mediaList": embedImage
            },
            "extensions": {"mentionedArray": mentions},
            "timestamp": int(timestamp() * 1000)
        }
        if replyTo: data["replyMessageId"] = replyTo
        if stickerId:
            data["content"] = None
            data["stickerId"] = stickerId
            data["type"] = 3
        if file:
            data["content"] = None
            if fileType == "audio":
                data["type"] = 2
                data["mediaType"] = 110
            elif fileType == "image":
                data["mediaType"] = 100
                data["mediaUploadValueContentType"] = "image/jpg"
                data["mediaUhqEnabled"] = True
            elif fileType == "gif":
                data["mediaType"] = 100
                data["mediaUploadValueContentType"] = "image/gif"
                data["mediaUhqEnabled"] = True
            else: raise exceptions.SpecifyType
            data["mediaUploadValue"] = base64.b64encode(file.read()).decode()
        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/message", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def delete_message(self, chatId: str, messageId: str, asStaff: bool = False, reason: str = None):
        data = {
            "adminOpName": 102,
            "adminOpNote": {"content": reason},
            "timestamp": int(timestamp() * 1000)
        }
        data = json.dumps(data)
        if not asStaff: response = requests.delete(f"{self.api}/g/s/chat/thread/{chatId}/message/{messageId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        else: response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/message/{messageId}/admin", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def mark_as_read(self, chatId: str, messageId: str):
        data = json.dumps({
            "messageId": messageId,
            "timestamp": int(timestamp() * 1000)
        })
        response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/mark-as-read", headers=headers.Headers().headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def edit_chat(self, chatId: str, doNotDisturb: bool = None, pinChat: bool = None, title: str = None, icon: str = None, backgroundImage: str = None, content: str = None, announcement: str = None, coHosts: list = None, keywords: list = None, pinAnnouncement: bool = None, publishToGlobal: bool = None, canTip: bool = None, viewOnly: bool = None, canInvite: bool = None, fansOnly: bool = None):
        data = {"timestamp": int(timestamp() * 1000)}
        if title: data["title"] = title
        if content: data["content"] = content
        if icon: data["icon"] = icon
        if keywords: data["keywords"] = keywords
        if announcement: data["extensions"] = {"announcement": announcement}
        if pinAnnouncement: data["extensions"] = {"pinAnnouncement": pinAnnouncement}
        if fansOnly: data["extensions"] = {"fansOnly": fansOnly}
        if publishToGlobal: data["publishToGlobal"] = 0
        if not publishToGlobal: data["publishToGlobal"] = 1
        res = []
        if doNotDisturb is not None:
            if doNotDisturb:
                data = json.dumps({"alertOption": 2, "timestamp": int(timestamp() * 1000)})
                response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/member/{self.userId}/alert", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
                if response.status_code != 200: res.append(print(json.loads(response.text)))
                else: res.append(response.status_code)
            if not doNotDisturb:
                data = json.dumps({"alertOption": 1, "timestamp": int(timestamp() * 1000)})
                response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/member/{self.userId}/alert", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
                if response.status_code != 200: res.append(print(json.loads(response.text)))
                else: res.append(response.status_code)
        if pinChat is not None:
            if pinChat:
                response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/pin", data=data, headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
                if response.status_code != 200: res.append(print(json.loads(response.text)))
                else: res.append(response.status_code)
            if not pinChat:
                response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/unpin", data=data, headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
                if response.status_code != 200: res.append(print(json.loads(response.text)))
                else: res.append(response.status_code)
        if backgroundImage is not None:
            data = json.dumps({"media": [100, backgroundImage, None], "timestamp": int(timestamp() * 1000)})
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/member/{self.userId}/background", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
            if response.status_code != 200: res.append(print(json.loads(response.text)))
            else: res.append(response.status_code)
        if coHosts is not None:
            data = json.dumps({"uidList": coHosts, "timestamp": int(timestamp() * 1000)})
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/co-host", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
            if response.status_code != 200: res.append(print(json.loads(response.text)))
            else: res.append(response.status_code)
        if viewOnly is not None:
            if viewOnly:
                response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/view-only/enable", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
                if response.status_code != 200: res.append(print(json.loads(response.text)))
                else: res.append(response.status_code)
            if not viewOnly:
                response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/view-only/disable", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
                if response.status_code != 200: res.append(print(json.loads(response.text)))
                else: res.append(response.status_code)
        if canInvite is not None:
            if canInvite:
                response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/members-can-invite/enable", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
                if response.status_code != 200: res.append(print(json.loads(response.text)))
                else: res.append(response.status_code)
            if not canInvite:
                response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/members-can-invite/disable", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
                if response.status_code != 200: res.append(print(json.loads(response.text)))
                else: res.append(response.status_code)
        if canTip is not None:
            if canTip:
                response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/tipping-perm-status/enable", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
                if response.status_code != 200: res.append(print(json.loads(response.text)))
                else: res.append(response.status_code)
            if not canTip:
                response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/tipping-perm-status/disable", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
                if response.status_code != 200: res.append(print(json.loads(response.text)))
                else: res.append(response.status_code)
        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: res.append(print(json.loads(response.text)))
        else: res.append(response.status_code)
        return res

    def visit(self, userId: str):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}?action=visit", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def send_coins(self, coins: int, blogId: str = None, chatId: str = None, objectId: str = None, transactionId: str = None):
        url = None
        if transactionId is None: transactionId = str(UUID(hexlify(urandom(16)).decode('ascii')))
        data = {
            "coins": coins,
            "tippingContext": {"transactionId": transactionId},
            "timestamp": int(timestamp() * 1000)
        }
        if blogId is not None: url = f"{self.api}/g/s/blog/{blogId}/tipping"
        if chatId is not None: url = f"{self.api}/g/s/chat/thread/{chatId}/tipping"
        if objectId is not None:
            data["objectId"] = objectId
            data["objectType"] = 2
            url = f"{self.api}/g/s/tipping"
        if url is None: raise exceptions.SpecifyType()
        data = json.dumps(data)
        response = requests.post(url, headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def follow(self, userId: [str, list]):
        if isinstance(userId, str):
            response = requests.post(f"{self.api}/g/s/user-profile/{userId}/member", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        elif isinstance(userId, list):
            data = json.dumps({"targetUidList": userId, "timestamp": int(timestamp() * 1000)})
            response = requests.post(f"{self.api}/g/s/user-profile/{self.userId}/joined", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        else: raise exceptions.WrongType
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def unfollow(self, userId: str):
        response = requests.delete(f"{self.api}/g/s/user-profile/{userId}/member/{self.userId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def block(self, userId: str):
        response = requests.post(f"{self.api}/g/s/block/{userId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def unblock(self, userId: str):
        response = requests.delete(f"{self.api}/g/s/block/{userId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def join_community(self, comId: str, invitationId: str = None):
        data = {"timestamp": int(timestamp() * 1000)}
        if invitationId: data["invitationId"] = invitationId
        data = json.dumps(data)
        response = requests.post(f"{self.api}/x{comId}/s/community/join", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def request_join_community(self, comId: str, message: str = None):
        data = json.dumps({"message": message, "timestamp": int(timestamp() * 1000)})
        response = requests.post(f"{self.api}/x{comId}/s/community/membership-request", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def leave_community(self, comId: str):
        response = requests.post(f"{self.api}/x{comId}/s/community/leave", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def flag_community(self, comId: str, reason: str, flagType: int, isGuest: bool = False):
        if reason is None: raise exceptions.ReasonNeeded
        if flagType is None: raise exceptions.FlagTypeNeeded
        data = json.dumps({
            "objectId": comId,
            "objectType": 16,
            "flagType": flagType,
            "message": reason,
            "timestamp": int(timestamp() * 1000)
        })
        if isGuest: flg = "g-flag"
        else: flg = "flag"
        response = requests.post(f"{self.api}/x{comId}/s/{flg}", data=data, headers=headers.Headers(data=data).headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def edit_profile(self, nickname: str = None, content: str = None, icon: str = None, backgroundColor: str = None, backgroundImage: str = None, defaultBubbleId: str = None):
        data = {
            "address": None,
            "latitude": 0,
            "longitude": 0,
            "mediaList": None,
            "eventSource": "UserProfileView",
            "timestamp": int(timestamp() * 1000)
        }
        if nickname: data["nickname"] = nickname
        if icon: data["icon"] = icon
        if content: data["content"] = content
        if backgroundColor: data["extensions"] = {"style": {"backgroundColor": backgroundColor}}
        if backgroundImage: data["extensions"] = {"style": {"backgroundMediaList": [[100, backgroundImage, None, None, None]]}}
        if defaultBubbleId: data["extensions"] = {"defaultBubbleId": defaultBubbleId}
        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/user-profile/{self.userId}", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def set_privacy_status(self, isAnonymous: bool = False, getNotifications: bool = False):
        data = {"timestamp": int(timestamp() * 1000)}
        if not isAnonymous: data["privacyMode"] = 1
        if isAnonymous: data["privacyMode"] = 2
        if not getNotifications: data["notificationStatus"] = 2
        if getNotifications: data["privacyMode"] = 1
        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/account/visit-settings", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def set_amino_id(self, aminoId: str):
        data = json.dumps({"aminoId": aminoId, "timestamp": int(timestamp() * 1000)})
        response = requests.post(f"{self.api}/g/s/account/change-amino-id", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def get_linked_communities(self, userId: str):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/linked-community", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.CommunityList(json.loads(response.text)["linkedCommunityList"]).CommunityList

    def get_unlinked_communities(self, userId: str):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/linked-community", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.CommunityList(json.loads(response.text)["unlinkedCommunityList"]).CommunityList

    def reorder_linked_communities(self, comIds: list):
        data = json.dumps({"ndcIds": comIds, "timestamp": int(timestamp() * 1000)})
        response = requests.post(f"{self.api}/g/s/user-profile/{self.userId}/linked-community/reorder", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def add_linked_community(self, comId: str):
        response = requests.post(f"{self.api}/g/s/user-profile/{self.userId}/linked-community/{comId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def remove_linked_community(self, comId: str):
        response = requests.delete(f"{self.api}/g/s/user-profile/{self.userId}/linked-community/{comId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def comment(self, message: str, userId: str = None, blogId: str = None, wikiId: str = None, replyTo: str = None):
        if message is None: raise exceptions.MessageNeeded
        data = {
            "content": message,
            "stickerId": None,
            "type": 0,
            "timestamp": int(timestamp() * 1000)
        }
        if replyTo: data["respondTo"] = replyTo
        if userId:
            data["eventSource"] = "UserProfileView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/user-profile/{userId}/g-comment", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        elif blogId:
            data["eventSource"] = "PostDetailView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/blog/{blogId}/g-comment", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        elif wikiId:
            data["eventSource"] = "PostDetailView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/item/{wikiId}/g-comment", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        else: raise exceptions.SpecifyType
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def delete_comment(self, commentId: str, userId: str = None, blogId: str = None, wikiId: str = None):
        if userId: response = requests.delete(f"{self.api}/g/s/user-profile/{userId}/g-comment/{commentId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        elif blogId: response = requests.delete(f"{self.api}/g/s/blog/{blogId}/g-comment/{commentId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        elif wikiId: response = requests.delete(f"{self.api}/g/s/item/{wikiId}/g-comment/{commentId}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        else: raise exceptions.SpecifyType
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def like_blog(self, blogId: [str, list] = None, wikiId: str = None):
        data = {
            "value": 4,
            "timestamp": int(timestamp() * 1000)
        }
        if blogId:
            if isinstance(blogId, str):
                data["eventSource"] = "UserProfileView"
                data = json.dumps(data)
                response = requests.post(f"{self.api}/g/s/blog/{blogId}/g-vote?cv=1.2", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
            elif isinstance(blogId, list):
                data["targetIdList"] = blogId
                data = json.dumps(data)
                response = requests.post(f"{self.api}/g/s/feed/g-vote", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
            else: raise exceptions.WrongType
        elif wikiId:
            data["eventSource"] = "PostDetailView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/item/{wikiId}/g-vote?cv=1.2", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        else: raise exceptions.SpecifyType
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def unlike_blog(self, blogId: str = None, wikiId: str = None):
        if blogId: response = requests.delete(f"{self.api}/g/s/blog/{blogId}/g-vote?eventSource=UserProfileView", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        elif wikiId: response = requests.delete(f"{self.api}/g/s/item/{wikiId}/g-vote?eventSource=PostDetailView", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        else: raise exceptions.SpecifyType
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def like_comment(self, commentId: str, userId: str = None, blogId: str = None, wikiId: str = None):
        data = {
            "value": 4,
            "timestamp": int(timestamp() * 1000)
        }
        if userId:
            data["eventSource"] = "UserProfileView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/user-profile/{userId}/comment/{commentId}/g-vote?cv=1.2&value=1", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        elif blogId:
            data["eventSource"] = "PostDetailView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/blog/{blogId}/comment/{commentId}/g-vote?cv=1.2&value=1", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        elif wikiId:
            data["eventSource"] = "PostDetailView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/item/{wikiId}/comment/{commentId}/g-vote?cv=1.2&value=1", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        else: raise exceptions.SpecifyType
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def unlike_comment(self, commentId: str, userId: str = None, blogId: str = None, wikiId: str = None):
        if userId: response = requests.delete(f"{self.api}/g/s/user-profile/{userId}/comment/{commentId}/g-vote?eventSource=UserProfileView", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        elif blogId: response = requests.delete(f"{self.api}/g/s/blog/{blogId}/comment/{commentId}/g-vote?eventSource=PostDetailView", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        elif wikiId: response = requests.delete(f"{self.api}/g/s/item/{wikiId}/comment/{commentId}/g-vote?eventSource=PostDetailView", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        else: raise exceptions.SpecifyType
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def get_membership_info(self):
        response = requests.get(f"{self.api}/g/s/membership?force=true", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.Membership(json.loads(response.text)).Membership

    def get_ta_announcements(self, language: str = "en", start: int = 0, size: int = 25):
        if language not in self.get_supported_languages(): raise exceptions.UnsupportedLanguage
        response = requests.get(f"{self.api}/g/s/announcement?language={language}&start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.BlogList(json.loads(response.text)["blogList"]).BlogList

    def get_wallet_info(self):
        response = requests.get(f"{self.api}/g/s/wallet", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.WalletInfo(json.loads(response.text)["wallet"]).WalletInfo

    def get_wallet_history(self, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/wallet/coin/history?start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.WalletHistory(json.loads(response.text)["coinHistoryList"]).WalletHistory

    def get_from_deviceid(self, deviceId: str):
        response = requests.get(f"{self.api}/g/s/auid?deviceId={deviceId}")
        if response.status_code != 200: return json.loads(response.text)
        else: return json.loads(response.text)["auid"]

    def get_from_code(self, code: str):
        response = requests.get(f"{self.api}/g/s/link-resolution?q={code}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.FromCode(json.loads(response.text)["linkInfoV2"]).FromCode

    def get_from_id(self, objectId: str, objectType: int, comId: str = None):
        data = json.dumps({
            "objectId": objectId,
            "targetCode": 1,
            "objectType": objectType,
            "timestamp": int(timestamp() * 1000)
        })
        if comId: response = requests.post(f"{self.api}/g/s-x{comId}/link-resolution", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        else: response = requests.post(f"{self.api}/g/s/link-resolution", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.FromCode(json.loads(response.text)["linkInfoV2"]).FromCode

    def get_supported_languages(self):
        response = requests.get(f"{self.api}/g/s/community-collection/supported-languages?start=0&size=100", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return json.loads(response.text)["supportedLanguages"]

    def claim_new_user_coupon(self):
        response = requests.post(f"{self.api}/g/s/coupon/new-user-coupon/claim", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def get_subscriptions(self, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/store/subscription?objectType=122&start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return json.loads(response.text)["storeSubscriptionItemList"]

    def get_all_users(self, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/user-profile?type=recent&start={start}&size={size}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.UserProfileCountList(json.loads(response.text)).UserProfileCountList

    def accept_host(self, chatId: str):
        data = json.dumps({"timestamp": int(timestamp() * 1000)})

        response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/accept-organizer", headers=headers.Headers(data=data).headers, data=data, proxies=self.proxies, verify=self.certificatePath)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def accept_organizer(self, chatId: str):
        self.accept_host(chatId)

    def link_identify(self, code: str):
        response = requests.get(f"{self.api}/g/s/community/link-identify?q=http%3A%2F%2Faminoapps.com%2Finvite%2F{code}", headers=headers.Headers().headers, proxies=self.proxies, verify=self.certificatePath)
        return json.loads(response.text)
