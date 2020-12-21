pageCenter = 'http://wechat.laixuanzuo.com/index.php/center.html' # 个人中心

pageIndex = 'http://wechat.laixuanzuo.com/index.php/reserve/index.html?f=wechat' # 首页

pagePre = 'http://wechat.laixuanzuo.com/index.php/prereserve/index.html' # 预定页面

pageFeed = 'https://wechat.laixuanzuo.com/index.php/reserve/index.html' # 预定后返回页面

def pageBook(lib_id,seat_key,dynamic_varity,yzm='',method='book'):
	if method=='book':
	 	return "http://wechat.laixuanzuo.com/index.php/reserve/get/libid=%s&%s=%s&yzm=%s"%(lib_id,dynamic_varity,seat_key,yzm)
	else:
		return "http://wechat.laixuanzuo.com/index.php/prereserve/save/libid=%s&%s=%s&yzm=%s"%(lib_id,dynamic_varity,seat_key,yzm)

