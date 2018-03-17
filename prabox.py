import wda
import time
import threading
import sched

bundle_id = 'pro.chain.wallet'
c = wda.Client('http://localhost:8100')
s = c.session(bundle_id)

schedule = sched.scheduler(time.time, time.sleep)
def get():
	while s(name='可领取').exists:
		s(name='可领取',className='Button').click_exists()
		s.tap(0,44) 
	pass

def send():
	while s(name='去生产').exists:
		s(name='去生产',className='Button').click_exists()
	pass
def back():
	s.swipe(129,219,129,700,0.5)
	s.swipe(129,232,129,540,0.5) 
	pass

def do():
	print(time.asctime( time.localtime(time.time()) ))
	schedule.enter(600, 0, do, ()) # 10分钟
	get()
	print("第一页领取完毕")
	s.swipe(129,600,129,205,1)
	get()
	print("第二页领取完毕")
	back()
	send()
	print("第一页生产完毕")
	s.swipe(129,600,129,205,0.5) 
	print("返回第二页")
	send()
	print("第二页生产完毕")
	back()
	pass
def main():  
    schedule.enter(0, 0, do, ())  
    schedule.run()
main()

	
















