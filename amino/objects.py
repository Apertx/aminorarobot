class UserProfile:
    def __init__(self, data):
        self.json = data

        try: self.fanClub: FanClubList = FanClubList(data["fanClubList"]).FanClubList
        except: self.fanClub: FanClubList = FanClubList([])

        self.accountMembershipStatus = None
        self.activation = None
        self.activePublicLiveThreadId = None
        self.age = None
        self.aminoId = None
        self.aminoIdEditable = None
        self.appleId = None
        self.avatarFrame = None
        self.avatarFrameId = None
        self.backgroundImage = None
        self.backgroundColor = None
        self.blogsCount = None
        self.commentsCount = None
        self.content = None
        self.coverAnimation = None
        self.createdTime = None
        self.customTitles = None
        self.dateOfBirth = None
        self.defaultBubbleId = None
        self.disabledLevel = None
        self.disabledStatus = None
        self.disabledTime = None
        self.email = None
        self.extensions = None
        self.facebookId = None
        self.fansCount = None
        self.followersCount = None
        self.followingCount = None
        self.followingStatus = None
        self.gender = None
        self.globalStrikeCount = None
        self.googleId = None
        self.icon = None
        self.influencerCreatedTime = None
        self.influencerInfo = None
        self.influencerMonthlyFee = None
        self.influencerPinned = None
        self.isGlobal = None
        self.isMemberOfTeamAmino = None
        self.isNicknameVerified = None
        self.itemsCount = None
        self.lastStrikeTime = None
        self.lastWarningTime = None
        self.level = None
        self.mediaList = None
        self.membershipStatus = None
        self.modifiedTime = None
        self.mood = None
        self.moodSticker = None
        self.nickname = None
        self.notificationSubscriptionStatus = None
        self.onlineStatus = None
        self.onlineStatus2 = None
        self.phoneNumber = None
        self.postsCount = None
        self.privilegeOfChatInviteRequest = None
        self.privilegeOfCommentOnUserProfile = None
        self.pushEnabled = None
        self.race = None
        self.reputation = None
        self.role = None
        self.securityLevel = None
        self.staffInfo = None
        self.status = None
        self.storiesCount = None
        self.strikeCount = None
        self.tagList = None
        self.twitterId = None
        self.userId = None
        self.verified = None
        self.visitPrivacy = None
        self.visitorsCount = None
        self.warningCount = None
        self.totalQuizHighestScore = None
        self.totalQuizPlayedTimes = None
        self.requestId = None
        self.message = None
        self.applicant = None
        self.avgDailySpendTimeIn7Days = None
        self.adminLogCountIn7Days = None

    @property
    def UserProfile(self):
        try: self.accountMembershipStatus = self.json["accountMembershipStatus"]
        except: pass
        try: self.activation = self.json["activation"]
        except: pass
        try: self.activePublicLiveThreadId = self.json["activePublicLiveThreadId"]
        except: pass
        try: self.age = self.json["age"]
        except: pass
        try: self.aminoId = self.json["aminoId"]
        except: pass
        try: self.aminoIdEditable = self.json["aminoIdEditable"]
        except: pass
        try: self.appleId = self.json["appleID"]
        except: pass
        try: self.avatarFrame = self.json["avatarFrame"]
        except: pass
        try: self.avatarFrameId = self.json["avatarFrameId"]
        except: pass
        try: self.backgroundColor = self.json["extensions"]["style"]["backgroundColor"]
        except: pass
        try: self.backgroundImage = self.json["extensions"]["style"]["backgroundMediaList"][1]
        except: pass
        try: self.blogsCount = self.json["blogsCount"]
        except: pass
        try: self.commentsCount = self.json["commentsCount"]
        except: pass
        try: self.content = self.json["content"]
        except: pass
        try: self.coverAnimation = self.json["extensions"]["coverAnimation"]
        except: pass
        try: self.createdTime = self.json["createdTime"]
        except: pass
        try: self.customTitles = self.json["extensions"]["customTitles"]
        except: pass
        try: self.dateOfBirth = self.json["dateOfBirth"]
        except: pass
        try: self.defaultBubbleId = self.json["extensions"]["defaultBubbleId"]
        except: pass
        try: self.disabledLevel = self.json["extensions"]["__disabledLevel__"]
        except: pass
        try: self.disabledStatus = self.json["extensions"]["__disabledStatus__"]
        except: pass
        try: self.disabledTime = self.json["extensions"]["__disabledTime__"]
        except: pass
        try: self.email = self.json["email"]
        except: pass
        try: self.extensions = self.json["extensions"]
        except: pass
        try: self.facebookId = self.json["facebookID"]
        except: pass
        try: self.fansCount = self.json["influencerInfo"]["fansCount"]
        except: pass
        try: self.followersCount = self.json["membersCount"]
        except: pass
        try: self.followingCount = self.json["joinedCount"]
        except: pass
        try: self.followingStatus = self.json["followingStatus"]
        except: pass
        try: self.gender = self.json["gender"]
        except: pass
        try: self.globalStrikeCount = self.json["adminInfo"]["globalStrikeCount"]
        except: pass
        try: self.googleId = self.json["googleID"]
        except: pass
        try: self.icon = self.json["icon"]
        except: pass
        try: self.influencerCreatedTime = self.json["influencerInfo"]["createdTime"]
        except: pass
        try: self.influencerInfo = self.json["influencerInfo"]
        except: pass
        try: self.influencerMonthlyFee = self.json["influencerInfo"]["monthlyFee"]
        except: pass
        try: self.influencerPinned = self.json["influencerInfo"]["pinned"]
        except: pass
        try: self.isGlobal = self.json["isGlobal"]
        except: pass
        try: self.isMemberOfTeamAmino = self.json["extensions"]["isMemberOfTeamAmino"]
        except: pass
        try: self.isNicknameVerified = self.json["isNicknameVerified"]
        except: pass
        try: self.itemsCount = self.json["itemsCount"]
        except: pass
        try: self.lastStrikeTime = self.json["adminInfo"]["lastStrikeTime"]
        except: pass
        try: self.lastWarningTime = self.json["adminInfo"]["lastWarningTime"]
        except: pass
        try: self.level = self.json["level"]
        except: pass
        try: self.mediaList = self.json["mediaList"]
        except: pass
        try: self.membershipStatus = self.json["membershipStatus"]
        except: pass
        try: self.modifiedTime = self.json["modifiedTime"]
        except: pass
        try: self.mood = self.json["mood"]
        except: pass
        try: self.moodSticker = self.json["moodSticker"]
        except: pass
        try: self.nickname = self.json["nickname"]
        except: pass
        try: self.notificationSubscriptionStatus = self.json["notificationSubscriptionStatus"]
        except: pass
        try: self.onlineStatus = self.json["onlineStatus"]
        except: pass
        try: self.onlineStatus2 = self.json["settings"]["onlineStatus"]
        except: pass
        try: self.phoneNumber = self.json["phoneNumber"]
        except: pass
        try: self.postsCount = self.json["postsCount"]
        except: pass
        try: self.privilegeOfChatInviteRequest = self.json["extensions"]["privilegeOfChatInviteRequest"]
        except: pass
        try: self.privilegeOfCommentOnUserProfile = self.json["extensions"]["privilegeOfCommentOnUserProfile"]
        except: pass
        try: self.pushEnabled = self.json["pushEnabled"]
        except: pass
        try: self.race = self.json["race"]
        except: pass
        try: self.reputation = self.json["reputation"]
        except: pass
        try: self.role = self.json["role"]
        except: pass
        try: self.securityLevel = self.json["securityLevel"]
        except: pass
        try: self.staffInfo = self.json["adminInfo"]
        except: pass
        try: self.status = self.json["status"]
        except: pass
        try: self.storiesCount = self.json["storiesCount"]
        except: pass
        try: self.strikeCount = self.json["adminInfo"]["strikeCount"]
        except: pass
        try: self.tagList = self.json["tagList"]
        except: pass
        try: self.twitterId = self.json["twitterID"]
        except: pass
        try: self.userId = self.json["uid"]
        except: pass
        try: self.verified = self.json["verified"]
        except: pass
        try: self.visitPrivacy = self.json["visitPrivacy"]
        except: pass
        try: self.visitorsCount = self.json["visitorsCount"]
        except: pass
        try: self.warningCount = self.json["adminInfo"]["warningCount"]
        except: pass
        try: self.totalQuizHighestScore = self.json["totalQuizHighestScore"]
        except: pass
        try: self.totalQuizPlayedTimes = self.json["totalQuizPlayedTimes"]
        except: pass
        try: self.requestId = self.json["requestId"]
        except: pass
        try: self.message = self.json["message"]
        except: pass
        try: self.applicant = self.json["applicant"]
        except: pass
        try: self.avgDailySpendTimeIn7Days = self.json["avgDailySpendTimeIn7Days"]
        except: pass
        try: self.adminLogCountIn7Days = self.json["adminLogCountIn7Days"]
        except: pass

        return self

class UserProfileList:
    def __init__(self, data):
        _fanClub = []

        self.json = data

        for y in data:
            try: _fanClub.append(FanClubList(y["fanClubList"]).FanClubList)
            except: _fanClub.append(None)

        self.accountMembershipStatus = []
        self.activation = []
        self.activePublicLiveThreadId = []
        self.age = []
        self.aminoId = []
        self.aminoIdEditable = []
        self.appleId = []
        self.avatarFrame = []
        self.avatarFrameId = []
        self.backgroundColor = []
        self.backgroundImage = []
        self.blogsCount = []
        self.commentsCount = []
        self.content = []
        self.coverAnimation = []
        self.createdTime = []
        self.customTitles = []
        self.dateOfBirth = []
        self.defaultBubbleId = []
        self.disabledLevel = []
        self.disabledStatus = []
        self.disabledTime = []
        self.email = []
        self.extensions = []
        self.facebookId = []
        self.fansCount = []
        self.fanClub = _fanClub
        self.followersCount = []
        self.followingCount = []
        self.followingStatus = []
        self.gender = []
        self.globalStrikeCount = []
        self.googleId = []
        self.icon = []
        self.influencerCreatedTime = []
        self.influencerInfo = []
        self.influencerMonthlyFee = []
        self.influencerPinned = []
        self.isGlobal = []
        self.isMemberOfTeamAmino = []
        self.isNicknameVerified = []
        self.itemsCount = []
        self.lastStrikeTime = []
        self.lastWarningTime = []
        self.level = []
        self.mediaList = []
        self.membershipStatus = []
        self.modifiedTime = []
        self.mood = []
        self.moodSticker = []
        self.nickname = []
        self.notificationSubscriptionStatus = []
        self.onlineStatus = []
        self.onlineStatus2 = []
        self.phoneNumber = []
        self.postsCount = []
        self.privilegeOfChatInviteRequest = []
        self.privilegeOfCommentOnUserProfile = []
        self.pushEnabled = []
        self.race = []
        self.reputation = []
        self.role = []
        self.securityLevel = []
        self.staffInfo = []
        self.status = []
        self.storiesCount = []
        self.strikeCount = []
        self.tagList = []
        self.twitterId = []
        self.userId = []
        self.verified = []
        self.visitPrivacy = []
        self.visitorsCount = []
        self.warningCount = []
        self.totalQuizPlayedTimes = []
        self.totalQuizHighestScore = []
        self.requestId = []
        self.message = []
        self.applicant = []
        self.avgDailySpendTimeIn7Days = []
        self.adminLogCountIn7Days = []

    @property
    def UserProfileList(self):
        for x in self.json:
            try: self.accountMembershipStatus.append(x["accountMembershipStatus"])
            except: self.accountMembershipStatus.append(None)
            try: self.activation.append(x["activation"])
            except: self.activation.append(None)
            try: self.activePublicLiveThreadId.append(x["activePublicLiveThreadId"])
            except: self.activePublicLiveThreadId.append(None)
            try: self.age.append(x["age"])
            except: self.age.append(None)
            try: self.aminoId.append(x["aminoId"])
            except: self.aminoId.append(None)
            try: self.aminoIdEditable.append(x["aminoIdEditable"])
            except: self.aminoIdEditable.append(None)
            try: self.appleId.append(x["appleID"])
            except: self.appleId.append(None)
            try: self.avatarFrame.append(x["avatarFrame"])
            except: self.avatarFrame.append(None)
            try: self.avatarFrameId.append(x["avatarFrameId"])
            except: self.avatarFrameId.append(None)
            try: self.backgroundColor.append(x["extensions"]["style"]["backgroundColor"])
            except: self.backgroundColor.append(None)
            try: self.backgroundImage.append(x["extensions"]["style"]["backgroundMediaList"][1])
            except: self.backgroundImage.append(None)
            try: self.blogsCount.append(x["blogsCount"])
            except: self.blogsCount.append(None)
            try: self.commentsCount.append(x["commentsCount"])
            except: self.commentsCount.append(None)
            try: self.content.append(x["content"])
            except: self.content.append(None)
            try: self.coverAnimation.append(x["extensions"]["coverAnimation"])
            except: self.coverAnimation.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.customTitles.append(x["extensions"]["customTitles"])
            except: self.customTitles.append(None)
            try: self.dateOfBirth.append(x["dateOfBirth"])
            except: self.dateOfBirth.append(None)
            try: self.defaultBubbleId.append(x["extensions"]["defaultBubbleId"])
            except: self.defaultBubbleId.append(None)
            try: self.disabledLevel.append(x["extensions"]["__disabledLevel__"])
            except: self.disabledLevel.append(None)
            try: self.disabledStatus.append(x["extensions"]["__disabledStatus__"])
            except: self.disabledStatus.append(None)
            try: self.disabledTime.append(x["extensions"]["__disabledTime__"])
            except: self.disabledTime.append(None)
            try: self.email.append(x["email"])
            except: self.email.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.facebookId.append(x["facebookID"])
            except: self.facebookId.append(None)
            try: self.fansCount.append(x["influencerInfo"]["fansCount"])
            except: self.fansCount.append(None)
            try: self.followersCount.append(x["membersCount"])
            except: self.followersCount.append(None)
            try: self.followingCount.append(x["joinedCount"])
            except: self.followingCount.append(None)
            try: self.followingStatus.append(x["followingStatus"])
            except: self.followingStatus.append(None)
            try: self.gender.append(x["gender"])
            except: self.gender.append(None)
            try: self.globalStrikeCount.append(x["adminInfo"]["globalStrikeCount"])
            except: self.globalStrikeCount.append(None)
            try: self.googleId.append(x["googleID"])
            except: self.googleId.append(None)
            try: self.icon.append(x["icon"])
            except: self.icon.append(None)
            try: self.influencerCreatedTime.append(x["influencerInfo"]["createdTime"])
            except: self.influencerCreatedTime.append(None)
            try: self.influencerInfo.append(x["influencerInfo"])
            except: self.influencerInfo.append(None)
            try: self.influencerMonthlyFee.append(x["influencerInfo"]["monthlyFee"])
            except: self.influencerMonthlyFee.append(None)
            try: self.influencerPinned.append(x["influencerInfo"]["pinned"])
            except: self.influencerPinned.append(None)
            try: self.isGlobal.append(x["isGlobal"])
            except: self.isGlobal.append(None)
            try: self.isMemberOfTeamAmino.append(x["extensions"]["isMemberOfTeamAmino"])
            except: self.isMemberOfTeamAmino.append(None)
            try: self.isNicknameVerified.append(x["isNicknameVerified"])
            except: self.isNicknameVerified.append(None)
            try: self.itemsCount.append(x["itemsCount"])
            except: self.itemsCount.append(None)
            try: self.lastStrikeTime.append(x["adminInfo"]["lastStrikeTime"])
            except: self.lastStrikeTime.append(None)
            try: self.lastWarningTime.append(x["adminInfo"]["lastWarningTime"])
            except: self.lastWarningTime.append(None)
            try: self.level.append(x["level"])
            except: self.level.append(None)
            try: self.mediaList.append(x["mediaList"])
            except: self.mediaList.append(None)
            try: self.membershipStatus.append(x["membershipStatus"])
            except: self.membershipStatus.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except: self.modifiedTime.append(None)
            try: self.mood.append(x["mood"])
            except: self.mood.append(None)
            try: self.moodSticker.append(x["moodSticker"])
            except: self.moodSticker.append(None)
            try: self.nickname.append(x["nickname"])
            except: self.nickname.append(None)
            try: self.notificationSubscriptionStatus.append(x["notificationSubscriptionStatus"])
            except: self.notificationSubscriptionStatus.append(None)
            try: self.onlineStatus.append(x["onlineStatus"])
            except: self.onlineStatus.append(None)
            try: self.onlineStatus2.append(x["settings"]["onlineStatus"])
            except: self.onlineStatus2.append(None)
            try: self.phoneNumber.append(x["phoneNumber"])
            except: self.phoneNumber.append(None)
            try: self.postsCount.append(x["postsCount"])
            except: self.postsCount.append(None)
            try: self.privilegeOfChatInviteRequest.append(x["extensions"]["privilegeOfChatInviteRequest"])
            except: self.privilegeOfChatInviteRequest.append(None)
            try: self.privilegeOfCommentOnUserProfile.append(x["extensions"]["privilegeOfCommentOnUserProfile"])
            except: self.privilegeOfCommentOnUserProfile.append(None)
            try: self.pushEnabled.append(x["pushEnabled"])
            except: self.pushEnabled.append(None)
            try: self.race.append(x["race"])
            except: self.race.append(None)
            try: self.reputation.append(x["reputation"])
            except: self.reputation.append(None)
            try: self.role.append(x["role"])
            except: self.role.append(None)
            try: self.securityLevel.append(x["securityLevel"])
            except: self.securityLevel.append(None)
            try: self.staffInfo.append(x["adminInfo"])
            except: self.staffInfo.append(None)
            try: self.status.append(x["status"])
            except: self.status.append(None)
            try: self.storiesCount.append(x["storiesCount"])
            except: self.storiesCount.append(None)
            try: self.strikeCount.append(x["adminInfo"]["strikeCount"])
            except: self.strikeCount.append(None)
            try: self.tagList.append(x["tagList"])
            except: self.tagList.append(None)
            try: self.twitterId.append(x["twitterID"])
            except: self.twitterId.append(None)
            try: self.userId.append(x["uid"])
            except: self.userId.append(None)
            try: self.verified.append(x["verified"])
            except: self.verified.append(None)
            try: self.visitPrivacy.append(x["visitPrivacy"])
            except: self.visitPrivacy.append(None)
            try: self.visitorsCount.append(x["visitorsCount"])
            except: self.visitorsCount.append(None)
            try: self.warningCount.append(x["adminInfo"]["warningCount"])
            except: self.warningCount.append(None)
            try: self.totalQuizPlayedTimes.append(x["totalQuizPlayedTimes"])
            except: self.totalQuizPlayedTimes.append(None)
            try: self.totalQuizHighestScore.append(x["totalQuizHighestScore"])
            except: self.totalQuizHighestScore.append(None)
            try: self.requestId.append(x["requestId"])
            except: self.requestId.append(None)
            try: self.message.append(x["message"])
            except: self.message.append(None)
            try: self.applicant.append(x["applicant"])
            except: self.applicant.append(None)
            try: self.avgDailySpendTimeIn7Days.append(x["avgDailySpendTimeIn7Days"])
            except: self.avgDailySpendTimeIn7Days.append(None)
            try: self.adminLogCountIn7Days.append(x["adminLogCountIn7Days"])
            except: self.adminLogCountIn7Days.append(None)

        return self

class BlogList:
    def __init__(self, data, nextPageToken = None, prevPageToken = None):
        _author, _quizQuestionList = [], []

        self.json = data
        self.nextPageToken = nextPageToken
        self.prevPageToken = prevPageToken

        for y in data:
            try: _author.append(y["author"])
            except: _author.append(None)
            try: _quizQuestionList.append(QuizQuestionList(y["quizQuestionList"]).QuizQuestionList)
            except: _quizQuestionList.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.quizQuestionList = _quizQuestionList

        self.createdTime = []
        self.globalVotesCount = []
        self.globalVotedValue = []
        self.keywords = []
        self.mediaList = []
        self.style = []
        self.totalQuizPlayCount = []
        self.title = []
        self.tipInfo = []
        self.tippersCount = []
        self.tippable = []
        self.tippedCoins = []
        self.contentRating = []
        self.needHidden = []
        self.guestVotesCount = []
        self.type = []
        self.status = []
        self.globalCommentsCount = []
        self.modifiedTime = []
        self.widgetDisplayInterval = []
        self.totalPollVoteCount = []
        self.blogId = []
        self.viewCount = []
        self.fansOnly = []
        self.backgroundColor = []
        self.votesCount = []
        self.endTime = []
        self.refObjectId = []
        self.refObject = []
        self.votedValue = []
        self.extensions = []
        self.commentsCount = []
        self.content = []
        self.featuredType = []
        self.shareUrl = []
        self.disabledTime = []
        self.quizPlayedTimes = []
        self.quizTotalQuestionCount = []
        self.quizTrendingTimes = []
        self.quizLastAddQuestionTime = []

    @property
    def BlogList(self):
        for x in self.json:
            try: self.globalVotesCount.append(x["globalVotesCount"])
            except: self.globalVotesCount.append(None)
            try: self.globalVotedValue.append(x["globalVotedValue"])
            except: self.globalVotedValue.append(None)
            try: self.keywords.append(x["keywords"])
            except: self.keywords.append(None)
            try: self.mediaList.append(x["mediaList"])
            except: self.mediaList.append(None)
            try: self.style.append(x["style"])
            except: self.style.append(None)
            try: self.totalQuizPlayCount.append(x["totalQuizPlayCount"])
            except: self.totalQuizPlayCount.append(None)
            try: self.title.append(x["title"])
            except: self.title.append(None)
            try: self.tipInfo.append(x["tipInfo"])
            except: self.tipInfo.append(None)
            try: self.tippersCount.append(x["tipInfo"]["tippersCount"])
            except: self.tippersCount.append(None)
            try: self.tippable.append(x["tipInfo"]["tippable"])
            except: self.tippable.append(None)
            try: self.tippedCoins.append(x["tipInfo"]["tippedCoins"])
            except: self.tippedCoins.append(None)
            try: self.contentRating.append(x["contentRating"])
            except: self.contentRating.append(None)
            try: self.needHidden.append(x["needHidden"])
            except: self.needHidden.append(None)
            try: self.guestVotesCount.append(x["guestVotesCount"])
            except: self.guestVotesCount.append(None)
            try: self.type.append(x["type"])
            except: self.type.append(None)
            try: self.status.append(x["status"])
            except: self.status.append(None)
            try: self.globalCommentsCount.append(x["globalCommentsCount"])
            except: self.globalCommentsCount.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except: self.modifiedTime.append(None)
            try: self.widgetDisplayInterval.append(x["widgetDisplayInterval"])
            except: self.widgetDisplayInterval.append(None)
            try: self.totalPollVoteCount.append(x["totalPollVoteCount"])
            except: self.totalPollVoteCount.append(None)
            try: self.blogId.append(x["blogId"])
            except: self.blogId.append(None)
            try: self.viewCount.append(x["viewCount"])
            except: self.viewCount.append(None)
            try: self.fansOnly.append(x["extensions"]["fansOnly"])
            except: self.fansOnly.append(None)
            try: self.backgroundColor.append(x["extensions"]["style"]["backgroundColor"])
            except: self.backgroundColor.append(None)
            try: self.votesCount.append(x["votesCount"])
            except: self.votesCount.append(None)
            try: self.endTime.append(x["endTime"])
            except: self.endTime.append(None)
            try: self.refObjectId.append(x["refObjectId"])
            except: self.refObjectId.append(None)
            try: self.refObject.append(x["refObject"])
            except: self.refObject.append(None)
            try: self.votedValue.append(x["votedValue"])
            except: self.votedValue.append(None)
            try: self.content.append(x["content"])
            except: self.content.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.shareUrl.append(x["shareURLFullPath"])
            except: self.shareUrl.append(None)
            try: self.commentsCount.append(x["commentsCount"])
            except: self.commentsCount.append(None)
            try: self.featuredType.append(x["extensions"]["featuredType"])
            except: self.featuredType.append(None)
            try: self.disabledTime.append(x["extensions"]["__disabledTime__"])
            except: self.disabledTime.append(None)
            try: self.quizPlayedTimes.append(x["extensions"]["quizPlayedTimes"])
            except: self.quizPlayedTimes.append(None)
            try: self.quizTotalQuestionCount.append(x["extensions"]["quizTotalQuestionCount"])
            except: self.quizTotalQuestionCount.append(None)
            try: self.quizTrendingTimes.append(x["extensions"]["quizTrendingTimes"])
            except: self.quizTrendingTimes.append(None)
            try: self.quizLastAddQuestionTime.append(x["extensions"]["quizLastAddQuestionTime"])
            except: self.quizLastAddQuestionTime.append(None)

        return self

class RecentBlogs:
    def __init__(self, data):
        self.json = data

        self.nextPageToken = None
        self.prevPageToken = None

    @property
    def RecentBlogs(self):
        try: self.nextPageToken = self.json["paging"]["nextPageToken"]
        except: pass
        try: self.prevPageToken = self.json["paging"]["prevPageToken"]
        except: pass

        return BlogList(self.json["blogList"], self.nextPageToken, self.prevPageToken).BlogList

class BlogCategoryList:
    def __init__(self, data):
        self.json = data
        self.status = []
        self.modifiedTime = []
        self.icon = []
        self.style = []
        self.title = []
        self.content = []
        self.createdTime = []
        self.position = []
        self.type = []
        self.categoryId = []
        self.blogsCount = []

    @property
    def BlogCategoryList(self):
        for x in self.json:
            try: self.status.append(x["status"])
            except: self.status.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except: self.modifiedTime.append(None)
            try: self.icon.append(x["icon"])
            except: self.icon.append(None)
            try: self.style.append(x["style"])
            except: self.style.append(None)
            try: self.title.append(x["label"])
            except: self.title.append(None)
            try: self.content.append(x["content"])
            except: self.content.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.position.append(x["position"])
            except: self.position.append(None)
            try: self.type.append(x["type"])
            except: self.type.append(None)
            try: self.categoryId.append(x["categoryId"])
            except: self.categoryId.append(None)
            try: self.blogsCount.append(x["blogsCount"])
            except: self.blogsCount.append(None)

        return self

class Blog:
    def __init__(self, data):
        self.json = data

        try: self.author: UserProfile = UserProfile(data["author"]).UserProfile
        except: self.author: UserProfile = UserProfile([])
        try: self.quizQuestionList: QuizQuestionList = QuizQuestionList(data["quizQuestionList"]).QuizQuestionList
        except: self.quizQuestionList: QuizQuestionList = QuizQuestionList([])

        self.createdTime = None
        self.globalVotesCount = None
        self.globalVotedValue = None
        self.keywords = None
        self.mediaList = None
        self.style = None
        self.totalQuizPlayCount = None
        self.title = None
        self.tipInfo = None
        self.tippersCount = None
        self.tippable = None
        self.tippedCoins = None
        self.contentRating = None
        self.needHidden = None
        self.guestVotesCount = None
        self.type = None
        self.status = None
        self.globalCommentsCount = None
        self.modifiedTime = None
        self.widgetDisplayInterval = None
        self.totalPollVoteCount = None
        self.blogId = None
        self.comId = None
        self.viewCount = None
        self.fansOnly = None
        self.backgroundColor = None
        self.votesCount = None
        self.endTime = None
        self.refObjectId = None
        self.refObject = None
        self.votedValue = None
        self.extensions = None
        self.commentsCount = None
        self.content = None
        self.featuredType = None
        self.shareUrl = None
        self.disabledTime = None
        self.quizPlayedTimes = None
        self.quizTotalQuestionCount = None
        self.quizTrendingTimes = None
        self.quizLastAddQuestionTime = None

    @property
    def Blog(self):
        try: self.globalVotesCount = self.json["globalVotesCount"]
        except: pass
        try: self.globalVotedValue = self.json["globalVotedValue"]
        except: pass
        try: self.keywords = self.json["keywords"]
        except: pass
        try: self.mediaList = self.json["mediaList"]
        except: pass
        try: self.style = self.json["style"]
        except: pass
        try: self.totalQuizPlayCount = self.json["totalQuizPlayCount"]
        except: pass
        try: self.title = self.json["title"]
        except: pass
        try: self.tipInfo = self.json["tipInfo"]
        except: pass
        try: self.tippersCount = self.json["tipInfo"]["tippersCount"]
        except: pass
        try: self.tippable = self.json["tipInfo"]["tippable"]
        except: pass
        try: self.tippedCoins = self.json["tipInfo"]["tippedCoins"]
        except: pass
        try: self.contentRating = self.json["contentRating"]
        except: pass
        try: self.needHidden = self.json["needHidden"]
        except: pass
        try: self.guestVotesCount = self.json["guestVotesCount"]
        except: pass
        try: self.type = self.json["type"]
        except: pass
        try: self.status = self.json["status"]
        except: pass
        try: self.globalCommentsCount = self.json["globalCommentsCount"]
        except: pass
        try: self.modifiedTime = self.json["modifiedTime"]
        except: pass
        try: self.widgetDisplayInterval = self.json["widgetDisplayInterval"]
        except: pass
        try: self.totalPollVoteCount = self.json["totalPollVoteCount"]
        except: pass
        try: self.blogId = self.json["blogId"]
        except: pass
        try: self.comId = self.json["ndcId"]
        except: pass
        try: self.viewCount = self.json["viewCount"]
        except: pass
        try: self.shareUrl = self.json["shareURLFullPath"]
        except: pass
        try: self.fansOnly = self.json["extensions"]["fansOnly"]
        except: pass
        try: self.backgroundColor = self.json["extensions"]["style"]["backgroundColor"]
        except: pass
        try: self.votesCount = self.json["votesCount"]
        except: pass
        try: self.endTime = self.json["endTime"]
        except: pass
        try: self.refObjectId = self.json["refObjectId"]
        except: pass
        try: self.refObject = self.json["refObject"]
        except: pass
        try: self.votedValue = self.json["votedValue"]
        except: pass
        try: self.content = self.json["content"]
        except: pass
        try: self.createdTime = self.json["createdTime"]
        except: pass
        try: self.extensions = self.json["extensions"]
        except: pass
        try: self.commentsCount = self.json["commentsCount"]
        except: pass
        try: self.featuredType = self.json["extensions"]["featuredType"]
        except: pass
        try: self.disabledTime = self.json["extensions"]["__disabledTime__"]
        except: pass
        try: self.quizPlayedTimes = self.json["extensions"]["quizPlayedTimes"]
        except: pass
        try: self.quizTotalQuestionCount = self.json["extensions"]["quizTotalQuestionCount"]
        except: pass
        try: self.quizTrendingTimes = self.json["extensions"]["quizTrendingTimes"]
        except: pass
        try: self.quizLastAddQuestionTime = self.json["extensions"]["quizLastAddQuestionTime"]
        except: pass

        return self

class Wiki:
    def __init__(self, data):
        self.json = data

        try: self.author: UserProfile = UserProfile(data["author"]).UserProfile
        except: self.author: UserProfile = UserProfile([])
        try: self.labels: WikiLabelList = WikiLabelList(data["extensions"]["props"]).WikiLabelList
        except: self.labels: WikiLabelList = WikiLabelList([])

        self.createdTime = None
        self.modifiedTime = None
        self.wikiId = None
        self.status = None
        self.style = None
        self.globalCommentsCount = None
        self.votedValue = None
        self.globalVotesCount = None
        self.globalVotedValue = None
        self.contentRating = None
        self.title = None
        self.content = None
        self.keywords = None
        self.needHidden = None
        self.guestVotesCount = None
        self.extensions = None
        self.backgroundColor = None
        self.fansOnly = None
        self.knowledgeBase = None
        self.originalWikiId = None
        self.version = None
        self.contributors = None
        self.votesCount = None
        self.comId = None
        self.createdTime = None
        self.mediaList = None
        self.commentsCount = None

    @property
    def Wiki(self):
        try: self.wikiId = self.json["itemId"]
        except: pass
        try: self.status = self.json["status"]
        except: pass
        try: self.style = self.json["style"]
        except: pass
        try: self.globalCommentsCount = self.json["globalCommentsCount"]
        except: pass
        try: self.modifiedTime = self.json["modifiedTime"]
        except: pass
        try: self.votedValue = self.json["votedValue"]
        except: pass
        try: self.globalVotesCount = self.json["globalVotesCount"]
        except: pass
        try: self.globalVotedValue = self.json["globalVotedValue"]
        except: pass
        try: self.contentRating = self.json["contentRating"]
        except: pass
        try: self.contentRating = self.json["contentRating"]
        except: pass
        try: self.title = self.json["label"]
        except: pass
        try: self.content = self.json["content"]
        except: pass
        try: self.keywords = self.json["keywords"]
        except: pass
        try: self.needHidden = self.json["needHidden"]
        except: pass
        try: self.guestVotesCount = self.json["guestVotesCount"]
        except: pass
        try: self.extensions = self.json["extensions"]
        except: pass
        try: self.votesCount = self.json["votesCount"]
        except: pass
        try: self.comId = self.json["ndcId"]
        except: pass
        try: self.createdTime = self.json["createdTime"]
        except: pass
        try: self.mediaList = self.json["mediaList"]
        except: pass
        try: self.commentsCount = self.json["commentsCount"]
        except: pass
        try: self.backgroundColor = self.json["extensions"]["style"]["backgroundColor"]
        except: pass
        try: self.fansOnly = self.json["extensions"]["fansOnly"]
        except: pass
        try: self.knowledgeBase = self.json["extensions"]["knowledgeBase"]
        except: pass
        try: self.version = self.json["extensions"]["knowledgeBase"]["version"]
        except: pass
        try: self.originalWikiId = self.json["extensions"]["knowledgeBase"]["originalItemId"]
        except: pass
        try: self.contributors = self.json["extensions"]["knowledgeBase"]["contributors"]
        except: pass

        return self

class WikiList:
    def __init__(self, data):
        _author, _labels = [], []

        self.json = data

        for y in data:
            try: _author.append(y["author"])
            except: _author.append(None)
            try: _labels.append(WikiLabelList(y["extensions"]["props"]).WikiLabelList)
            except: _labels.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.labels = _labels
        self.createdTime = []
        self.modifiedTime = []
        self.wikiId = []
        self.status = []
        self.style = []
        self.globalCommentsCount = []
        self.votedValue = []
        self.globalVotesCount = []
        self.globalVotedValue = []
        self.contentRating = []
        self.title = []
        self.content = []
        self.keywords = []
        self.needHidden = []
        self.guestVotesCount = []
        self.extensions = []
        self.backgroundColor = []
        self.fansOnly = []
        self.knowledgeBase = []
        self.originalWikiId = []
        self.version = []
        self.contributors = []
        self.votesCount = []
        self.comId = []
        self.createdTime = []
        self.mediaList = []
        self.commentsCount = []

    @property
    def WikiList(self):
        for x in self.json:
            try: self.wikiId.append(x["itemId"])
            except: self.wikiId.append(None)
            try: self.status.append(x["status"])
            except: self.status.append(None)
            try: self.style.append(x["style"])
            except: self.style.append(None)
            try: self.globalCommentsCount.append(x["globalCommentsCount"])
            except: self.globalCommentsCount.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except: self.modifiedTime.append(None)
            try: self.votedValue.append(x["votedValue"])
            except: self.votedValue.append(None)
            try: self.globalVotesCount.append(x["globalVotesCount"])
            except: self.globalVotesCount.append(None)
            try: self.globalVotedValue.append(x["globalVotedValue"])
            except: self.globalVotedValue.append(None)
            try: self.contentRating.append(x["contentRating"])
            except: self.contentRating.append(None)
            try: self.contentRating.append(x["contentRating"])
            except: self.contentRating.append(None)
            try: self.title.append(x["label"])
            except: self.title.append(None)
            try: self.content.append(x["content"])
            except: self.content.append(None)
            try: self.keywords.append(x["keywords"])
            except: self.keywords.append(None)
            try: self.needHidden.append(x["needHidden"])
            except: self.needHidden.append(None)
            try: self.guestVotesCount.append(x["guestVotesCount"])
            except: self.guestVotesCount.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.votesCount.append(x["votesCount"])
            except: self.votesCount.append(None)
            try: self.comId.append(x["ndcId"])
            except: self.comId.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.mediaList.append(x["mediaList"])
            except: self.mediaList.append(None)
            try: self.commentsCount.append(x["commentsCount"])
            except: self.commentsCount.append(None)
            try: self.backgroundColor.append(x["extensions"]["style"]["backgroundColor"])
            except: self.backgroundColor.append(None)
            try: self.fansOnly.append(x["extensions"]["fansOnly"])
            except: self.fansOnly.append(None)
            try: self.knowledgeBase.append(x["extensions"]["knowledgeBase"])
            except: self.knowledgeBase.append(None)
            try: self.version.append(x["extensions"]["knowledgeBase"]["version"])
            except: self.version.append(None)
            try: self.originalWikiId.append(x["extensions"]["knowledgeBase"]["originalItemId"])
            except: self.originalWikiId.append(None)
            try: self.contributors.append(x["extensions"]["knowledgeBase"]["contributors"])
            except: self.contributors.append(None)

        return self


class WikiLabelList:
    def __init__(self, data):
        self.json = data
        self.title = []
        self.content = []
        self.type = []

    @property
    def WikiLabelList(self):
        for x in self.json:
            try: self.title.append(x["title"])
            except: self.title.append(None)
            try: self.content.append(x["value"])
            except: self.content.append(None)
            try: self.type.append(x["type"])
            except: self.type.append(None)

        return self

class RankingTableList:
    def __init__(self, data):
        self.json = data
        self.title = []
        self.level = []
        self.reputation = []
        self.id = []

    @property
    def RankingTableList(self):
        for x in self.json:
            try: self.title.append(x["title"])
            except: self.title.append(None)
            try: self.level.append(x["level"])
            except: self.level.append(None)
            try: self.reputation.append(x["reputation"])
            except: self.reputation.append(None)
            try: self.id.append(x["id"])
            except: self.id.append(None)

        return self

class Community:
    def __init__(self, data):
        self.json = data

        try: self.agent: UserProfile = UserProfile(data["agent"]).UserProfile
        except: self.agent: UserProfile = UserProfile([])
        try: self.rankingTable: RankingTableList = RankingTableList(data["advancedSettings"]["rankingTable"]).RankingTableList
        except: self.rankingTable: RankingTableList = RankingTableList([])

        self.usersCount = None
        self.createdTime = None
        self.aminoId = None
        self.icon = None
        self.link = None
        self.comId = None
        self.modifiedTime = None
        self.status = None
        self.joinType = None
        self.tagline = None
        self.primaryLanguage = None
        self.heat = None
        self.themePack = None
        self.probationStatus = None
        self.listedStatus = None
        self.userAddedTopicList = None
        self.name = None
        self.isStandaloneAppDeprecated = None
        self.searchable = None
        self.influencerList = None
        self.keywords = None
        self.mediaList = None
        self.description = None
        self.isStandaloneAppMonetizationEnabled = None
        self.advancedSettings = None
        self.activeInfo = None
        self.configuration = None
        self.extensions = None
        self.nameAliases = None
        self.templateId = None
        self.promotionalMediaList = None
        self.defaultRankingTypeInLeaderboard = None
        self.joinedBaselineCollectionIdList = None
        self.newsfeedPages = None
        self.catalogEnabled = None
        self.pollMinFullBarVoteCount = None
        self.leaderboardStyle = None
        self.facebookAppIdList = None
        self.welcomeMessage = None
        self.welcomeMessageEnabled = None
        self.hasPendingReviewRequest = None
        self.frontPageLayout = None
        self.themeColor = None
        self.themeHash = None
        self.themeVersion = None
        self.themeUrl = None
        self.themeHomePageAppearance = None
        self.themeLeftSidePanelTop = None
        self.themeLeftSidePanelBottom = None
        self.themeLeftSidePanelColor = None
        self.customList = None

    @property
    def Community(self):
        try: self.name = self.json["name"]
        except: pass
        try: self.usersCount = self.json["membersCount"]
        except: pass
        try: self.createdTime = self.json["createdTime"]
        except: pass
        try: self.aminoId = self.json["endpoint"]
        except: pass
        try: self.icon = self.json["icon"]
        except: pass
        try: self.link = self.json["link"]
        except: pass
        try: self.comId = self.json["ndcId"]
        except: pass
        try: self.modifiedTime = self.json["modifiedTime"]
        except: pass
        try: self.status = self.json["status"]
        except: pass
        try: self.joinType = self.json["joinType"]
        except: pass
        try: self.primaryLanguage = self.json["primaryLanguage"]
        except: pass
        try: self.heat = self.json["communityHeat"]
        except: pass
        try: self.userAddedTopicList = self.json["userAddedTopicList"]
        except: pass
        try: self.probationStatus = self.json["probationStatus"]
        except: pass
        try: self.listedStatus = self.json["listedStatus"]
        except: pass
        try: self.themePack = self.json["themePack"]
        except: pass
        try: self.themeColor = self.json["themePack"]["themeColor"]
        except: pass
        try: self.themeHash = self.json["themePack"]["themePackHash"]
        except: pass
        try: self.themeVersion = self.json["themePack"]["themePackRevision"]
        except: pass
        try: self.themeUrl = self.json["themePack"]["themePackUrl"]
        except: pass
        try: self.themeHomePageAppearance = self.json["configuration"]["appearance"]["homePage"]["navigation"]
        except: pass
        try: self.themeLeftSidePanelTop = self.json["configuration"]["appearance"]["leftSidePanel"]["navigation"]["level1"]
        except: pass
        try: self.themeLeftSidePanelBottom = self.json["configuration"]["appearance"]["leftSidePanel"]["navigation"]["level2"]
        except: pass
        try: self.themeLeftSidePanelColor = self.json["configuration"]["appearance"]["leftSidePanel"]["style"]["iconColor"]
        except: pass
        try: self.customList = self.json["configuration"]["page"]["customList"]
        except: pass
        try: self.tagline = self.json["tagline"]
        except: pass
        try: self.searchable = self.json["searchable"]
        except: pass
        try: self.isStandaloneAppDeprecated = self.json["isStandaloneAppDeprecated"]
        except: pass
        try: self.influencerList = self.json["influencerList"]
        except: pass
        try: self.keywords = self.json["keywords"]
        except: pass
        try: self.mediaList = self.json["mediaList"]
        except: pass
        try: self.description = self.json["content"]
        except: pass
        try: self.isStandaloneAppMonetizationEnabled = self.json["isStandaloneAppMonetizationEnabled"]
        except: pass
        try: self.advancedSettings = self.json["advancedSettings"]
        except: pass
        try: self.defaultRankingTypeInLeaderboard = self.json["advancedSettings"]["defaultRankingTypeInLeaderboard"]
        except: pass
        try: self.frontPageLayout = self.json["advancedSettings"]["frontPageLayout"]
        except: pass
        try: self.hasPendingReviewRequest = self.json["advancedSettings"]["hasPendingReviewRequest"]
        except: pass
        try: self.welcomeMessageEnabled = self.json["advancedSettings"]["welcomeMessageEnabled"]
        except: pass
        try: self.welcomeMessage = self.json["advancedSettings"]["welcomeMessageText"]
        except: pass
        try: self.pollMinFullBarVoteCount = self.json["advancedSettings"]["pollMinFullBarVoteCount"]
        except: pass
        try: self.catalogEnabled = self.json["advancedSettings"]["catalogEnabled"]
        except: pass
        try: self.leaderboardStyle = self.json["advancedSettings"]["leaderboardStyle"]
        except: pass
        try: self.facebookAppIdList = self.json["advancedSettings"]["facebookAppIdList"]
        except: pass
        try: self.newsfeedPages = self.json["advancedSettings"]["newsfeedPages"]
        except: pass
        try: self.joinedBaselineCollectionIdList = self.json["advancedSettings"]["joinedBaselineCollectionIdList"]
        except: pass
        try: self.activeInfo = self.json["activeInfo"]
        except: pass
        try: self.configuration = self.json["configuration"]
        except: pass
        try: self.extensions = self.json["extensions"]
        except: pass
        try: self.nameAliases = self.json["extensions"]["communityNameAliases"]
        except: pass
        try: self.templateId = self.json["templateId"]
        except: pass
        try: self.promotionalMediaList = self.json["promotionalMediaList"]
        except: pass

        return self

class CommunityList:
    def __init__(self, data):
        _agent, _rankingTable = [], []

        self.json = data

        for y in data:
            try: _agent.append(y["agent"])
            except: _agent.append(None)
            try: _rankingTable.append(RankingTableList(y["advancedSettings"]["rankingTable"]).RankingTableList)
            except: _rankingTable.append(None)

        self.agent: UserProfileList = UserProfileList(_agent).UserProfileList
        self.rankingTable = _rankingTable
        self.usersCount = []
        self.createdTime = []
        self.aminoId = []
        self.icon = []
        self.link = []
        self.comId = []
        self.modifiedTime = []
        self.status = []
        self.joinType = []
        self.tagline = []
        self.primaryLanguage = []
        self.heat = []
        self.themePack = []
        self.probationStatus = []
        self.listedStatus = []
        self.userAddedTopicList = []
        self.name = []
        self.isStandaloneAppDeprecated = []
        self.searchable = []
        self.influencerList = []
        self.keywords = []
        self.mediaList = []
        self.description = []
        self.isStandaloneAppMonetizationEnabled = []
        self.advancedSettings = []
        self.activeInfo = []
        self.configuration = []
        self.extensions = []
        self.nameAliases = []
        self.templateId = []
        self.promotionalMediaList = []
        self.defaultRankingTypeInLeaderboard = []
        self.joinedBaselineCollectionIdList = []
        self.newsfeedPages = []
        self.catalogEnabled = []
        self.pollMinFullBarVoteCount = []
        self.leaderboardStyle = []
        self.facebookAppIdList = []
        self.welcomeMessage = []
        self.welcomeMessageEnabled = []
        self.hasPendingReviewRequest = []
        self.frontPageLayout = []
        self.themeColor = []
        self.themeHash = []
        self.themeVersion = []
        self.themeUrl = []
        self.themeHomePageAppearance = []
        self.themeLeftSidePanelTop = []
        self.themeLeftSidePanelBottom = []
        self.themeLeftSidePanelColor = []
        self.customList = []

    @property
    def CommunityList(self):
        for x in self.json:
            try: self.name.append(x["name"])
            except: self.name.append(None)
            try: self.usersCount.append(x["membersCount"])
            except: self.usersCount.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.aminoId.append(x["endpoint"])
            except: self.aminoId.append(None)
            try: self.icon.append(x["icon"])
            except: self.icon.append(None)
            try: self.link.append(x["link"])
            except: self.link.append(None)
            try: self.comId.append(x["ndcId"])
            except: self.comId.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except: self.modifiedTime.append(None)
            try: self.status.append(x["status"])
            except: self.status.append(None)
            try: self.joinType.append(x["joinType"])
            except: self.joinType.append(None)
            try: self.primaryLanguage.append(x["primaryLanguage"])
            except: self.primaryLanguage.append(None)
            try: self.heat.append(x["communityHeat"])
            except: self.heat.append(None)
            try: self.userAddedTopicList.append(x["userAddedTopicList"])
            except: self.userAddedTopicList.append(None)
            try: self.probationStatus.append(x["probationStatus"])
            except: self.probationStatus.append(None)
            try: self.listedStatus.append(x["listedStatus"])
            except: self.listedStatus.append(None)
            try: self.themePack.append(x["themePack"])
            except: self.themePack.append(None)
            try: self.tagline.append(x["tagline"])
            except: self.tagline.append(None)
            try: self.searchable.append(x["searchable"])
            except: self.searchable.append(None)
            try: self.isStandaloneAppDeprecated.append(x["isStandaloneAppDeprecated"])
            except: self.isStandaloneAppDeprecated.append(None)
            try: self.influencerList.append(x["influencerList"])
            except: self.influencerList.append(None)
            try: self.keywords.append(x["keywords"])
            except: self.keywords.append(None)
            try: self.mediaList.append(x["mediaList"])
            except: self.mediaList.append(None)
            try: self.description.append(x["content"])
            except: self.description.append(None)
            try: self.isStandaloneAppMonetizationEnabled.append(x["isStandaloneAppMonetizationEnabled"])
            except: self.isStandaloneAppMonetizationEnabled.append(None)
            try: self.advancedSettings.append(x["advancedSettings"])
            except: self.advancedSettings.append(None)
            try: self.defaultRankingTypeInLeaderboard.append(x["advancedSettings"]["defaultRankingTypeInLeaderboard"])
            except: self.defaultRankingTypeInLeaderboard.append(None)
            try: self.frontPageLayout.append(x["advancedSettings"]["frontPageLayout"])
            except: self.frontPageLayout.append(None)
            try: self.hasPendingReviewRequest.append(x["advancedSettings"]["hasPendingReviewRequest"])
            except: self.hasPendingReviewRequest.append(None)
            try: self.welcomeMessageEnabled.append(x["advancedSettings"]["welcomeMessageEnabled"])
            except: self.welcomeMessageEnabled.append(None)
            try: self.welcomeMessage.append(x["advancedSettings"]["welcomeMessageText"])
            except: self.welcomeMessage.append(None)
            try: self.pollMinFullBarVoteCount.append(x["advancedSettings"]["pollMinFullBarVoteCount"])
            except: self.pollMinFullBarVoteCount.append(None)
            try: self.catalogEnabled.append(x["advancedSettings"]["catalogEnabled"])
            except: self.catalogEnabled.append(None)
            try: self.leaderboardStyle.append(x["advancedSettings"]["leaderboardStyle"])
            except: self.leaderboardStyle.append(None)
            try: self.facebookAppIdList.append(x["advancedSettings"]["facebookAppIdList"])
            except: self.facebookAppIdList.append(None)
            try: self.newsfeedPages.append(x["advancedSettings"]["newsfeedPages"])
            except: self.newsfeedPages.append(None)
            try: self.joinedBaselineCollectionIdList.append(x["advancedSettings"]["joinedBaselineCollectionIdList"])
            except: self.joinedBaselineCollectionIdList.append(None)
            try: self.activeInfo.append(x["activeInfo"])
            except: self.activeInfo.append(None)
            try: self.configuration.append(x["configuration"])
            except: self.configuration.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.nameAliases.append(x["extensions"]["communityNameAliases"])
            except: self.nameAliases.append(None)
            try: self.templateId.append(x["templateId"])
            except: self.templateId.append(None)
            try: self.promotionalMediaList.append(x["promotionalMediaList"])
            except: self.promotionalMediaList.append(None)
            try: self.themeColor.append(x["themePack"]["themeColor"])
            except: self.themeColor.append(None)
            try: self.themeHash.append(x["themePack"]["themePackHash"])
            except: self.themeHash.append(None)
            try: self.themeVersion.append(x["themePack"]["themePackRevision"])
            except: self.themeVersion.append(None)
            try: self.themeUrl.append(x["themePack"]["themePackUrl"])
            except: self.themeUrl.append(None)
            try: self.themeHomePageAppearance.append(x["configuration"]["appearance"]["homePage"]["navigation"])
            except: self.themeHomePageAppearance.append(None)
            try: self.themeLeftSidePanelTop.append(x["configuration"]["appearance"]["leftSidePanel"]["navigation"]["level1"])
            except: self.themeLeftSidePanelTop.append(None)
            try: self.themeLeftSidePanelBottom.append(x["configuration"]["appearance"]["leftSidePanel"]["navigation"]["level2"])
            except: self.themeLeftSidePanelBottom.append(None)
            try: self.themeLeftSidePanelColor.append(x["configuration"]["appearance"]["leftSidePanel"]["style"]["iconColor"])
            except: self.themeLeftSidePanelColor.append(None)
            try: self.customList.append(x["configuration"]["page"]["customList"])
            except: self.customList.append(None)

        return self

class VisitorsList:
    def __init__(self, data):
        _profile = []

        self.json = data

        for y in data["visitors"]:
            try: _profile.append(y["profile"])
            except: _profile.append(None)

        self.profile: UserProfileList = UserProfileList(_profile).UserProfileList
        self.visitors = None
        self.lastCheckTime = None
        self.visitorsCapacity = None
        self.visitorsCount = None
        self.ownerPrivacyMode = []
        self.visitorPrivacyMode = []
        self.visitTime = []

    @property
    def VisitorsList(self):
        try: self.visitors = self.json["visitors"]
        except: pass
        try: self.lastCheckTime = self.json["lastCheckTime"]
        except: pass
        try: self.visitorsCapacity = self.json["capacity"]
        except: pass
        try: self.visitorsCount = self.json["visitorsCount"]
        except: pass

        for x in self.json["visitors"]:
            try: self.ownerPrivacyMode.append(x["ownerPrivacyMode"])
            except: self.ownerPrivacyMode.append(None)
            try: self.visitorPrivacyMode.append(x["visitorPrivacyMode"])
            except: self.visitorPrivacyMode.append(None)
            try: self.visitTime.append(x["visitTime"])
            except: self.visitTime.append(None)

        return self

class CommentList:
    def __init__(self, data):
        _author = []

        self.json = data

        for y in data:
            try: _author.append(y["author"])
            except: _author.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.votesSum = []
        self.votedValue = []
        self.mediaList = []
        self.parentComId = []
        self.parentId = []
        self.parentType = []
        self.content = []
        self.extensions = []
        self.comId = []
        self.modifiedTime = []
        self.createdTime = []
        self.commentId = []
        self.subcommentsCount = []
        self.type = []

    @property
    def CommentList(self):
        for x in self.json:
            try: self.votesSum.append(x["votesSum"])
            except: self.votesSum.append(None)
            try: self.votedValue.append(x["votedValue"])
            except: self.votedValue.append(None)
            try: self.mediaList.append(x["mediaList"])
            except: self.mediaList.append(None)
            try: self.parentComId.append(x["parentNdcId"])
            except: self.parentComId.append(None)
            try: self.parentId.append(x["parentId"])
            except: self.parentId.append(None)
            try: self.parentType.append(x["parentType"])
            except: self.parentType.append(None)
            try: self.content.append(x["content"])
            except: self.content.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.comId.append(x["ndcId"])
            except: self.comId.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except: self.modifiedTime.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.commentId.append(x["commentId"])
            except: self.commentId.append(None)
            try: self.subcommentsCount.append(x["subcommentsCount"])
            except: self.subcommentsCount.append(None)
            try: self.type.append(x["type"])
            except: self.type.append(None)

        return self

class Membership:
    def __init__(self, data):
        self.json = data
        self.premiumFeature = None
        self.hasAnyAndroidSubscription = None
        self.hasAnyAppleSubscription = None
        self.accountMembership = None
        self.paymentType = None
        self.membershipStatus = None
        self.isAutoRenew = None
        self.createdTime = None
        self.modifiedTime = None
        self.renewedTime = None
        self.expiredTime = None

    @property
    def Membership(self):
        try: self.premiumFeature = self.json["premiumFeatureEnabled"]
        except: pass
        try: self.hasAnyAndroidSubscription = self.json["hasAnyAndroidSubscription"]
        except: pass
        try: self.hasAnyAppleSubscription = self.json["hasAnyAppleSubscription"]
        except: pass
        try: self.accountMembership = self.json["accountMembershipEnabled"]
        except: pass
        try: self.paymentType = self.json["paymentType"]
        except: pass
        try: self.membershipStatus = self.json["membership"]["membershipStatus"]
        except: pass
        try: self.isAutoRenew = self.json["membership"]["isAutoRenew"]
        except: pass
        try: self.createdTime = self.json["membership"]["createdTime"]
        except: pass
        try: self.modifiedTime = self.json["membership"]["modifiedTime"]
        except: pass
        try: self.renewedTime = self.json["membership"]["renewedTime"]
        except: pass
        try: self.expiredTime = self.json["membership"]["expiredTime"]
        except: pass

        return self

class FromCode:
    def __init__(self, data):
        self.json = data
        self.path = None
        self.objectType = None
        self.shortCode = None
        self.fullPath = None
        self.targetCode = None
        self.objectId = None
        self.shortUrl = None
        self.fullUrl = None

    @property
    def FromCode(self):
        try: self.path = self.json["path"]
        except: pass
        try: self.objectType = self.json["extensions"]["linkInfo"]["objectType"]
        except: pass
        try: self.shortCode = self.json["extensions"]["linkInfo"]["shortCode"]
        except: pass
        try: self.fullPath = self.json["extensions"]["linkInfo"]["fullPath"]
        except: pass
        try: self.targetCode = self.json["extensions"]["linkInfo"]["targetCode"]
        except: pass
        try: self.objectId = self.json["extensions"]["linkInfo"]["objectId"]
        except: pass
        try: self.shortUrl = self.json["extensions"]["linkInfo"]["shareURLShortCode"]
        except: pass
        try: self.fullUrl = self.json["extensions"]["linkInfo"]["shareURLFullPath"]
        except: pass

        return self

class UserProfileCountList:
    def __init__(self, data):
        self.json = data

        try: self.profile: UserProfileList = UserProfileList(data["userProfileList"]).UserProfileList
        except: self.profile: UserProfileList = UserProfileList([])

        self.userProfileCount = None

    @property
    def UserProfileCountList(self):
        try: self.userProfileCount = self.json["userProfileCount"]
        except: pass

        return self

class UserCheckIns:
    def __init__(self, data):
        self.json = data
        self.hasAnyCheckIn = None
        self.brokenStreaks = None
        self.consecutiveCheckInDays = None

    @property
    def UserCheckIns(self):
        try: self.hasAnyCheckIn = self.json["hasAnyCheckIn"]
        except: pass
        try: self.brokenStreaks = self.json["brokenStreaks"]
        except: pass
        try: self.consecutiveCheckInDays = self.json["consecutiveCheckInDays"]
        except: pass

        return self

class WalletInfo:
    def __init__(self, data):
        self.json = data
        self.totalCoinsFloat = None
        self.adsEnabled = None
        self.adsVideoStats = None
        self.adsFlags = None
        self.totalCoins = None
        self.businessCoinsEnabled = None
        self.totalBusinessCoins = None
        self.totalBusinessCoinsFloat = None

    @property
    def WalletInfo(self):
        try: self.totalCoinsFloat = self.json["totalCoinsFloat"]
        except: pass
        try: self.adsEnabled = self.json["adsEnabled"]
        except: pass
        try: self.adsVideoStats = self.json["adsVideoStats"]
        except: pass
        try: self.adsFlags = self.json["adsFlags"]
        except: pass
        try: self.totalCoins = self.json["totalCoins"]
        except: pass
        try: self.businessCoinsEnabled = self.json["businessCoinsEnabled"]
        except: pass
        try: self.totalBusinessCoins = self.json["totalBusinessCoins"]
        except: pass
        try: self.totalBusinessCoinsFloat = self.json["totalBusinessCoinsFloat"]
        except: pass

        return self

class WalletHistory:
    def __init__(self, data):
        self.json = data
        self.taxCoins = []
        self.bonusCoinsFloat = []
        self.isPositive = []
        self.bonusCoins = []
        self.taxCoinsFloat = []
        self.transanctionId = []
        self.changedCoins = []
        self.totalCoinsFloat = []
        self.changedCoinsFloat = []
        self.sourceType = []
        self.createdTime = []
        self.totalCoins = []
        self.originCoinsFloat = []
        self.originCoins = []
        self.extData = []
        self.title = []
        self.description = []
        self.icon = []
        self.objectDeeplinkUrl = []
        self.sourceIp = []

    @property
    def WalletHistory(self):
        for x in self.json:
            try: self.taxCoins.append(x["taxCoins"])
            except: self.taxCoins.append(None)
            try: self.bonusCoinsFloat.append(x["bonusCoinsFloat"])
            except: self.bonusCoinsFloat.append(None)
            try: self.isPositive.append(x["isPositive"])
            except: self.isPositive.append(None)
            try: self.bonusCoins.append(x["bonusCoins"])
            except: self.bonusCoins.append(None)
            try: self.taxCoinsFloat.append(x["taxCoinsFloat"])
            except: self.taxCoinsFloat.append(None)
            try: self.transanctionId.append(x["uid"])
            except: self.transanctionId.append(None)
            try: self.changedCoins.append(x["changedCoins"])
            except: self.changedCoins.append(None)
            try: self.totalCoinsFloat.append(x["totalCoinsFloat"])
            except: self.totalCoinsFloat.append(None)
            try: self.changedCoinsFloat.append(x["changedCoinsFloat"])
            except: self.changedCoinsFloat.append(None)
            try: self.sourceType.append(x["sourceType"])
            except: self.sourceType.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.totalCoins.append(x["totalCoins"])
            except: self.totalCoins.append(None)
            try: self.originCoinsFloat.append(x["originCoinsFloat"])
            except: self.originCoinsFloat.append(None)
            try: self.originCoins.append(x["originCoins"])
            except: self.originCoins.append(None)
            try: self.extData.append(x["extData"])
            except: self.extData.append(None)
            try: self.title.append(x["extData"]["description"])
            except: self.title.append(None)
            try: self.icon.append(x["extData"]["icon"])
            except: self.icon.append(None)
            try: self.description.append(x["extData"]["subtitle"])
            except: self.description.append(None)
            try: self.objectDeeplinkUrl.append(x["extData"]["objectDeeplinkUrl"])
            except: self.objectDeeplinkUrl.append(None)
            try: self.sourceIp.append(x["extData"]["sourceIp"])
            except: self.sourceIp.append(None)

        return self


class UserAchievements:
    def __init__(self, data):
        self.json = data
        self.secondsSpentOfLast24Hours = None
        self.secondsSpentOfLast7Days = None
        self.numberOfFollowersCount = None
        self.numberOfPostsCreated = None

    @property
    def UserAchievements(self):
        try: self.secondsSpentOfLast24Hours = self.json["secondsSpentOfLast24Hours"]
        except: pass
        try: self.secondsSpentOfLast7Days = self.json["secondsSpentOfLast7Days"]
        except: pass
        try: self.numberOfFollowersCount = self.json["numberOfMembersCount"]
        except: pass
        try: self.numberOfPostsCreated = self.json["numberOfPostsCreated"]
        except: pass

        return self

class UserSavedBlogs:
    def __init__(self, data):
        _object = []

        self.json = data

        for y in data:
            if y["refObjectType"] == 1:
                try: _object.append(Blog(y["refObject"]).Blog)
                except: _object.append(None)

            elif y["refObjectType"] == 2:
                try: _object.append(Wiki(y["refObject"]).Wiki)
                except: _object.append(None)

            else:
                try: _object.append(y["refObject"])
                except: _object.append(None)

        self.object = _object
        self.objectType = []
        self.bookmarkedTime = []
        self.objectId = []
        self.objectJson = []

    @property
    def UserSavedBlogs(self):
        for x in self.json:
            try: self.objectType.append(x["refObjectType"])
            except: self.objectType.append(None)
            try: self.bookmarkedTime.append(x["bookmarkedTime"])
            except: self.bookmarkedTime.append(None)
            try: self.objectId.append(x["refObjectId"])
            except: self.objectId.append(None)
            try: self.objectJson.append(x["refObject"])
            except: self.objectJson.append(None)

        return self

class GetWikiInfo:
    def __init__(self, data):
        self.json = data

        try: self.wiki: Wiki = Wiki(data["item"]).Wiki
        except: self.wiki: Wiki = Wiki([])

        self.inMyFavorites = None
        self.isBookmarked = None

    @property
    def GetWikiInfo(self):
        try: self.inMyFavorites = self.json["inMyFavorites"]
        except: pass
        try: self.isBookmarked = self.json["isBookmarked"]
        except: pass

        return self

class GetBlogInfo:
    def __init__(self, data):
        self.json = data

        try: self.blog: Blog = Blog(data["blog"]).Blog
        except: self.blog: Blog = Blog([])

        self.isBookmarked = None

    @property
    def GetBlogInfo(self):
        try: self.isBookmarked = self.json["isBookmarked"]
        except: pass

        return self

class GetSharedFolderInfo:
    def __init__(self, data):
        self.json = data
        self.folderCount = None
        self.fileCount = None

    @property
    def GetSharedFolderInfo(self):
        try: self.folderCount = self.json["folderCount"]
        except: pass
        try: self.fileCount = self.json["fileCount"]
        except: pass

        return self

class WikiCategoryList:
    def __init__(self, data):
        _author = []

        self.json = data

        for y in data:
            try: _author.append(y["author"])
            except: _author.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.itemsCount = []
        self.parentCategoryId = []
        self.categoryId = []
        self.content = []
        self.extensions = []
        self.createdTime = []
        self.subcategoriesCount = []
        self.title = []
        self.mediaList = []
        self.icon = []

    @property
    def WikiCategoryList(self):
        for x in self.json:
            try: self.itemsCount.append(x["itemsCount"])
            except: self.itemsCount.append(None)
            try: self.parentCategoryId.append(x["parentCategoryId"])
            except: self.parentCategoryId.append(None)
            try: self.categoryId.append(x["categoryId"])
            except: self.categoryId.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.title.append(x["label"])
            except: self.title.append(None)
            try: self.mediaList.append(x["mediaList"])
            except: self.mediaList.append(None)
            try: self.icon.append(x["icon"])
            except: self.icon.append(None)

        return self

class WikiCategory:
    def __init__(self, data):
        self.json = data

        try: self.author = UserProfile(data["itemCategory"]["author"]).UserProfile
        except: self.author: UserProfile = UserProfile([])
        try: self.subCategory = WikiCategoryList(data["childrenWrapper"]["itemCategoryList"]).WikiCategoryList
        except: self.subCategory: WikiCategoryList = WikiCategoryList([])

        self.itemsCount = None
        self.parentCategoryId = None
        self.parentType = None
        self.categoryId = None
        self.content = None
        self.extensions = None
        self.createdTime = None
        self.subcategoriesCount = None
        self.title = None
        self.mediaList = None
        self.icon = None

    @property
    def WikiCategory(self):
        try: self.itemsCount = self.json["itemCategory"]["itemsCount"]
        except: pass
        try: self.parentCategoryId = self.json["itemCategory"]["parentCategoryId"]
        except: pass
        try: self.categoryId = self.json["itemCategory"]["categoryId"]
        except: pass
        try: self.extensions = self.json["itemCategory"]["extensions"]
        except: pass
        try: self.createdTime = self.json["itemCategory"]["createdTime"]
        except: pass
        try: self.title = self.json["itemCategory"]["label"]
        except: pass
        try: self.mediaList = self.json["itemCategory"]["mediaList"]
        except: pass
        try: self.icon = self.json["itemCategory"]["icon"]
        except: pass
        try: self.parentType = self.json["childrenWrapper"]["type"]
        except: pass

        return self

class TippedUsersSummary:
    def __init__(self, data):
        _author = []

        self.json = data

        for y in data["tippedUserList"]:
            try: _author.append(y["tipper"])
            except: _author.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.tipSummary = None
        self.totalCoins = None
        self.tippersCount = None
        self.globalTipSummary = None
        self.globalTippersCount = None
        self.globalTotalCoins = None
        self.lastTippedTime = []
        self.totalTippedCoins = []
        self.lastThankedTime = []

    @property
    def TippedUsersSummary(self):
        try: self.tipSummary = self.json["tipSummary"]
        except: pass
        try: self.totalCoins = self.json["tipSummary"]["totalCoins"]
        except: pass
        try: self.tippersCount = self.json["tipSummary"]["tippersCount"]
        except: pass
        try: self.globalTipSummary = self.json["globalTipSummary"]
        except: pass
        try: self.globalTippersCount = self.json["globalTipSummary"]["tippersCount"]
        except: pass
        try: self.globalTotalCoins = self.json["globalTipSummary"]["totalCoins"]
        except: pass

        for tippedUserList in self.json["tippedUserList"]:
            try: self.lastTippedTime.append(tippedUserList["lastTippedTime"])
            except: self.lastTippedTime.append(None)
            try: self.totalTippedCoins.append(tippedUserList["totalTippedCoins"])
            except: self.totalTippedCoins.append(None)
            try: self.lastThankedTime.append(tippedUserList["lastThankedTime"])
            except: self.lastThankedTime.append(None)

        return self

class Thread:
    def __init__(self, data):
        self.json = data

        try: self.author: UserProfile = UserProfile(data["author"]).UserProfile
        except: self.author: UserProfile = UserProfile([])
        try: self.membersSummary: UserProfileList = UserProfileList(data["membersSummary"]).UserProfileList
        except: self.membersSummary: UserProfileList = UserProfileList([])

        self.userAddedTopicList = None
        self.membersQuota = None
        self.chatId = None
        self.keywords = None
        self.membersCount = None
        self.isPinned = None
        self.title = None
        self.membershipStatus = None
        self.content = None
        self.needHidden = None
        self.alertOption = None
        self.lastReadTime = None
        self.type = None
        self.status = None
        self.publishToGlobal = None
        self.modifiedTime = None
        self.condition = None
        self.icon = None
        self.latestActivityTime = None
        self.extensions = None
        self.viewOnly = None
        self.coHosts = None
        self.membersCanInvite = None
        self.announcement = None
        self.language = None
        self.lastMembersSummaryUpdateTime = None
        self.backgroundImage = None
        self.channelType = None
        self.comId = None
        self.createdTime = None
        self.creatorId = None
        self.bannedUsers = None
        self.tippingPermStatus = None
        self.visibility = None
        self.fansOnly = None
        self.pinAnnouncement = None
        self.vvChatJoinType = None
        self.screeningRoomHostId = None
        self.screeningRoomPermission = None
        self.disabledTime = None

    @property
    def Thread(self):
        try: self.userAddedTopicList = self.json["userAddedTopicList"]
        except: pass
        try: self.membersQuota = self.json["membersQuota"]
        except: pass
        try: self.chatId = self.json["threadId"]
        except: pass
        try: self.keywords = self.json["keywords"]
        except: pass
        try: self.membersCount = self.json["membersCount"]
        except: pass
        try: self.isPinned = self.json["isPinned"]
        except: pass
        try: self.title = self.json["title"]
        except: pass
        try: self.content = self.json["content"]
        except: pass
        try: self.needHidden = self.json["needHidden"]
        except: pass
        try: self.alertOption = self.json["alertOption"]
        except: pass
        try: self.lastReadTime = self.json["lastReadTime"]
        except: pass
        try: self.type = self.json["type"]
        except: pass
        try: self.status = self.json["status"]
        except: pass
        try: self.publishToGlobal = self.json["publishToGlobal"]
        except: pass
        try: self.modifiedTime = self.json["modifiedTime"]
        except: pass
        try: self.condition = self.json["condition"]
        except: pass
        try: self.icon = self.json["icon"]
        except: pass
        try: self.latestActivityTime = self.json["latestActivityTime"]
        except: pass
        try: self.comId = self.json["ndcId"]
        except: pass
        try: self.createdTime = self.json["createdTime"]
        except: pass
        try: self.extensions = self.json["extensions"]
        except: pass
        try: self.viewOnly = self.json["extensions"]["viewOnly"]
        except: pass
        try: self.coHosts = self.json["extensions"]["coHost"]
        except: pass
        try: self.membersCanInvite = self.json["extensions"]["membersCanInvite"]
        except: pass
        try: self.language = self.json["extensions"]["language"]
        except: pass
        try: self.announcement = self.json["extensions"]["announcement"]
        except: pass
        try: self.backgroundImage = self.json["extensions"]["bm"][1]
        except: pass
        try: self.lastMembersSummaryUpdateTime = self.json["extensions"]["lastMembersSummaryUpdateTime"]
        except: pass
        try: self.channelType = self.json["extensions"]["channelType"]
        except: pass
        try: self.creatorId = self.json["extensions"]["creatorUid"]
        except: pass
        try: self.bannedUsers = self.json["extensions"]["bannedMemberUidList"]
        except: pass
        try: self.visibility = self.json["extensions"]["visibility"]
        except: pass
        try: self.fansOnly = self.json["extensions"]["fansOnly"]
        except: pass
        try: self.pinAnnouncement = self.json["extensions"]["pinAnnouncement"]
        except: pass
        try: self.vvChatJoinType = self.json["extensions"]["vvChatJoinType"]
        except: pass
        try: self.disabledTime = self.json["extensions"]["__disabledTime__"]
        except: pass
        try: self.tippingPermStatus = self.json["extensions"]["tippingPermStatus"]
        except: pass
        try: self.screeningRoomHostId = self.json["extensions"]["screeningRoomHostUid"]
        except: pass
        try: self.screeningRoomPermission = self.json["extensions"]["screeningRoomPermission"]["action"]
        except: pass

        return self

class ThreadList:
    def __init__(self, data):
        _author, _membersSummary = [], []

        self.json = data

        for y in data:
            try: _author.append(y["author"])
            except: _author.append(None)

            try: _membersSummary.append(UserProfileList(y["membersSummary"]).UserProfileList)
            except: _membersSummary.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.membersSummary = _membersSummary
        self.userAddedTopicList = []
        self.membersQuota = []
        self.chatId = []
        self.keywords = []
        self.membersCount = []
        self.isPinned = []
        self.title = []
        self.membershipStatus = []
        self.content = []
        self.needHidden = []
        self.alertOption = []
        self.lastReadTime = []
        self.type = []
        self.status = []
        self.publishToGlobal = []
        self.modifiedTime = []
        self.condition = []
        self.icon = []
        self.latestActivityTime = []
        self.extensions = []
        self.viewOnly = []
        self.coHosts = []
        self.membersCanInvite = []
        self.announcement = []
        self.language = []
        self.lastMembersSummaryUpdateTime = []
        self.backgroundImage = []
        self.channelType = []
        self.comId = []
        self.createdTime = []
        self.creatorId = []
        self.bannedUsers = []
        self.tippingPermStatus = []
        self.visibility = []
        self.fansOnly = []
        self.pinAnnouncement = []
        self.vvChatJoinType = []
        self.screeningRoomHostId = []
        self.screeningRoomPermission = []
        self.disabledTime = []

    @property
    def ThreadList(self):
        for chat in self.json:
            try: self.userAddedTopicList.append(chat["userAddedTopicList"])
            except: self.userAddedTopicList.append(None)
            try: self.membersQuota.append(chat["membersQuota"])
            except: self.membersQuota.append(None)
            try: self.chatId.append(chat["threadId"])
            except: self.chatId.append(None)
            try: self.keywords.append(chat["keywords"])
            except: self.keywords.append(None)
            try: self.membersCount.append(chat["membersCount"])
            except: self.membersCount.append(None)
            try: self.isPinned.append(chat["isPinned"])
            except: self.isPinned.append(None)
            try: self.title.append(chat["title"])
            except: self.title.append(None)
            try: self.content.append(chat["content"])
            except: self.content.append(None)
            try: self.needHidden.append(chat["needHidden"])
            except: self.needHidden.append(None)
            try: self.alertOption.append(chat["alertOption"])
            except: self.alertOption.append(None)
            try: self.lastReadTime.append(chat["lastReadTime"])
            except: self.lastReadTime.append(None)
            try: self.type.append(chat["type"])
            except: self.type.append(None)
            try: self.status.append(chat["status"])
            except: self.status.append(None)
            try: self.publishToGlobal.append(chat["publishToGlobal"])
            except: self.publishToGlobal.append(None)
            try: self.modifiedTime.append(chat["modifiedTime"])
            except: self.modifiedTime.append(None)
            try: self.condition.append(chat["condition"])
            except: self.condition.append(None)
            try: self.icon.append(chat["icon"])
            except: self.icon.append(None)
            try: self.latestActivityTime.append(chat["latestActivityTime"])
            except: self.latestActivityTime.append(None)
            try: self.comId.append(chat["ndcId"])
            except: self.comId.append(None)
            try: self.createdTime.append(chat["createdTime"])
            except: self.createdTime.append(None)
            try:  self.extensions.append(chat["extensions"])
            except: self.extensions.append(None)
            try:  self.viewOnly.append(chat["extensions"]["viewOnly"])
            except: self.viewOnly.append(None)
            try:  self.coHosts.append(chat["extensions"]["coHost"])
            except: self.coHosts.append(None)
            try:  self.membersCanInvite.append(chat["extensions"]["membersCanInvite"])
            except: self.membersCanInvite.append(None)
            try:  self.language.append(chat["extensions"]["language"])
            except: self.language.append(None)
            try:  self.announcement.append(chat["extensions"]["announcement"])
            except: self.announcement.append(None)
            try:  self.backgroundImage.append(chat["extensions"]["bm"][1])
            except: self.backgroundImage.append(None)
            try:  self.lastMembersSummaryUpdateTime.append(chat["extensions"]["lastMembersSummaryUpdateTime"])
            except: self.lastMembersSummaryUpdateTime.append(None)
            try:  self.channelType.append(chat["extensions"]["channelType"])
            except: self.channelType.append(None)
            try:  self.creatorId.append(chat["extensions"]["creatorUid"])
            except: self.creatorId.append(None)
            try:  self.bannedUsers.append(chat["extensions"]["bannedMemberUidList"])
            except: self.bannedUsers.append(None)
            try:  self.visibility.append(chat["extensions"]["visibility"])
            except: self.visibility.append(None)
            try:  self.fansOnly.append(chat["extensions"]["fansOnly"])
            except: self.fansOnly.append(None)
            try:  self.pinAnnouncement.append(chat["extensions"]["pinAnnouncement"])
            except: self.pinAnnouncement.append(None)
            try:  self.vvChatJoinType.append(chat["extensions"]["vvChatJoinType"])
            except: self.vvChatJoinType.append(None)
            try:  self.tippingPermStatus.append(chat["extensions"]["tippingPermStatus"])
            except: self.tippingPermStatus.append(None)
            try:  self.screeningRoomHostId.append(chat["extensions"]["screeningRoomHostUid"])
            except: self.screeningRoomHostId.append(None)
            try:  self.disabledTime.append(chat["extensions"]["__disabledTime__"])
            except: self.disabledTime.append(None)
            try:  self.screeningRoomPermission.append(chat["extensions"]["screeningRoomPermission"]["action"])
            except: self.screeningRoomPermission.append(None)

        return self

class Sticker:
    def __init__(self, data):
        self.json = data

        try: self.collection: StickerCollection = StickerCollection(data["stickerCollectionSummary"]).StickerCollection
        except: self.collection: StickerCollection = StickerCollection([])

        self.status = None
        self.icon = None
        self.iconV2 = None
        self.name = None
        self.stickerId = None
        self.smallIcon = None
        self.smallIconV2 = None
        self.stickerCollectionId = None
        self.mediumIcon = None
        self.mediumIconV2 = None
        self.extensions = None
        self.usedCount = None
        self.createdTime = None

    @property
    def Sticker(self):
        try: self.status = self.json["status"]
        except: pass
        try: self.icon = self.json["icon"]
        except: pass
        try: self.iconV2 = self.json["iconV2"]
        except: pass
        try: self.name = self.json["name"]
        except: pass
        try: self.stickerId = self.json["stickerId"]
        except: pass
        try: self.smallIcon = self.json["smallIcon"]
        except: pass
        try: self.smallIconV2 = self.json["smallIconV2"]
        except: pass
        try: self.stickerCollectionId = self.json["stickerCollectionId"]
        except: pass
        try: self.mediumIcon = self.json["mediumIcon"]
        except: pass
        try: self.mediumIconV2 = self.json["mediumIconV2"]
        except: pass
        try: self.extensions = self.json["extensions"]
        except: pass
        try: self.usedCount = self.json["usedCount"]
        except: pass
        try: self.createdTime = self.json["createdTime"]
        except: pass

        return self

class StickerList:
    def __init__(self, data):
        _collection = []

        self.json = data

        for y in data:
            try: _collection.append(y["stickerCollectionSummary"])
            except: _collection.append(None)

        self.collection: StickerCollectionList = StickerCollectionList(_collection).StickerCollectionList
        self.status = []
        self.icon = []
        self.iconV2 = []
        self.name = []
        self.stickerId = []
        self.smallIcon = []
        self.smallIconV2 = []
        self.stickerCollectionId = []
        self.mediumIcon = []
        self.mediumIconV2 = []
        self.extensions = []
        self.usedCount = []
        self.createdTime = []

    @property
    def StickerList(self):
        for x in self.json:
            try: self.status.append(x["status"])
            except: self.status.append(None)
            try: self.icon.append(x["icon"])
            except: self.icon.append(None)
            try: self.iconV2.append(x["iconV2"])
            except: self.iconV2.append(None)
            try: self.name.append(x["name"])
            except: self.name.append(None)
            try: self.stickerId.append(x["stickerId"])
            except: self.stickerId.append(None)
            try: self.smallIcon.append(x["smallIcon"])
            except: self.smallIcon.append(None)
            try: self.smallIconV2.append(x["smallIconV2"])
            except: self.smallIconV2.append(None)
            try: self.stickerCollectionId.append(x["stickerCollectionId"])
            except: self.stickerCollectionId.append(None)
            try: self.mediumIcon.append(x["mediumIcon"])
            except: self.mediumIcon.append(None)
            try: self.mediumIconV2.append(x["mediumIconV2"])
            except: self.mediumIconV2.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.usedCount.append(x["usedCount"])
            except: self.usedCount.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)

        return self

class StickerCollection:
    def __init__(self, data):
        self.json = data

        try: self.author: UserProfile = UserProfile(data["author"]).UserProfile
        except: self.author: UserProfile = UserProfile([])
        try: self.originalAuthor: UserProfile = UserProfile(data["extensions"]["originalAuthor"]).UserProfile
        except: self.originalAuthor: UserProfile = UserProfile([])
        try: self.originalCommunity: Community = Community(data["extensions"]["originalCommunity"]).Community
        except: self.originalCommunity: Community = Community([])

        self.status = None
        self.collectionType = None
        self.modifiedTime = None
        self.bannerUrl = None
        self.smallIcon = None
        self.stickersCount = None
        self.usedCount = None
        self.icon = None
        self.title = None
        self.collectionId = None
        self.extensions = None
        self.isActivated = None
        self.ownershipStatus = None
        self.isNew = None
        self.availableComIds = None
        self.description = None
        self.iconSourceStickerId = None
        self.restrictionInfo = None
        self.discountValue = None
        self.discountStatus = None
        self.ownerId = None
        self.ownerType = None
        self.restrictType = None
        self.restrictValue = None
        self.availableDuration = None

    @property
    def StickerCollection(self):
        try: self.status = self.json["status"]
        except: pass
        try: self.collectionType = self.json["collectionType"]
        except: pass
        try: self.modifiedTime = self.json["modifiedTime"]
        except: pass
        try: self.bannerUrl = self.json["bannerUrl"]
        except: pass
        try: self.smallIcon = self.json["smallIcon"]
        except: pass
        try: self.stickersCount = self.json["stickersCount"]
        except: pass
        try: self.usedCount = self.json["usedCount"]
        except: pass
        try: self.icon = self.json["icon"]
        except: pass
        try: self.title = self.json["name"]
        except: pass
        try: self.collectionId = self.json["collectionId"]
        except: pass
        try: self.extensions = self.json["extensions"]
        except: pass
        try: self.iconSourceStickerId = self.json["extensions"]["iconSourceStickerId"]
        except: pass
        try: self.isActivated = self.json["isActivated"]
        except: pass
        try: self.ownershipStatus = self.json["ownershipStatus"]
        except: pass
        try: self.isNew = self.json["isNew"]
        except: pass
        try: self.availableComIds = self.json["availableNdcIds"]
        except: pass
        try: self.description = self.json["description"]
        except: pass
        try: self.restrictionInfo = self.json["restrictionInfo"]
        except: pass
        try: self.discountStatus = self.json["restrictionInfo"]["discountStatus"]
        except: pass
        try: self.discountValue = self.json["restrictionInfo"]["discountValue"]
        except: pass
        try: self.ownerId = self.json["restrictionInfo"]["ownerUid"]
        except: pass
        try: self.ownerType = self.json["restrictionInfo"]["ownerType"]
        except: pass
        try: self.restrictType = self.json["restrictionInfo"]["restrictType"]
        except: pass
        try: self.restrictValue = self.json["restrictionInfo"]["restrictValue"]
        except: pass
        try: self.availableDuration = self.json["restrictionInfo"]["availableDuration"]
        except: pass

        return self

class StickerCollectionList:
    def __init__(self, data):
        _author, _originalAuthor, _originalCommunity = [], [], []

        self.json = data

        for y in data:
            try: _author.append(y["author"])
            except: _author.append(None)
            try: _originalAuthor.append(y["extensions"]["originalAuthor"])
            except: _originalAuthor.append(None)
            try: _originalCommunity.append(y["extensions"]["originalCommunity"])
            except: _originalCommunity.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.originalAuthor: UserProfileList = UserProfileList(_originalAuthor).UserProfileList
        self.originalCommunity: CommunityList = CommunityList(_originalCommunity).CommunityList
        self.status = []
        self.collectionType = []
        self.modifiedTime = []
        self.bannerUrl = []
        self.smallIcon = []
        self.stickersCount = []
        self.usedCount = []
        self.icon = []
        self.name = []
        self.collectionId = []
        self.extensions = []
        self.isActivated = []
        self.ownershipStatus = []
        self.isNew = []
        self.availableComIds = []
        self.description = []
        self.iconSourceStickerId = []
        self.restrictionInfo = []
        self.discountValue = []
        self.discountStatus = []
        self.ownerId = []
        self.ownerType = []
        self.restrictType = []
        self.restrictValue = []
        self.availableDuration = []

    @property
    def StickerCollectionList(self):
        for x in self.json:
            try: self.status.append(x["status"])
            except: self.status.append(None)
            try: self.collectionType.append(x["collectionType"])
            except: self.collectionType.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except: self.modifiedTime.append(None)
            try: self.bannerUrl.append(x["bannerUrl"])
            except: self.bannerUrl.append(None)
            try: self.smallIcon.append(x["smallIcon"])
            except: self.smallIcon.append(None)
            try: self.stickersCount.append(x["stickersCount"])
            except: self.stickersCount.append(None)
            try: self.usedCount.append(x["usedCount"])
            except: self.usedCount.append(None)
            try: self.icon.append(x["icon"])
            except: self.icon.append(None)
            try: self.name.append(x["name"])
            except: self.name.append(None)
            try: self.collectionId.append(x["collectionId"])
            except: self.collectionId.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.iconSourceStickerId.append(x["extensions"]["iconSourceStickerId"])
            except: self.iconSourceStickerId.append(None)
            try: self.isActivated.append(x["isActivated"])
            except: self.isActivated.append(None)
            try: self.ownershipStatus.append(x["ownershipStatus"])
            except: self.ownershipStatus.append(None)
            try: self.isNew.append(x["isNew"])
            except: self.isNew.append(None)
            try: self.availableComIds.append(x["availableNdcIds"])
            except: self.availableComIds.append(None)
            try: self.description.append(x["description"])
            except: self.description.append(None)
            try: self.restrictionInfo.append(x["restrictionInfo"])
            except: self.restrictionInfo.append(None)
            try: self.discountStatus.append(x["restrictionInfo"]["discountStatus"])
            except: self.discountStatus.append(None)
            try: self.discountValue.append(x["restrictionInfo"]["discountValue"])
            except: self.discountValue.append(None)
            try: self.ownerId.append(x["restrictionInfo"]["ownerUid"])
            except: self.ownerId.append(None)
            try: self.ownerType.append(x["restrictionInfo"]["ownerType"])
            except: self.ownerType.append(None)
            try: self.restrictType.append(x["restrictionInfo"]["restrictType"])
            except: self.restrictType.append(None)
            try: self.restrictValue.append(x["restrictionInfo"]["restrictValue"])
            except: self.restrictValue.append(None)
            try: self.availableDuration.append(x["restrictionInfo"]["availableDuration"])
            except: self.availableDuration.append(None)

        return self

class Message:
    def __init__(self, data):
        self.json = data

        try: self.author: UserProfile = UserProfile(data["author"]).UserProfile
        except: self.author: UserProfile = UserProfile([])
        try: self.sticker: Sticker = Sticker(data["extensions"]["sticker"]).Sticker
        except: self.sticker: Sticker = Sticker([])

        self.content = None
        self.includedInSummary = None
        self.isHidden = None
        self.messageType = None
        self.messageId = None
        self.mediaType = None
        self.mediaValue = None
        self.chatBubbleId = None
        self.clientRefId = None
        self.chatId = None
        self.createdTime = None
        self.chatBubbleVersion = None
        self.type = None
        self.extensions = None
        self.duration = None
        self.originalStickerId = None
        self.videoDuration = None
        self.videoExtensions = None
        self.videoHeight = None
        self.videoCoverImage = None
        self.videoWidth = None
        self.mentionUserIds = None
        self.tippingCoins = None

    @property
    def Message(self):
        try: self.content = self.json["content"]
        except: pass
        try: self.includedInSummary = self.json["includedInSummary"]
        except: pass
        try: self.isHidden = self.json["isHidden"]
        except: pass
        try: self.messageId = self.json["messageId"]
        except: pass
        try: self.messageType = self.json["messageType"]
        except: pass
        try: self.mediaType = self.json["mediaType"]
        except: pass
        try: self.chatBubbleId = self.json["chatBubbleId"]
        except: pass
        try: self.clientRefId = self.json["clientRefId"]
        except: pass
        try: self.chatId = self.json["threadId"]
        except: pass
        try: self.createdTime = self.json["createdTime"]
        except: pass
        try: self.chatBubbleVersion = self.json["chatBubbleVersion"]
        except: pass
        try: self.type = self.json["type"]
        except: pass
        try: self.mediaValue = self.json["mediaValue"]
        except: pass
        try: self.extensions = self.json["extensions"]
        except: pass
        try: self.duration = self.json["extensions"]["duration"]
        except: pass
        try: self.videoDuration = self.json["extensions"]["videoExtensions"]["duration"]
        except: pass
        try: self.videoHeight = self.json["extensions"]["videoExtensions"]["height"]
        except: pass
        try: self.videoWidth = self.json["extensions"]["videoExtensions"]["width"]
        except: pass
        try: self.videoCoverImage = self.json["extensions"]["videoExtensions"]["coverImage"]
        except: pass
        try: self.originalStickerId = self.json["extensions"]["originalStickerId"]
        except: pass
        try: self.mentionUserIds = self.json["extensions"]["mentionUserIds"]
        except: pass
        try: self.tippingCoins = self.json["extensions"]["tippingCoins"]
        except: pass

        return self

class MessageList:
    def __init__(self, data, nextPageToken = None, prevPageToken = None):
        _author, _sticker = [], []

        self.json = data
        self.nextPageToken = nextPageToken
        self.prevPageToken = prevPageToken

        for y in data:
            try: _author.append(y["author"])
            except: _author.append(None)
            try: _sticker.append(y["extensions"]["sticker"])
            except: _sticker.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.sticker: StickerList = StickerList(_sticker).StickerList
        self.content = []
        self.includedInSummary = []
        self.isHidden = []
        self.messageType = []
        self.messageId = []
        self.mediaType = []
        self.mediaValue = []
        self.chatBubbleId = []
        self.clientRefId = []
        self.chatId = []
        self.createdTime = []
        self.chatBubbleVersion = []
        self.type = []
        self.extensions = []
        self.mentionUserIds = []
        self.duration = []
        self.originalStickerId = []
        self.videoExtensions = []
        self.videoDuration = []
        self.videoHeight = []
        self.videoWidth = []
        self.videoCoverImage = []
        self.tippingCoins = []

    @property
    def MessageList(self):
        for x in self.json:
            try: self.content.append(x["content"])
            except: self.content.append(None)
            try: self.includedInSummary.append(x["includedInSummary"])
            except: self.includedInSummary.append(None)
            try: self.isHidden.append(x["isHidden"])
            except: self.isHidden.append(None)
            try: self.messageId.append(x["messageId"])
            except: self.messageId.append(None)
            try: self.chatBubbleId.append(x["chatBubbleId"])
            except: self.chatBubbleId.append(None)
            try: self.clientRefId.append(x["clientRefId"])
            except: self.clientRefId.append(None)
            try: self.chatId.append(x["threadId"])
            except: self.chatId.append(None)
            try: self.messageType.append(x["messageType"])
            except: self.messageType.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.chatBubbleVersion.append(x["chatBubbleVersion"])
            except: self.chatBubbleVersion.append(None)
            try: self.type.append(x["type"])
            except: self.type.append(None)
            try: self.mediaValue.append(x["mediaValue"])
            except: self.mediaValue.append(None)
            try: self.mediaType.append(x["mediaType"])
            except: self.mediaType.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.duration.append(x["extensions"]["duration"])
            except: self.duration.append(None)
            try: self.originalStickerId.append(x["extensions"]["originalStickerId"])
            except: self.originalStickerId.append(None)
            try: self.mentionUserIds.append(x["extensions"]["mentionUserIds"])
            except: self.mentionUserIds.append(None)
            try: self.videoExtensions.append(x["extensions"]["videoExtensions"])
            except: self.videoExtensions.append(None)
            try: self.videoDuration.append(x["extensions"]["videoExtensions"]["duration"])
            except: self.videoDuration.append(None)
            try: self.videoHeight.append(x["extensions"]["videoExtensions"]["height"])
            except: self.videoHeight.append(None)
            try: self.videoWidth.append(x["extensions"]["videoExtensions"]["width"])
            except: self.videoWidth.append(None)
            try: self.videoCoverImage.append(x["extensions"]["videoExtensions"]["coverImage"])
            except: self.videoCoverImage.append(None)
            try: self.tippingCoins.append(x["extensions"]["tippingCoins"])
            except: self.tippingCoins.append(None)

        return self

class GetMessages:
    def __init__(self, data):
        self.json = data

        self.messageList = []
        self.nextPageToken = None
        self.prevPageToken = None

    @property
    def GetMessages(self):
        try: self.nextPageToken = self.json["paging"]["nextPageToken"]
        except: pass
        try: self.prevPageToken = self.json["paging"]["prevPageToken"]
        except: pass
        try: self.messageList = self.json["messageList"]
        except: pass

        return MessageList(self.messageList, self.nextPageToken, self.prevPageToken).MessageList

class CommunityStickerCollection:
    def __init__(self, data):
        self.json = data

        try: self.sticker: StickerCollectionList = StickerCollectionList(data["stickerCollectionList"]).StickerCollectionList
        except: self.sticker: StickerCollectionList = StickerCollectionList([])

        self.stickerCollectionCount = None

    @property
    def CommunityStickerCollection(self):
        try: self.stickerCollectionCount = self.json["stickerCollectionCount"]
        except: pass

        return self

class NotificationList:
    def __init__(self, data):
        _author = []

        self.json = data

        for y in data:
            try: _author.append(y["author"])
            except: _author.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.contextComId = []
        self.objectText = []
        self.objectType = []
        self.contextValue = []
        self.comId = []
        self.notificationId = []
        self.objectSubtype = []
        self.parentType = []
        self.createdTime = []
        self.parentId = []
        self.type = []
        self.contextText = []
        self.objectId = []
        self.parentText = []

    @property
    def NotificationList(self):
        for x in self.json:
            try: self.parentText.append(x["parentText"])
            except: self.parentText.append(None)
            try: self.objectId.append(x["objectId"])
            except: self.objectId.append(None)
            try: self.contextText.append(x["contextText"])
            except: self.contextText.append(None)
            try: self.type.append(x["type"])
            except: self.type.append(None)
            try: self.parentId.append(x["parentId"])
            except: self.parentId.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.parentType.append(x["parentType"])
            except: self.parentType.append(None)
            try: self.objectSubtype.append(x["objectSubtype"])
            except: self.objectSubtype.append(None)
            try: self.comId.append(x["ndcId"])
            except: self.comId.append(None)
            try: self.notificationId.append(x["notificationId"])
            except: self.notificationId.append(None)
            try: self.objectText.append(x["objectText"])
            except: self.objectText.append(None)
            try: self.contextValue.append(x["contextValue"])
            except: self.contextValue.append(None)
            try: self.contextComId.append(x["contextNdcId"])
            except: self.contextComId.append(None)
            try: self.objectType.append(x["objectType"])
            except: self.objectType.append(None)

        return self

class AdminLogList:
    def __init__(self, data):
        _author = []

        self.json = data

        for y in data:
            try: _author.append(y["author"])
            except: _author.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.createdTime = []
        self.objectType = []
        self.operationName = []
        self.comId = []
        self.referTicketId = []
        self.extData = []
        self.operationDetail = []
        self.operationLevel = []
        self.moderationLevel = []
        self.operation = []
        self.objectId = []
        self.logId = []
        self.objectUrl = []
        self.content = []
        self.value = []

    @property
    def AdminLogList(self):
        for x in self.json:
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.objectType.append(x["objectType"])
            except: self.objectType.append(None)
            try: self.operationName.append(x["operationName"])
            except: self.operationName.append(None)
            try: self.comId.append(x["ndcId"])
            except: self.comId.append(None)
            try: self.referTicketId.append(x["referTicketId"])
            except: self.referTicketId.append(None)
            try: self.extData.append(x["extData"])
            except: self.extData.append(None)
            try: self.content.append(x["extData"]["note"])
            except: self.content.append(None)
            try: self.value.append(x["extData"]["value"])
            except: self.value.append(None)
            try: self.operationDetail.append(x["operationDetail"])
            except: self.operationDetail.append(None)
            try: self.operationLevel.append(x["operationLevel"])
            except: self.operationLevel.append(None)
            try: self.moderationLevel.append(x["moderationLevel"])
            except: self.moderationLevel.append(None)
            try: self.operation.append(x["operation"])
            except: self.operation.append(None)
            try: self.objectId.append(x["objectId"])
            except: self.objectId.append(None)
            try: self.logId.append(x["logId"])
            except: self.logId.append(None)
            try: self.objectUrl.append(x["objectUrl"])
            except: self.objectUrl.append(None)

        return self

class LotteryLog:
    def __init__(self, data):
        self.json = data
        self.awardValue = None
        self.parentId = None
        self.parentType = None
        self.objectId = None
        self.objectType = None
        self.createdTime = None
        self.awardType = None
        self.refObject = None

    @property
    def LotteryLog(self):
        try: self.awardValue = self.json["awardValue"]
        except: pass
        try: self.parentId = self.json["parentId"]
        except: pass
        try: self.parentType = self.json["parentType"]
        except: pass
        try: self.objectId = self.json["objectId"]
        except: pass
        try: self.objectType = self.json["objectType"]
        except: pass
        try: self.createdTime = self.json["createdTime"]
        except: pass
        try: self.awardType = self.json["awardType"]
        except: pass
        try: self.refObject = self.json["refObject"]
        except: pass

        return self

class VcReputation:
    def __init__(self, data):
        self.json = data
        self.availableReputation = None
        self.maxReputation = None
        self.reputation = None
        self.participantCount = None
        self.totalReputation = None
        self.duration = None

    @property
    def VcReputation(self):
        try: self.availableReputation = self.json["availableReputation"]
        except: pass
        try: self.maxReputation = self.json["maxReputation"]
        except: pass
        try: self.reputation = self.json["reputation"]
        except: pass
        try: self.participantCount = self.json["participantCount"]
        except: pass
        try: self.totalReputation = self.json["totalReputation"]
        except: pass
        try: self.duration = self.json["duration"]
        except: pass

        return self

class FanClubList:
    def __init__(self, data):
        _profile, _targetUserProfile = [], []

        self.json = data

        for y in data:
            try: _profile.append(y["fansUserProfile"])
            except: _profile.append(None)
            try: _targetUserProfile.append(y["targetUserProfile"])
            except: _targetUserProfile.append(None)

        self.profile: UserProfileList = UserProfileList(_profile).UserProfileList
        self.targetUserProfile: UserProfileList = UserProfileList(_targetUserProfile).UserProfileList
        self.userId = []
        self.lastThankedTime = []
        self.expiredTime = []
        self.createdTime = []
        self.status = []
        self.targetUserId = []

    @property
    def FanClubList(self):
        for x in self.json:
            try: self.userId.append(x["uid"])
            except: self.userId.append(None)
            try: self.lastThankedTime.append(x["lastThankedTime"])
            except: self.lastThankedTime.append(None)
            try: self.expiredTime.append(x["expiredTime"])
            except: self.expiredTime.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.status.append(x["fansStatus"])
            except: self.status.append(None)
            try: self.targetUserId.append(x["targetUid"])
            except: self.targetUserId.append(None)

        return self

class InfluencerFans:
    def __init__(self, data):
        self.json = data

        try: self.influencerProfile: UserProfile = UserProfile(data["influencerUserProfile"]).UserProfile
        except: self.influencerProfile: UserProfile = UserProfile([])
        try: self.fanClubList: FanClubList = FanClubList(data["fanClubList"]).FanClubList
        except: self.fanClubList: FanClubList = FanClubList([])

        self.myFanClub = None

    @property
    def InfluencerFans(self):
        try: self.myFanClub = self.json["myFanClub"]
        except: pass

        return self

class QuizQuestionList:
    def __init__(self, data):
        _answersList = []

        self.json = data

        for y in data:
            try: _answersList.append(QuizAnswers(y["extensions"]["quizQuestionOptList"]).QuizAnswers)
            except: _answersList.append(None)

        self.status = []
        self.parentType = []
        self.title = []
        self.createdTime = []
        self.questionId = []
        self.parentId = []
        self.mediaList = []
        self.extensions = []
        self.style = []
        self.backgroundImage = []
        self.backgroundColor = []
        self.answerExplanation = []
        self.answersList = _answersList

    @property
    def QuizQuestionList(self):
        for x in self.json:
            try: self.status.append(x["status"])
            except: self.status.append(None)
            try: self.parentType.append(x["parentType"])
            except: self.parentType.append(None)
            try: self.title.append(x["title"])
            except: self.title.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.questionId.append(x["quizQuestionId"])
            except: self.questionId.append(None)
            try: self.parentId.append(x["parentId"])
            except: self.parentId.append(None)
            try: self.mediaList.append(x["mediaList"])
            except: self.mediaList.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.style.append(x["extensions"]["style"])
            except: self.style.append(None)
            try: self.backgroundImage.append(x["extensions"]["style"]["backgroundMediaList"][0][1])
            except: self.backgroundImage.append(None)
            try: self.backgroundColor.append(x["extensions"]["style"]["backgroundColor"])
            except: self.backgroundColor.append(None)
            try: self.answerExplanation.append(x["extensions"]["quizAnswerExplanation"])
            except: self.answerExplanation.append(None)

        return self

class QuizAnswers:
    def __init__(self, data):
        self.json = data
        self.answerId = []
        self.isCorrect = []
        self.mediaList = []
        self.title = []
        self.qhash = []

    @property
    def QuizAnswers(self):
        for x in self.json:
            try: self.answerId.append(x["optId"])
            except: self.answerId.append(None)
            try: self.qhash.append(x["qhash"])
            except: self.qhash.append(None)
            try: self.isCorrect.append(x["isCorrect"])
            except: self.isCorrect.append(None)
            try: self.mediaList.append(x["mediaList"])
            except: self.mediaList.append(None)
            try: self.title.append(x["title"])
            except: self.title.append(None)

        return self

class QuizRankings:
    def __init__(self, data):
        _rankingList = []

        self.json = data

        for y in data:
            try: _rankingList.append(QuizRanking(y["quizResultRankingList"]).QuizRanking)
            except: _rankingList.append(None)

        self.rankingList = _rankingList
        self.quizPlayedTimes = None
        self.quizInBestQuizzes = None
        self.profile: QuizRanking = QuizRanking([])

    @property
    def QuizRankings(self):
        try: self.quizPlayedTimes = self.json["quizPlayedTimes"]
        except: pass
        try: self.quizInBestQuizzes = self.json["quizInBestQuizzes"]
        except: pass
        try: self.profile: QuizRanking = QuizRanking(self.json["quizResultOfCurrentUser"]).QuizRanking
        except: pass

        return self

class QuizRanking:
    def __init__(self, data):
        self.json = data
        self.highestMode = None
        self.modifiedTime = None
        self.isFinished = None
        self.hellIsFinished = None
        self.highestScore = None
        self.beatRate = None
        self.lastBeatRate = None
        self.totalTimes = None
        self.latestScore = None
        self.latestMode = None
        self.createdTime = None

    @property
    def QuizRanking(self):
        try: self.highestMode = self.json["highestMode"]
        except: pass
        try: self.modifiedTime = self.json["modifiedTime"]
        except: pass
        try: self.isFinished = self.json["isFinished"]
        except: pass
        try: self.hellIsFinished = self.json["hellIsFinished"]
        except: pass
        try: self.highestScore = self.json["highestScore"]
        except: pass
        try: self.beatRate = self.json["beatRate"]
        except: pass
        try: self.lastBeatRate = self.json["lastBeatRate"]
        except: pass
        try: self.totalTimes = self.json["totalTimes"]
        except: pass
        try: self.latestScore = self.json["latestScore"]
        except: pass
        try: self.latestMode = self.json["latestMode"]
        except: pass
        try: self.createdTime = self.json["createdTime"]
        except: pass

        return self

class QuizRankingList:
    def __init__(self, data):
        _author = []

        self.json = data

        for y in data:
            try: _author.append(y["author"])
            except: _author.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.highestMode = []
        self.modifiedTime = []
        self.isFinished = []
        self.hellIsFinished = []
        self.highestScore = []
        self.beatRate = []
        self.lastBeatRate = []
        self.totalTimes = []
        self.latestScore = []
        self.latestMode = []
        self.createdTime = []

    @property
    def QuizRankingList(self):
        for x in self.json:
            try: self.highestMode.append(x["highestMode"])
            except: self.highestMode.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except: self.modifiedTime.append(None)
            try: self.isFinished.append(x["isFinished"])
            except: self.isFinished.append(None)
            try: self.hellIsFinished.append(x["hellIsFinished"])
            except: self.hellIsFinished.append(None)
            try: self.highestScore.append(x["highestScore"])
            except: self.highestScore.append(None)
            try: self.beatRate.append(x["beatRate"])
            except: self.beatRate.append(None)
            try: self.lastBeatRate.append(x["lastBeatRate"])
            except: self.lastBeatRate.append(None)
            try: self.totalTimes.append(x["totalTimes"])
            except: self.totalTimes.append(None)
            try: self.latestScore.append(x["latestScore"])
            except: self.latestScore.append(None)
            try: self.latestMode.append(x["latestMode"])
            except: self.latestMode.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)

        return self

class SharedFolderFile:
    def __init__(self, data):
        self.json = data

        try: self.author: UserProfile = UserProfile(data["author"]).UserProfile
        except: self.author: UserProfile = UserProfile([])

        self.votesCount = None
        self.createdTime = None
        self.modifiedTime = None
        self.extensions = None
        self.title = None
        self.media = None
        self.width = None
        self.height = None
        self.commentsCount = None
        self.fileType = None
        self.votedValue = None
        self.fileId = None
        self.comId = None
        self.status = None
        self.fileUrl = None
        self.mediaType = None

    @property
    def SharedFolderFile(self):
        try: self.votesCount = self.json["votesCount"]
        except: pass
        try: self.createdTime = self.json["createdTime"]
        except: pass
        try: self.modifiedTime = self.json["modifiedTime"]
        except: pass
        try: self.extensions = self.json["extensions"]
        except: pass
        try: self.width = self.json["width_hq"]
        except: pass
        try: self.height = self.json["height_hq"]
        except: pass
        try: self.title = self.json["title"]
        except: pass
        try: self.media = self.json["media"]
        except: pass
        try: self.mediaType = self.json["media"][0]
        except: pass
        try: self.fileUrl = self.json["media"][1]
        except: pass
        try: self.commentsCount = self.json["commentsCount"]
        except: pass
        try: self.fileType = self.json["fileType"]
        except: pass
        try: self.votedValue = self.json["votedValue"]
        except: pass
        try: self.fileId = self.json["fileId"]
        except: pass
        try: self.comId = self.json["ndcId"]
        except: pass
        try: self.status = self.json["status"]
        except: pass

        return self

class SharedFolderFileList:
    def __init__(self, data):
        _author = []

        self.json = data

        for y in data:
            try: _author.append(y["author"])
            except: _author.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.votesCount = []
        self.createdTime = []
        self.modifiedTime = []
        self.extensions = []
        self.title = []
        self.media = []
        self.width = []
        self.height = []
        self.commentsCount = []
        self.fileType = []
        self.votedValue = []
        self.fileId = []
        self.comId = []
        self.status = []
        self.fileUrl = []
        self.mediaType = []

    @property
    def SharedFolderFileList(self):
        for x in self.json:
            try: self.votesCount.append(x["votesCount"])
            except: self.votesCount.append(None)
            try: self.createdTime.append(x["createdTime"])
            except: self.createdTime.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except: self.modifiedTime.append(None)
            try: self.extensions.append(x["extensions"])
            except: self.extensions.append(None)
            try: self.width.append(x["width_hq"])
            except: self.width.append(None)
            try: self.height.append(x["height_hq"])
            except: self.height.append(None)
            try: self.title.append(x["title"])
            except: self.title.append(None)
            try: self.media.append(x["media"])
            except: self.media.append(None)
            try: self.mediaType.append(x["media"][0])
            except: self.mediaType.append(None)
            try: self.fileUrl.append(x["media"][1])
            except: self.fileUrl.append(None)
            try: self.commentsCount.append(x["commentsCount"])
            except: self.commentsCount.append(None)
            try: self.fileType.append(x["fileType"])
            except: self.fileType.append(None)
            try: self.votedValue.append(x["votedValue"])
            except: self.votedValue.append(None)
            try: self.fileId.append(x["fileId"])
            except: self.fileId.append(None)
            try: self.comId.append(x["ndcId"])
            except: self.comId.append(None)
            try: self.status.append(x["status"])
            except: self.status.append(None)

        return self

class Event:
    def __init__(self, data):
        self.json = data
        self.comId = None
        self.alertOption = None
        self.membershipStatus = None
        self.actions = None
        self.target = None
        self.params = None
        self.threadType = None
        self.id = None
        self.duration = None

        try: self.message: Message = Message(data["chatMessage"]).Message
        except: self.message: Message = Message([])

    @property
    def Event(self):
        try: self.comId = self.json["ndcId"]
        except: pass
        try: self.alertOption = self.json["alertOption"]
        except: pass
        try: self.membershipStatus = self.json["membershipStatus"]
        except: pass
        try: self.actions = self.json["actions"]
        except: pass
        try: self.target = self.json["target"]
        except: pass
        try: self.params = self.json["params"]
        except: pass
        try: self.threadType = self.json["params"]["threadType"]
        except: pass
        try: self.duration = self.json["params"]["duration"]
        except: pass
        try: self.id = self.json["id"]
        except: pass

        return self

class JoinRequest:
    def __init__(self, data):
        _author = []

        self.json = data

        for y in data["communityMembershipRequestList"]:
            try: _author.append(y)
            except: _author.append(None)

        self.author: UserProfileList = UserProfileList(_author).UserProfileList
        self.communityMembershipRequestCount = None

    @property
    def JoinRequest(self):
        try: self.communityMembershipRequestCount = self.json["communityMembershipRequestCount"]
        except: pass

        return self

class CommunityStats:
    def __init__(self, data):
        self.json = data
        self.dailyActiveMembers = None
        self.monthlyActiveMembers = None
        self.totalTimeSpent = None
        self.totalPostsCreated = None
        self.newMembersToday = None
        self.totalMembers = None

    @property
    def CommunityStats(self):
        try: self.dailyActiveMembers = self.json["dailyActiveMembers"]
        except: pass
        try: self.monthlyActiveMembers = self.json["monthlyActiveMembers"]
        except: pass
        try: self.totalTimeSpent = self.json["totalTimeSpent"]
        except: pass
        try: self.totalPostsCreated = self.json["totalPostsCreated"]
        except: pass
        try: self.newMembersToday = self.json["newMembersToday"]
        except: pass
        try: self.totalMembers = self.json["totalMembers"]
        except: pass

        return self
