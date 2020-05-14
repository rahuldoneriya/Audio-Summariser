from audio_processing.audio_conversion import mp3_to_wav, stereo_to_mono
from audio_processing.audio_upload import upload_blob, delete_blob
from audio_processing.audio_transcription import google_transcribe
from text_processing.text_cleaning import clean_text
from text_processing.text_summary import generate_summary
from text_processing.sentiment_analysis import analyze_sentiment

def main():
    audio_file_name = 'childlabor.wav'
    
    # Convert audio if necessary
    mp3_to_wav(audio_file_name)
    
    # Transcribe audio
    transcript = google_transcribe(audio_file_name)
    
    # Clean the transcript
    cleaned_text = clean_text(transcript)
    
    # Generate summary
    summary = generate_summary(cleaned_text)
    
    # Perform sentiment analysis
    sentiment = analyze_sentiment(cleaned_text)
    
    # Output results
    with open("btpsummary.txt", "w") as summary_file:
        summary_file.write(summary)
    
    with open("btpsentimentanalysis.txt", "w") as sentiment_file:
        sentiment_file.write(str(sentiment))
    
    print('Process Ends')


if __name__ == "__main__":
    main()