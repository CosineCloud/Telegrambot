{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset204 PTMono-Bold;\f1\fnil\fcharset204 PTMono-Regular;}
{\colortbl;\red255\green255\blue255;\red222\green53\blue46;\red242\green242\blue242;\red52\green52\blue52;
\red117\green117\blue117;\red228\green143\blue83;\red43\green132\blue210;\red115\green0\blue2;\red102\green155\blue78;
}
{\*\expandedcolortbl;;\cssrgb\c90588\c29804\c23529;\cssrgb\c96078\c96078\c96078;\cssrgb\c26667\c26667\c26667;
\cssrgb\c53333\c53333\c53333;\cssrgb\c92157\c63137\c39608;\cssrgb\c20392\c59608\c85882;\cssrgb\c53333\c0\c0;\cssrgb\c47059\c66275\c37647;
}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\b\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
import
\f1\b0 \cf4  datetime  \cf5 # Importing the datetime library\cf4 \

\f0\b \cf2 import
\f1\b0 \cf4  telepot   \cf5 # Importing the telepot library\cf4 \

\f0\b \cf2 from
\f1\b0 \cf4  telepot.loop 
\f0\b \cf2 import
\f1\b0 \cf4  MessageLoop    \cf5 # Library function to communicate with telegram bot\cf4 \

\f0\b \cf2 import
\f1\b0 \cf4  RPi.GPIO 
\f0\b \cf2 as
\f1\b0 \cf4  GPIO     \cf5 # Importing the GPIO library to use the GPIO pins of Raspberry pi\cf4 \

\f0\b \cf2 from
\f1\b0 \cf4  time 
\f0\b \cf2 import
\f1\b0 \cf4  sleep      \cf5 # Importing the time library to provide the delays in program\cf4 \
\
red_led_pin = \cf6 21\cf4                 \cf5 # Initializing GPIO 21 for red led\cf4 \
green_led_pin = \cf6 20\cf4                 \cf5 # Initializing GPIO 20 for green led\cf4 \
\
GPIO.setmode(GPIO.BCM)      \cf5 # Use Board pin numbering\cf4 \
GPIO.setup(red_led_pin, GPIO.OUT) \cf5 # Declaring the GPIO 21 as output pin\cf4 \
GPIO.setup(green_led_pin, GPIO.OUT) \cf5 # Declaring the GPIO 20 as output pin\cf4 \
\
now = datetime.datetime.now() \cf5 # Getting date and time\cf4 \
\

\f0\b \cf2 def
\f1\b0 \cf4  
\f0\b \cf7 handle
\f1\b0 \cf8 (msg)\cf4 :\
    chat_id = msg[\cf6 'chat'\cf4 ][\cf6 'id'\cf4 ] \cf5 # Receiving the message from telegram\cf4 \
    command = msg[\cf6 'text'\cf4 ]   \cf5 # Getting text from the message\cf4 \
\
    
\f0\b \cf2 print
\f1\b0 \cf4  (\cf6 'Received:'\cf4 )\
    print(command)\
\
    \cf5 # Comparing the incoming message to send a reply according to it\cf4 \
    
\f0\b \cf2 if
\f1\b0 \cf4  command == \cf6 '/hi'\cf4 :\
        bot.sendMessage (chat_id, str(\cf6 "Hi! This Gotech bot\'94\cf4 ))\
    
\f0\b \cf2 elif
\f1\b0 \cf4  command == \cf6 '/time'\cf4 :\
        bot.sendMessage(chat_id, str(\cf6 "Time: "\cf4 ) + str(now.hour) + str(\cf6 ":"\cf4 ) + str(now.minute) + str(\cf6 ":"\cf4 ) + str(now.second))\
    
\f0\b \cf2 elif
\f1\b0 \cf4  command == \cf6 '/date'\cf4 :\
        bot.sendMessage(chat_id, str(\cf6 "Date: "\cf4 ) + str(now.day) + str(\cf6 "/"\cf4 ) + str(now.month) + str(\cf6 "/"\cf4 ) + str(now.year))\
    
\f0\b \cf2 elif
\f1\b0 \cf4  command == \cf6 '/red_1'\cf4 :\
        bot.sendMessage(chat_id, str(\cf6 "Red led is ON"\cf4 ))\
        GPIO.output(red_led_pin, \cf9 True\cf4 )\
    
\f0\b \cf2 elif
\f1\b0 \cf4  command == \cf6 '/red_0'\cf4 :\
        bot.sendMessage(chat_id, str(\cf6 "Red led is OFF"\cf4 ))\
        GPIO.output(red_led_pin, \cf9 False\cf4 )\
    
\f0\b \cf2 elif
\f1\b0 \cf4  command == \cf6 '/green_1'\cf4 :\
        bot.sendMessage(chat_id, str(\cf6 "Green led is ON"\cf4 ))\
        GPIO.output(green_led_pin, \cf9 True\cf4 )\
    
\f0\b \cf2 elif
\f1\b0 \cf4  command == \cf6 '/green_0'\cf4 :\
        bot.sendMessage(chat_id, str(\cf6 "Green led is OFF"\cf4 ))\
        GPIO.output(green_led_pin, \cf9 False\cf4 )\
\
\cf5 # Insert your telegram token below\cf4 \
bot = telepot.Bot(\cf6 '542543102:AAE7xb6_XGAn9Yh-4PPJmfK5YK9TEA4'\cf4 )\

\f0\b \cf2 print
\f1\b0 \cf4  (bot.getMe())\
\
\cf5 # Start listening to the telegram bot and whenever a message is  received, the handle function will be called.\cf4 \
MessageLoop(bot, handle).run_as_thread()\

\f0\b \cf2 print
\f1\b0 \cf4  (\cf6 'Listening....'\cf4 )\
\

\f0\b \cf2 while
\f1\b0 \cf4  \cf6 1\cf4 :\
    sleep(\cf6 10\cf4 )}