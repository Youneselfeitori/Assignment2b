#Created by: Younes Elfeitori
#Created on: Oct 2017
#Created for: ICS3U
#This program calculates the height remaining since the object has been dropped

import ui
def calculate_touch_up_inside(sender):
    #this calculates height remaining
    
    #input
    seconds = float(view['seconds_textbox'].text)
    
    #process
    height = 100 - (0.5) * 9.81 * seconds ** (2)
    
    #output
    view['height_answer_label'].text = 'The height of the object is: ' + str(height) + ' m'
	
view = ui.load_view()
view.present('sheet')
