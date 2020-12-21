'''

'''

class Header():
	def __init__(self, time,session):
		self.time = time
		self.session = session
		self.header = {
			"Host": "wechat.laixuanzuo.com",
			"Connection": "keep-alive",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116"
					  " Safari/537.36 QBCore/4.0.1219.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) "
					  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501"
					  " NetType/WIFI WindowsWechat",
			"Referer": "https://wechat.laixuanzuo.com/index.php/reserve/index.html",
			"Cookie": "wechatSESS_ID=" + session + "; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=" + str(time)+','+str(time+9000)+','+str(time+15000)+','+str(time+17000) + "; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=" + str(time+19000) + "",
		}

	def initPageIndex(self): # 首页

		return self.header

	def initPagePre(self): # 预定页面

		return self.header

	def initImage(self):
		self.header["Referer"] = "https://wechat.laixuanzuo.com/index.php/prereserve/index.html"
		print('get')
		return self.header

	def initBook(self,lib_id): # 订座
		self.header["Referer"] = "https://wechat.laixuanzuo.com/index.php/reserve/layoutApi/action=prereserve_event&libid="+lib_id
		return self.header

	def initGetNameVerify(self):
		header["Referer"] = "https://wechat.laixuanzuo.com/index.php/prereserve/index.html"
		return self.header

	def initImageWithName(self):
		self.header["Host"] = "static.wechat.laixuanzuo.com"
		return self.header

	def initBook_today(self):
		self.header["X-Requested-With"] = "XMLHttpRequest"
		self.header["Referer"] = "https://wechat.laixuanzuo.com/index.php/reserve/index.html?f=wechat"
		self.header["cookie"] = "wechatSESS_ID=%s; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098=%s; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098=%s"%(self.session,self.time,self.time+2000)
		return self.header

	def Feedback(self):
		header = {
			'Host': "wechat.laixuanzuo.com",
			"Connection": "keep-alive",
			"Cache-Control": "max-age=0",
			"X-Requested-With": "com.tencent.mm",
			"Sec-Fetch-Mode": "navigate",
			"Sec-Fetch-User": "?1",
			"Upgrade-Insecure-Requests": "1",
			"Sec-Fetch-Site": "same-origin",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116"
					  " Safari/537.36 QBCore/4.0.1219.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) "
					  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501"
					  " NetType/WIFI WindowsWechat",
			"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
			"Referer": "https://wechat.laixuanzuo.com/index.php/reserve/index.html",
			"Accept-Encoding": "gzip, deflate, br",
			"Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6",
			"Cookie": "wechatSESS_ID="+self.session+"; FROM_TYPE=weixin; Hm_lvt_7838cef374eb966ae9ff502c68d6f098="+str(self.time)+"; Hm_lpvt_7838cef374eb966ae9ff502c68d6f098="+str(self.time+1000)+"",
		}
		return header

if __name__ == '__main__':
	pass