from google.cloud import speech
from google.cloud import storage
from .audio_upload import upload_blob, delete_blob
from .audio_conversion import mp3_to_wav, stereo_to_mono
import wave

def google_transcribe(audio_file_name):


    file_name = audio_file_name
    mp3_to_wav(file_name)

    frame_rate, channels = frame_rate_channel(file_name)

    if channels > 1:
        stereo_to_mono(file_name)

    bucket_name = "knnbtp"  # Name of the bucket created in the step before
    source_file_name = audio_file_name
    destination_blob_name = audio_file_name

    upload_blob(bucket_name, source_file_name, destination_blob_name)

    gcs_uri = 'gs://' + bucket_name + '/' + audio_file_name
    transcript = ''

    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                                       sample_rate_hertz=frame_rate, language_code='en-US',
                                       enable_automatic_punctuation=True)

    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=10000)

    for result in response.results:
        transcript += result.alternatives[0].transcript

    delete_blob(bucket_name, destination_blob_name)
    return transcript