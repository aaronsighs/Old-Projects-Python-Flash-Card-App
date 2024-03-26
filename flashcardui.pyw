### py flash_card

import pygame
from pygame.locals import *
import json
import os
import random
import time




def box_loc(box):
	return (box[0]+20,box[1])
def font_text_color(text,color,size):
	font = pygame.font.Font(None, size)
	return font.render(str(text),True, color)

def wrap_text_color_size(screen,text,loc,color,size):
	org_loc = loc
	x = loc[0]
	y = loc[1]
	text = text.split()
	for word in text:
		a = screen.blit(font_text_color(word,color,size),(x,y))
		if x+a.width < 515: 
			x = a[0]+a.width+5
		else: 
			y = y+18
			x = loc[0]


def wrap_text(screen,text,loc):
	org_loc = loc
	x = loc[0]
	y = loc[1]
	text = text.split()
	for word in text:
		a = screen.blit(font_text_color(word,(5,5,5),22),(x,y))
		if x+a.width < 515: 
			x = a[0]+a.width+5
		else: 
			y = y+18
			x = loc[0]
	
def on_box(box,position):
		if (position[0] >= box.x and position[0] <=box.x+box.width) and (position[1] >= box.y and position[1] <=box.y+box.height):
			return True
		return False
def center_text(screen,text,size,color,clear,height):
	font = pygame.font.Font(None,20)
	a = screen.blit(font_text_color(text,(240,240,240),size),(0,0))
	if clear ==1:erase = pygame.draw.rect(screen,(240,240,240), pygame.Rect(0,0,600,80))
	center_x = 300-(a.width/2)
	b = screen.blit(font_text_color(text,(color),size),(center_x,height))
	
def draw_check_box(screen,loc,state):
	border= pygame.draw.rect(screen,(0,0,0), pygame.Rect(loc[0],loc[1],13,13))
	backround = pygame.draw.rect(screen,(255,255,255), pygame.Rect(loc[0]+1,loc[1]+1,11,11))
	if state==1:
		fill_in = pygame.draw.rect(screen,(0,0,0), pygame.Rect(loc[0]+2,loc[1]+2,9,9))
	return backround
	
def check_box(click,location):
	box = draw_check_box(location,click)
	for event in pygame.event.get():
		pos = pygame.mouse.get_pos()
		if event.type == MOUSEBUTTONDOWN and on_box(box,pos) and click==0:
			click = 1
		elif event.type == MOUSEBUTTONDOWN and on_box(box,pos) and click==1:
			click = 0
	return click

def run():
	pygame.font.init()		
	white = (240,240,240)
	teal = (0,20,100)
	green = (0,200,20)	
	width, height = 620,520
	screen = pygame.display.set_mode((width,height))
	cwd = os.getcwd()
	#try:
	Files = json.load(open(cwd+"/Data/filenames.txt"))
	#except FileNotFoundError: exit()
	File = cwd+'/Files/'+Files["1"]
	pygame.display.set_caption("Flash Cards------>> "+Files["1"])
	screen.fill(white)
	pygame.display.flip()
	done = False
	pos = [0,0]
	c = [15,80]
	active = True
	wrong_count,correct_count = 0,0
	loop=-1
	fc = json.load(open(File))
	keys = list(fc.keys())
	length = len(fc)
	called = []
	while len(called)<length:
		done = False
		list_q = []
		c1,c2,c3,c4=0,0,0,0
		number = random.randint(0,length-1)
		if number not in called:
			called.append(number)
			if len(fc)<4: q_amt = len(fc)
			else: q_amt = 4
			while len(list_q)< q_amt-1:
				for key in keys:
					if key != keys[number] and key not in list_q and random.randint(0,random.randint(2,10))==1 and len(list_q)!= q_amt-1:
						list_q.append(key)
			list_q.append(keys[number])
			random.shuffle(list_q)
			def_or_ans = random.randint(0,random.randint(1,3))
			if def_or_ans<=1: dif,dis = 0,120
			else: dif,dis = 40,80
			while not done:
				screen.fill(white)
				if len(list_q)>=1:cbox1 = draw_check_box(screen,(c[0],c[1]+dif),c1)
				if len(list_q)>=2:cbox2 = draw_check_box(screen,(c[0],c[1]+dis+dif),c2)
				if len(list_q)>=3:cbox3 = draw_check_box(screen,(c[0],c[1]+dis*2+dif),c3)
				if len(list_q)>=4:cbox4 = draw_check_box(screen,(c[0],c[1]+dis*3+dif),c4)
				if len(list_q)>=1:cbox_all = [cbox1]
				if len(list_q)>=2:cbox_all = [cbox1,cbox2]
				if len(list_q)>=3:cbox_all = [cbox1,cbox2,cbox3]
				if len(list_q)==4:cbox_all = [cbox1,cbox2,cbox3,cbox4]
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						done = True
						length = 0
					pos = pygame.mouse.get_pos()
					if len(list_q)>=1 and event.type == MOUSEBUTTONDOWN and on_box(cbox1,pos) and c1==0:
						c1,c2,c3,c4 = 1,0,0,0
					elif len(list_q)>=1 and event.type == MOUSEBUTTONDOWN and on_box(cbox1,pos) and c1==1:
						c1 = 0
					if len(list_q)>=2 and event.type == MOUSEBUTTONDOWN and on_box(cbox2,pos) and c2==0:
						c1,c2,c3,c4 = 0,1,0,0
					elif len(list_q)>=2 and event.type == MOUSEBUTTONDOWN and on_box(cbox2,pos) and c2==1:
						c2 = 0
					if len(list_q)>=3 and event.type == MOUSEBUTTONDOWN and on_box(cbox3,pos) and c3==0:
						c1,c2,c3,c4 = 0,0,1,0
					elif len(list_q)>=3 and event.type == MOUSEBUTTONDOWN and on_box(cbox3,pos) and c3==1:
						c3 = 0
					if len(list_q)>=4 and event.type == MOUSEBUTTONDOWN and on_box(cbox4,pos) and c4==0:
						c1,c2,c3,c4 = 0,0,0,1
					elif  len(list_q)>=4 and event.type == MOUSEBUTTONDOWN and on_box(cbox4,pos) and c4==1:
						c4 = 0
						
						
				if def_or_ans<=1:topic = center_text(screen,keys[number],40,teal,0,20)
				else:
					topic = wrap_text_color_size(screen,fc[keys[number]],(20,15),teal,26)
				c_all = [c1,c2,c3,c4]
				
				if len(list_q)>=1 and def_or_ans<=1: one = fc[list_q[0]]
				elif len(list_q)>=1 and def_or_ans>=2: one = list_q[0]
				
				if len(list_q)>=2 and def_or_ans<=1: two = fc[list_q[1]]
				elif len(list_q)>=2 and def_or_ans>=2: two = list_q[1]
				
				if len(list_q)>=3 and def_or_ans<=1: three = fc[list_q[2]]
				elif len(list_q)>=3 and def_or_ans>=2: three = list_q[2]
				
				if len(list_q)>=4 and def_or_ans<=1: four = fc[list_q[3]]
				elif len(list_q)>=4 and def_or_ans>=2: four = list_q[3]
				
				if len(list_q)>=1 and def_or_ans<=1:wrap_text(screen,one,box_loc(cbox1))
				elif len(list_q)>=1: wrap_text_color_size(screen,one,box_loc(cbox1),(5,5,5),23)
				
				if len(list_q)>=2 and def_or_ans<=1:wrap_text(screen,two,box_loc(cbox2))
				elif len(list_q)>=2: wrap_text_color_size(screen,two,box_loc(cbox2),(5,5,5),23)
				
				if len(list_q)>=3 and def_or_ans<=1:wrap_text(screen,three,box_loc(cbox3))
				elif len(list_q)>=3: wrap_text_color_size(screen,three,box_loc(cbox3),(5,5,5),23)
				
				if len(list_q)>=4 and def_or_ans<=1:wrap_text(screen,four,box_loc(cbox4))
				elif len(list_q)>=4: wrap_text_color_size(screen,four,box_loc(cbox4),(5,5,5),23)
				

				pygame.display.flip()
				
				
				
					
				if c1 == 1 and (list_q[0] == keys[number]): 
					done = True
					cbox1 = draw_check_box(screen,(c[0],c[1]+dif),c1)
					center_text(screen,"Correct!!!",40,green,1,20)
					correct_count +=1
					pygame.display.flip()	
					time.sleep(.5)
				elif c2 == 1 and list_q[1] == keys[number]: 
					done = True
					cbox2 = draw_check_box(screen,(c[0],c[1]+dis+dif),c2)
					center_text(screen,"Correct!!!",40,green,1,20)
					correct_count +=1
					pygame.display.flip()	
					time.sleep(.5)
				elif c3 == 1 and list_q[2] == keys[number]:
					done = True
					cbox3 = draw_check_box(screen,(c[0],c[1]+dis*2+dif),c3)
					correct_count +=1
					center_text(screen,"Correct!!!",40,green,1,20)
					pygame.display.flip()	
					time.sleep(.5)
				elif c4 == 1 and list_q[3] == keys[number]:
					done = True
					cbox4 = draw_check_box(screen,(c[0],c[1]+dis*3+dif),c4)
					correct_count +=1
					center_text(screen,"Correct!!!",40,green,1,20)
					pygame.display.flip()	
					time.sleep(.5)
				elif 1 in c_all:
					loop+=1
					for s in c_all:
						if s==1 and loop == 1: 
							center_text(screen,"Wrong!!!",40,(200,0,50),1,20)
							wrong_count +=1
							pygame.display.flip()
							time.sleep(.5)
							done=True
							loop =-1
	screen.fill(white)	
	score = center_text(screen,"Score:::",40,teal,0,20)
	score = center_text(screen,"Correct:::",40,green,0,125)
	score = center_text(screen,str(correct_count),40,(0,0,0),0,170)
	score = center_text(screen,"Wrong:::",40,(200,0,50),0,250)
	score = center_text(screen,str(wrong_count),40,(0,0,0),0,295)
	pygame.display.flip()
	wait = True
	while wait:
		if event.type == pygame.QUIT: 
			time.sleep(.75)
			wait = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				wait = False
	pygame.quit()

