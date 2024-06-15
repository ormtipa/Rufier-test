from PyQt5.QtCore import QTime


win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = 'Welcome to the Health status detection program!'
txt_next = 'Start'
txt_instruction = '' 
txt_title = ''
txt_name = 'Enter Your Full name:'
txt_hintname = "Full name"
txt_hintage = "0"
txt_test1 = 'Lie on your back and take your pulse for 15 seconds. Click the "Start first test" button to start the timer.\nWrite down the result in the appropriate field.'
txt_test2 = 'Perform 30 squats in 45 seconds. Todo this, click the "Start doing squats" button to start the squat counter.'
txt_test3 = '''Lie on your back and take your pulse for the first 15 seconds of the minute, then for the last 15 seconds of the minute.\n
Press the "Start final test" button to start the timer.\n
The seconds that should be measured are indicated in green and the minutes that should not be measured are indicated in black. Write down the results in the appropriate fields.'''
txt_sendresults = 'Send the results'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Start the first test'
txt_starttest2 = 'Start doing squats'
txt_starttest3 = 'Start the final test'

time = QTime(0, 0, 15)
txt_timer = time.toString("hh:mm:ss")
txt_age = 'Full years:'
txt_finalwin = 'Results'
txt_index = 'Roufier Index: '
txt_workheart = 'Cardiac performance: '
txt_res1 = "low. See your doctor right away!"
txt_res2 = "satisfactory. See your doctor!"
txt_res3 = "average. It may be worth seeing your doctor to get checked out."
txt_res4 = "above average"
txt_res5 = "high"