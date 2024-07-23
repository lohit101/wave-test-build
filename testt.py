import requests
from pydub import AudioSegment

url = "https://api.v7.unrealspeech.com/speech"

payload = {
    "Text": "This is a test voice message just to see if this block is working",
    "VoiceId": "Scarlett",
    "Bitrate": "192k",
    "Speed": "0",
    "Pitch": "1",
    "TimestampType": "sentence"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer 7Qtps05ptTV1sGGvuqyMMDDRJ76gcFFQFJI4Ycw6wj4L0ehGI3Q3tL"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    response_json = response.json()
    output_uri = response_json.get("OutputUri")
    
    if output_uri:
        # Download the audio file from the output URI
        audio_response = requests.get(output_uri)
        if audio_response.status_code == 200:
            with open("output.mp3", "wb") as audio_file:
                audio_file.write(audio_response.content)
            print("Audio content written to file 'output.mp3'")
        else:
            print(f"Failed to download audio file: {audio_response.status_code}")
    else:
        print("Output URI not found in the response")
else:
    print(f"Request failed: {response.status_code}")
    print(response.text)

sound = AudioSegment.from_mp3("output.mp3")
sound.export("output.wav", format="wav")