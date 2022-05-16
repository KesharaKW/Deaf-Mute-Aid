#Libraries
import cv2
import numpy as np
import deepspeeech 

#Create a model object
model_file_path = 'deepspeech-0.6.0-models/output_graph.pbmm'
beam_width = 500
model = deepspeech.Model(model_file_path, beam_width)
#Adding langauge model for better accuracy
lm_file_path = 'deepspeech-0.6.0-models/lm.binary'
trie_file_path = 'deepspeech-0.6.0-models/trie'
lm_alpha = 0.75
lm_beta = 1.85
model.enableDecoderWithLM(lm_file_path, trie_file_path, lm_alpha, lm_beta)

'''
#Read the audio file (If we got a audio file)
import wave
filename = 'audio/8455-210777-0068.wav' #sample file
w = wave.open(filename, 'r')
rate = w.getframerate()
frames = w.getnframes()
buffer = w.readframes(frames)
print(rate)
16000 #wave rate
print(model.sampleRate())
16000
type(buffer)
#Convert into 16-bit int array
import numpy as np
data16 = np.frombuffer(buffer, dtype=np.int16)
type(data16)
#Getting the text
text = model.stt(data16)
print(text)
'''

#Streaming API
'''
Consists of 3 steps
1. Session open
2. Data Feeding
3. Session close
'''
#1. Open a streaming session
context = model.createStream()
#2. Feeding
buffer_len = len(buffer)
offset = 0
batch_size = 16384
text = ''
while offset < buffer_len:
     end_offset = offset + batch_size
     chunk = buffer[offset:end_offset]
     data16 = np.frombuffer(chunk, dtype=np.int16)
     model.feedAudioContent(context, data16)
     text = model.intermediateDecode(context)
     print(text)
     offset = end_offset
#3. Result text
text = model.finishStream(context)
print(text)

#Uploading the animation ~ Create a VideoCapture object and read from input file
anim1 = cv2.VideoCapture('anim1.mp4') #Hello
anim2 = cv2.VideoCapture('anim2.mp4') #Hi
anim3 = cv2.VideoCapture('anim3.mp4')

#Play the relevant animation
if text == Hello:
	cv2.imshow('Result',anim1)
if text == Hi:
	cv2.imshow('Result',anim2)
