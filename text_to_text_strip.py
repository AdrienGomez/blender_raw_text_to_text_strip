import bpy
### This script convert sentences in a raw text to text strip. length is define by word count ### 

#text to convert to text strip in sequence editor
thetext = "Three Rings for the Elven-kings under the sky. Seven for the Dwarf-lords in their halls of stone. Nine for Mortal Men doomed to die. One for the Dark Lord on his dark throne. In the Land of Mordor where the Shadows lie. One Ring to rule them all. One Ring to find them. One Ring to bring them all and in the darkness bind them.In the Land of Mordor where the Shadows lie."

# define average number of frame per word
framerate = bpy.data.scenes['Scene'].render.fps
wordspermin = (framerate*60)/150

#convert text to a list of sentences
thesentences = [sentence.strip() + "." for sentence in thetext.split(".") if sentence]

#unse the Frame start as a starting point for text strips)
stripstart= int(bpy.data.scenes["Scene"].frame_start)

print(thesentences)

for sentences in thesentences:
    # define the strip length
    striplength = int(wordspermin * len(sentences.split()))
    
    #add strips
    thestrip=bpy.data.scenes['Scene'].sequence_editor.sequences.new_effect(name=sentences, type='TEXT', channel=5, frame_start = int(stripstart), frame_end = stripstart+striplength)
    
    print('frame end: '+str(stripstart+striplength))
    
    #define text for the strip
    thestrip.text = sentences
    thestrip.align_y = 'BOTTOM'
    thestrip.location[1] = 0.1
    
    #define the next strip frame start
    stripstart += int(striplength)
