#=================================================================================
#                   Speech To Text Convertor
#=================================================================================


# Speech Recognition Library
import speech_recognition as sr

recognizer = sr.Recognizer()  # Created recognizers object , listen to audio, convert audio into text

print("="*60)
print("Welcome to Speech to text converter")
print("="*60)

print("NOTE :- Enter Duration Like :")
print("To record in minutes : 10 min")
print("To record in seconds : 20")
duration = input("\nPlease Enter The Duration:")

d = duration.split()

if len(d) == 2 and d[1] == 'min':
    duration = int(d[0])
    duration = duration*60
else:
    duration = int(d[0])
    
with sr.Microphone() as source:  # we opened microphone here 
    
    print("Listening...")
    
    # it detects noise around u like fan , ac traffic it improves recognition accuracy
    # Duration is for listening noise more duartion more efficiency but 
    # low duration faster working
    recognizer.adjust_for_ambient_noise(source,duration=0.2) 
    
    # this records ypur voice 
    audio = recognizer.record(source,duration = duration)

try:
    # here we send our audio to Google Speech Recognition API
    text = recognizer.recognize_google(audio) 
    
    # Here we print the text 
    print(f"You said: {text}")

# Error handling
except sr.UnknownValueError:
    print("Could Not understand audio")

except sr.RequestError as e :
    print(f"API Error: {e}")