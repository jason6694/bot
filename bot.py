# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
cl = LINE("boooooob456@gmail.com","Sonyxp456")
print ("======Master登入成功=====")
kicker01 = LINE("booooob456@gmail.com","Sonyxp456")
print ("======Kicker1登入成功=====")
kicker02 = LINE("a890128@icloud.com","Sonyxp456")
print ("======Kicker2登入成功=====")
kicker03 = LINE("jason6694@icloud.com","Sonyxp456")
print ("======Kicker3登入成功=====")
oepoll = OEPoll(cl)
channelToken = cl.getChannelResult()
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
clProfile = cl.getProfile()
clMID = cl.profile.mid
kicker01MID = kicker01.profile.mid
kicker02MID = kicker02.profile.mid
kicker03MID = kicker03.profile.mid
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
KAC = [kicker01,kicker02,kicker03]
master = ['u2d18b195540f5484316912e588829dda']
admin = ['u2d18b195540f5484316912e588829dda',clMID,kicker01MID,kicker02MID,kicker03MID]
msg_dict = {}
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
msg_dict = {}
bl = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """§指令表℅
《Help》幫助
§黑單指令℅
《BLACKLIST》查看黑名單-名字
《BLACKMID》查看黑名單-MID
《JBLACK @》加入黑單
《JMBLACK "mid"》加入黑單-MID
《CLEAR BLACKLIST》清空黑單
《UBLACK @》解除黑單
《UMBLACK "mid"》解除黑單-MID
§自動運行開關指令℅
《Autojoin On/Off》機器自動進群開啟/關閉
《Inviteptt On/Off》群組邀請保護開啟/關閉
《Urlptt On/Off》群組網址保護開啟/關閉
《Leave On/Off》自動離開副本開啟/關閉
《Groupsptt On/Off》群組保護開啟/關閉
《Add On/Off》自動加入好友開啟/關閉
《Contact On/Off》友資資訊開啟/關閉
§踢出指令℅
《MIDK “mid”》用MID踢出
《NK “name”》用名字踢出
《CLEANK @》踢出清除資料
《KBLACK》踢出黑單-單群
《KABLACK》踢出黑單-全群
《KICK @》用標注踢出
《Ri @》標注踢出重邀
§群組用指令℅
《MJOIN “mid”》MID邀請入群
《Url On/Off》群組網址開啟/關閉
《Tagall》全體標註 ＊請謹慎使用
《Group “name”》更改群組名稱
《Cancel》取消所有邀請
《Ginfo》群組詳細資料
《Gurl》 顯示群組網址
《Bot Join》防翻入群
《Bot Bye》防翻出群
《Gurl》群組網址
§其他指令℅
>自己
《Me》丟出自己好友資料
《MyMid》查看自己系統識別碼
《MyName》查看自己名字
《MyBio》查看自己個簽
《MyPicture》查看自己頭貼網址
《MyCover》查看自己封面網址
《Mid @》標註查看系統識別碼
《Picture @》標註查看頭貼
《user “mid”》識別碼查看友資
>權限
《Op》增加權限者
《Deop》刪除權限者
>狀態
《Runtime》運行時間查詢
《Rebot》運行速度查詢
《Speed》運行速度查詢
《About》狀態查詢
《Test》運行確認
《Set》目前狀態
>已讀
《Setread》《Sr》已讀設置
《Lookread》《Lr》已讀查看
⇛Create It By.承"""
    return helpMessage

def lineBot(op):
    try:
        if op.type == 0:
            return
        elif op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            if settings["qrprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)
                    invsend = 0
                    cl.sendMessage(op.param1,cl.getContact(op.param2).displayName + "！群組網址保護中 請勿觸碰網址開關！")
                    kicker02.kickoutFromGroup(op.param1,[op.param2])
        elif op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            print ("[☆] 邀請群組通知: " + str(group.name) + "\n邀請者: " + contact1.displayName + "\n被邀請者" + contact2.displayName)
            if settings["inviteprotect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1,[op.param3])
                    time.sleep(0.1)
                    kicker02.kickoutFromGroup(op.param1,[op.param3])
            if settings["autoJoin"] == True:
                if op.param2 in admin:
                    print ("[☆]進入群組: " + str(group.name))
                    cl.acceptGroupInvitation(op.param1)
                pass
        elif op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n被踢者" + contact2.displayName + "\nMid:" + contact2.mid )
            if settings["protect"] == True:
                if op.param2 in admin:
                    pass
                else:
                    if settings["kicktag"] == True:
                        klist = [kicker01,kicker02,kicker03]
                        kickers = random.choice(klist)
                        kickers.kickoutFromGroup(to,[target])
                        time.sleep(0.1)
                        cl.sendMessage(op.param1,"《被踢者》")
                        cl.sendContact(op.param1,op.param3)
                    else:
                        klist = [kicker01,kicker02,kicker03]
                        kickers = random.choice(klist)
                        kickers.kickoutFromGroup(to,[target])
                        time.sleep(0.1)
            else:
                if settings["kicktag"] == True:
                    cl.sendMessage(op.param1,"《被踢者》")
                    cl.sendContact(op.param1,op.param3)
                else:
                    pass
            if clMID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker01MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker02.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker02.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker02.updateGroup(G)
                    invsend = 0
                    Ti = kicker02.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker02MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker03.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker03.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker03.updateGroup(G)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker03MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker03.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
        elif op.type == 24:
            print ("[ LEAVE ] 通知離開副本")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        elif op.type in [25,26]:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            
            #收回記錄
            try:
                if settings["reread"] == True and op.type == 26:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
            #收回記錄end
            
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
            elif msg.contentType == 13:
                if settings["contact"] == True:
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = "\n《封面網址》:\n" + cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"《顯示名稱》:\n" + msg.contentMetadata['displayName'] + "\n《mid》:\n" + msg.contentMetadata["mid"] + "\n《圖片網址》:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = "\n《封面網址》:\n" + cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"《顯示名稱》:\n" + contact.displayName + "\n《mid》:\n" + msg.contentMetadata["mid"] + "\n《圖片網址》:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "《文章網址》\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendMessage(msg.to,msg.text)
            elif msg.contentType == 7:
               if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "《貼圖資料》"
                    ret_ += "\n貼圖ID : {}".format(stk_id)
                    ret_ += "\n貼圖包ID : {}".format(pkg_id)
                    ret_ += "\n貼圖網址 : https://stickershop.line-scdn.net/stickershop/v1/sticker/{}".format(stk_id)
                    ret_ += "/ANDROID/sticker.png"
                    cl.sendMessage(to, str(ret_))
            if sender in admin:
                if msg.text in ["help","Help"]:
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    kicker01.sendContact(to, "u2d18b195540f5484316912e588829dda")
                    kicker02.sendMessage(to, '⇛Create it By.Ge™⇚')
                    kicker03.sendMessage(to, '⇛Made in Taiwan⇚')
                elif text.lower() == 'bot bye':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        try:
                            kicker01.leaveGroup(to)
                            kicker02.leaveGroup(to)
                            kicker03.leaveGroup(to)
                        except:
                            pass
                elif text.lower() == 'bot join':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker01.acceptGroupInvitationByTicket(to, Ti)
                            kicker02.acceptGroupInvitationByTicket(to, Ti)
                            kicker03.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker01.acceptGroupInvitationByTicket(to, Ti)
                            kicker02.acceptGroupInvitationByTicket(to, Ti)
                            kicker03.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                elif text.lower() == 'bot1 join':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker01.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker01.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                elif text.lower() == 'bot2 join':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker02.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker02.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                elif text.lower() == 'bot3 join':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker03.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker03.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                elif text.lower() == 'test':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=5000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'《處理速度》\n' + str1 + '秒')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'《指令反應》\n' + format(str(elapsed_time)) + '秒')
                    kicker01.sendMessage(to, '《運行確認》')
                    kicker02.sendMessage(to, '《運行確認》')
                    kicker03.sendMessage(to, '《運行確認》')
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "《重新啟動中》")
                    restartBot()
                elif "KICK " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in master:
                            pass
                        else:
                            try:
                                klist = [kicker01,kicker02,kicker03]
                                kickers = random.choice(klist)
                                kickers.kickoutFromGroup(to,[target])
                                time.sleep(0.1)
                            except:
                                pass
                elif text.lower().startswith('op '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.append(str(inkey))
                    kicker01.sendMessage(to,'《成功加入權限者》')
                elif text.lower().startswith('deop '):
                    MENTION = eval(msg.contentMetadata['MENTION'])
                    inkey = MENTION['MENTIONEES'][0]['M']
                    admin.remove(str(inkey))
                    kicker01.sendMessage(to,'《成功刪除權限者》')
                elif "Gn " in msg.text:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                        cl.sendMessage(msg.to,"《群組名稱已更改》")
                    else:
                        cl.sendMessage(msg.to,"《無法使用在群組外》")
                elif "MJOIN " in msg.text:
                    midd = msg.text.replace("MJOIN ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                elif "MIDK " in msg.text:
                    midd = text.replace("MIDK ","")
                    kicker01.kickoutFromGroup(to,[midd])
                elif "NK " in msg.text:
                    _name = text.replace("NK ","")
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in master:
                                pass
                            else:
                                try:
                                    kicker02.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif "CLEANK " in msg.text:
                        vkick0 = msg.text.replace("CLEANK ","")
                        vkick1 = vkick0.rstrip()
                        vkick2 = vkick1.replace("@","")
                        vkick3 = vkick2.rstrip()
                        _name = vkick3
                        gs = kicker03.getGroup(msg.to)
                        targets = []
                        for s in gs.members:
                            if _name in s.displayName:
                                targets.append(s.mid)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    kicker03.kickoutFromGroup(msg.to,[target])
                                    kicker03.findAndAddContactsByMid(target)
                                    kicker03.inviteIntoGroup(msg.to,[target])
                                    kicker03.cancelGroupInvitation(msg.to,[target])
                                except:
                                    pass
                elif "Ri " in msg.text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    kicker03.kickoutFromGroup(to,[target])
                                    kicker03.findAndAddContactsByMid(target)
                                    kicker03.inviteIntoGroup(to,[target])
                                except:
                                    pass
                elif msg.text in ["Sr","SR","Setread"]:
                    cl.sendMessage(msg.to, "《已讀設置》")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.tor
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                elif msg.text in ["Lr","LR","Lookread"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "《已讀的人》%s\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "《還沒設定已讀點哦¨》")
                elif msg.text in ["cancel","Cancel","c","C"]:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "《已取消所有邀請，費時%s秒》" % (elapsed_time))
                        cl.sendMessage(to, "" )
                    else:
                        cl.sendMessage(to, "《沒有邀請可以取消》")
                elif "user " in msg.text:
                    mmid = msg.text.replace("user ","")
                    cl.sendContact(to, mmid)
                elif "JBLACK @" in msg.text:
                    if msg.toType == 2:
                        print ("[Ban] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    cl.sendMessage(to, "《加入黑名單》")
                                except:
                                    pass
                elif "JMBLACK " in msg.text:
                    mmid = msg.text.replace("JMBLACK ","")
                    try:
                        settings["blacklist"][mmid] = True
                        cl.sendMessage(to, "《加入黑名單》")
                    except:
                        pass
                elif "UMBLACK " in msg.text:
                    mmid = msg.text.replace("UMBLACK ","")
                    try:
                        settings["blacklist"][mmid] = True
                        cl.sendMessage(to, "《解除黑名單》")
                    except:
                        pass
                elif "UBLACK @" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    cl.sendMessage(to, "《解除黑名單》")
                                except:
                                    pass
                elif msg.text in ["Clear BLACKLIST"]:
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    cl.sendMessage(to, "《清空黑名單》")
                elif msg.text in ["BLACKLIST"]:
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "《沒有黑名單》")
                    else:
                        cl.sendMessage(to, "《以下是黑名單》")
                        mc = ""
                        for mi_d in settings["blacklist"]:
                            mc += "》" + cl.getContact(mi_d).displayName + "\n"
                        cl.sendMessage(to, mc)
                elif msg.text in ["BLACKMID"]:
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "《沒有黑名單》")
                    else:
                        cl.sendMessage(to, "《以下是黑名單》")
                        mc = ""
                        for mi_d in settings["blacklist"]:
                            mc += "》" + mi_d + "\n"
                        cl.sendMessage(to, mc)
                elif msg.text in ["KBLACK"]:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            cl.sendMessage(to, "《沒有黑名單》")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "《黑名單已清除》")
                elif msg.text in ["KABLACK"]:
                    gid = cl.getGroupIdsJoined()
                    group = cl.getGroup(to)
                    gMembMids = [contact.mid for contact in group.members]
                    ban_list = []
                    for tag in settings["blacklist"]:
                        ban_list += filter(lambda str: str == tag, gMembMids)
                    if ban_list == []:
                        cl.sendMessage(to, "《沒有黑名單》")
                    else:
                        for i in gid:
                            for jj in ban_list:
                                cl.kickoutFromGroup(i, [jj])
                            cl.sendMessage(i, "《已清除所有群組黑單對象》")
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    cl.sendContact(to, sender)
                elif text.lower() == 'mymid':
                    cl.sendMessage(msg.to,"《MID》\n" +  sender)
                elif text.lower() == 'myname':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"《顯示名稱》\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = cl.getContact(sender)
                    cl.sendMessage(msg.to,"《狀態消息》\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                    me = cl.getContact(sender)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                    me = cl.getContact(sender)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = cl.getContact(sender)
                    cover = cl.getProfileCoverURL(sender)
                    cl.sendImageWithURL(msg.to, cover)
                elif msg.text in ["speed","Speed"]:
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'《處理速度》\n' + str1 + '秒')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'《指令反應》\n' + format(str(elapsed_time)) + '秒')
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "《機器運行時間 {}》".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u2d18b195540f5484316912e588829dda"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "《關於自己》"
                        ret_ += "\n版本 : v3.7.0"
                        ret_ += "\n名稱 : {}".format(contact.displayName)
                        ret_ += "\n群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n好友 : {}".format(str(len(contactlist)))
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif msg.text in ["set","Set"]:
                    try:
                        ret_ = "《設定》"
                        if settings["autoJoin"] == True: ret_ += "\n自動加入群組 🆗"
                        else: ret_ += "\n自動加入群組 🈲"
                        if settings["autoAdd"] == True: ret_ += "\n自動加入好友 🆗"
                        else: ret_ += "\n自動加入好友 🈲"
                        if settings["autoLeave"] == True: ret_ += "\n自動離開副本 🆗"
                        else: ret_ += "\n自動離開副本 🈲"
                        if settings["reread"] == True: ret_ += "\n查詢收回 🆗"
                        else: ret_ += "\n查詢收回 🈲"
                        if settings["inviteprotect"] == True: ret_ += "\n邀請保護 🆗"
                        else: ret_ += "\n邀請保護 🈲"
                        if settings["qrprotect"] == True: ret_ += "\n網址保護 🆗"
                        else: ret_ += "\n網址保護 🈲"
                        if settings["protect"] == True: ret_ += "\n群組保護 🆗"
                        else: ret_ += "\n群組保護 🈲"
                        if settings["contact"] == True: ret_ += "\n友資資訊 🆗"
                        else: ret_ += "\n友資資訊 🈲"
                        if settings["checkSticker"] == True: ret_+= "\n貼圖查詢 🆗"
                        else:ret_ += "\n貼圖查詢 🈲"
                        if settings["kicktag"] == True: ret_+= "\n被踢者查詢 🆗"
                        else:ret_ += "\n被踢者查詢 🈲"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif msg.text in ["kicktag On","Kicktag On"]:
                    settings["kicktag"] = True
                    cl.sendMessage(to, "《被踢者標注已開啟》")
                elif msg.text in ["kicktag Off","Kicktag Off"]:
                    settings["kicktag"] = False
                    cl.sendMessage(to, "《被踢者標注已關閉》")
                elif msg.text in ["autojoin On","Autojoin On"]:
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "《自動加入群組已開啟》")
                elif msg.text in ["autojoin Off","Autojoin Off"]:
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "《自動加入群組已關閉》")
                elif msg.text in ["leave On","Leave On"]:
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "《自動離開副本已開啟》")
                elif msg.text in ["leave Off","Leave Off"]:
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "《自動離開副本已關閉》")
                elif msg.text in ["add On","Add On"]:
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "《自動加入好友已開啟》")
                elif msg.text in ["add Off","Add Off"]:
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "《自動加入好友已關閉》")
                elif msg.text in ["inviteptt On","Inviteptt On"]:
                    settings["inviteprotect"] = True
                    cl.sendMessage(to, "《群組邀請保護已開啟》")
                elif msg.text in ["inviteptt Off","Inviteptt Off"]:
                    settings["inviteprotect"] = False
                    cl.sendMessage(to, "《群組邀請保護已關閉》")
                elif msg.text in ["URLptt On"]:
                    settings["qrprotect"] = True
                    cl.sendMessage(to, "《群組網址保護已開啟》")
                elif msg.text in ["URLptt Off"]:
                    settings["qrprotect"] = False
                    cl.sendMessage(to, "《群組網址保護已關閉》")
                elif msg.text in ["groupsptt On","Groupsptt On"]:
                    settings["protect"] = True
                    cl.sendMessage(to, "《群組保護已開啟》")
                elif msg.text in ["groupsptt Off","Groupsptt Off"]:
                    settings["protect"] = False
                    cl.sendMessage(to, "《群組保護已關閉》")
                elif msg.text in ["contact On","Contact On"]:
                    settings["contact"] = True
                    cl.sendMessage(to, "《友資資訊已開啟》")
                elif msg.text in ["contact Off","Contact Off"]:
                    settings["contact"] = False
                    cl.sendMessage(to, "《友資資訊已關閉》")
                elif msg.text in ["reread On","Reread On"]:
                    settings["reread"] = True
                    cl.sendMessage(to, "《查詢收回已開啟》")
                elif msg.text in ["reread Off","Reread Off"]:
                    settings["reread"] = False
                    cl.sendMessage(to, "《查詢收回已關閉》")
                elif msg.text in ["Sticker On","sticker On"]:
                    settings["checkSticker"] = True
                    cl.sendMessage(to, "《貼圖查詢已開啟》")
                elif msg.text in ["Sticker Off","sticker Off"]:
                    settings["checkSticker"] = False
                    cl.sendMessage(to, "《貼圖查詢已關閉》")
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("picture "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line-cdn.net/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text in ["Grl","grl"]:
                        groups = cl.groups
                        ret_ = "《群組列表 》"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n☆ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n《總共 {} 個群組 》".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif msg.text in ["Gurl","gurl"]:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "《群組網址》\nhttp://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "《群組網址未開啟》".format(str(settings["keyCommand"])))
                elif msg.text in ["URL On"]:
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "《群組網址已開啟》")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "《成功開啟群組網址》")
                elif msg.text in ["URL Off"]:
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "《群組網址已關閉》")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "《成功關閉群組網址》")
                elif msg.text in ["Ginfo","ginfo"]:
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "未找到"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "沒有"
                    else:
                        gQr = "開啟"
                        gTicket = "http://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "《群組資料 》"
                    ret_ += "\n顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n群組ＩＤ : {}".format(group.id)
                    ret_ += "\n群組作者 : {}".format(str(gCreator))
                    ret_ += "\n成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n邀請數量 : {}".format(gPending)
                    ret_ += "\n群組網址 : {}".format(gQr)
                    ret_ += "\n群組網址 : {}".format(gTicket)
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif msg.text in ["Tagall","tagall"]:
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "《總共 {} 個成員》".format(str(len(nama))))
        elif op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n☆" + Name
                        wait2['ROM'][op.param1][op.param2] = "☆" + Name
                else:
                    pass
            except:
                pass
        elif op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            kicker01.sendMessage(at,"《收回訊息者》\n%s\n《訊息內容》\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)