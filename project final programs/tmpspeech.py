'''
Created on 09-Sep-2016

@author: Aishwarya-HP
'''
s="empty"
class tmpspeech:
    
        def speech(self):
            import speech_recognition as sr
            
            #obtain audio from the microphone
    
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            # recognize speech using Google Speech Recognition
            try:
                
                s=str(r.recognize_google(audio,language="en-IN"))
                
    # for testing purposes, we're just using the default API key r.recognize_google(audio))
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
                #print("Google Speech Recognition thinks you said " +r1)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                return ""
            except sr.RequestError as e:
                print("Could not request results fs=r.recognize_google(audio)rom Google Speech Recognition service; {0}".format(e))
                return ""
            return s   
            
            
