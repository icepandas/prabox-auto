import wda
import time
import threading
import sched  
bundle_id = 'pro.chain.wallet'
c = wda.Client('http://localhost:8100')
s = c.session(bundle_id)
schedule = sched.scheduler(time.time, time.sleep) 
def f():
	s(name='可领取').click_exists()
	s.swipe(129,232,129,540,0.5)
	# s.tap(20,93)
	s(name='去生产').click_exists()
def f2():
	s.swipe(129,600,129,205,0.5)		
	s(name='可领取').click_exists()
	# s.tap(20,93)          			
	s.swipe(129,219,129,700,0.5) 
	s.swipe(129,232,129,540,0.5) 
	s.swipe(129,600,129,205,0.5) 
	s(name='去生产').click_exists()
	s.swipe(129,219,129,700,0.5)
def get():
	print(time.asctime( time.localtime(time.time()) ))
	schedule.enter(300, 0, get, ()) 
	s.swipe(129,600,129,205,1)
	i=int(len(s(name='可领取',className='Button').find_elements()))
	s.swipe(129,205,129,700,0.5)
	for x in range(1,4):
		if s(name='可领取').exists:
			f()
			pass
		pass
	for x in range(0,i):
		f2()
		pass
def main_start():  
    schedule.enter(0, 0, get, ())  
    schedule.run()  
  
main_start()  


















