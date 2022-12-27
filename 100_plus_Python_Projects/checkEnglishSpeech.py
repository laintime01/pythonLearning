import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    print('Please read the english sentence')
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    # try recognizing the speech in the recording
    try:
        text = recognizer.recognize_google(audio)
    except Exception as e:
        print(e)
        text = None
    return text

if __name__ == '__main__':
    text = input('Please input a English word or sentence: ').strip()
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    speech_text = recognize_speech_from_mic(recognizer, microphone)

    while speech_text is not None and text.lower() != speech_text.lower():
        print(speech_text)
        speech_text = recognize_speech_from_mic(recognizer, microphone)

    if speech_text:
        print('{} {}'.format(speech_text, 'V'))
    else:
        print('Please try the speech recognition service later')