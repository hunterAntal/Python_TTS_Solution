from pyt2s.services import stream_elements

# Default Voice
data = stream_elements.requestTTS('Lorem Ipsum is simply dummy text.')

# Custom Voice
data = stream_elements.requestTTS('Lorem Ipsum is simply dummy text.', stream_elements.Voice.Russell.value)

with open('output.mp3', '+wb') as file:
    file.write(data)