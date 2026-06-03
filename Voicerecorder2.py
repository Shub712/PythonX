#=================================================================
#                   Simple Voice Recorder in Python                       
#=================================================================

#=================================================================
# Author : Shubham Kiran Pawar
# Date :    12/05/2026
#=================================================================

import pyaudio
import wave

# Configuration

FORMAT = pyaudio.paInt16    # this means audio stores in a 16 bit numbers
CHANNELS = 1                # microphonne channels 1 means Mono, 2 means stereo
RATE = 16000                # it means sound samples taken every second higher the number big file size
CHUNK = 1024                # records in a small samples audio bucket

audio = pyaudio.PyAudio()  # created PyAudio object

stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE, # it means open microphone and starts litening
                    input=True,frames_per_buffer=CHUNK
                    )

print("\nPress : ctrl + c to stop the recording")
print("-"*60)
print("Recording...")
print("-"*60)

frames = []  # stores all the recording samples in the list 

# Record for 5 seconds (example)
try:
    while True:
        
        data = stream.read(CHUNK,exception_on_overflow=False)
        frames.append(data) 

except KeyboardInterrupt:
    print("\nRecording Stopped!")

finally:
    print("Recording Finished...")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save audio into .wave file

    filename = input("File Name : ")

    sound_file = wave.open(filename+".wave","wb")

    sound_file.setnchannels(CHANNELS)  # this tells wav file if its mono or stereo
    sound_file.setsampwidth(audio.get_sample_size(FORMAT))  # this tells how big the sample size is 
    sound_file.setframerate(RATE)  # set the frame rate 44100 frames per second

    sound_file.writeframes(b''.join(frames))  # here we join all the chunks from the frames list because wave nees one big data 

    sound_file.close()

    print("Audio Saved..")