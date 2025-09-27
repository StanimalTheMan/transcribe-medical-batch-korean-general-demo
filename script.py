
# from __future__ import print_function
# import time
# import boto3

# transcribe = boto3.client('transcribe')
# job_name = "my-first-med-transcription-job"
# job_uri = "s3://transcribe-medical-demo-kinori/my-input-files/cholesterol_bilirubin_high.m4a"
# transcribe.start_medical_transcription_job(
#     MedicalTranscriptionJobName = job_name,
#     Media = {
#     'MediaFileUri': job_uri
#     },     
#     OutputBucketName = 'transcribe-medical-demo-kinori',                                
#     OutputKey = 'my-output-files/', 
#     LanguageCode = 'en-US',
#     Specialty = 'PRIMARYCARE',
#     Type = 'DICTATION'
# )
# while True:
#     status = transcribe.get_medical_transcription_job(MedicalTranscriptionJobName = job_name)
#     if status['MedicalTranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
#         break
#     print("Not ready yet...")
#     time.sleep(5)
# print(status)
                        
# Korean
from __future__ import print_function
import time
import boto3

# Use the general Transcribe service (not Medical)
transcribe = boto3.client("transcribe")

job_name = "my-korean-transcription-job"
job_uri = "s3://transcribe-medical-demo-kinori/my-input-files/cholesterol_bilirubin_high.m4a"

# Start a regular transcription job with Korean language support
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={"MediaFileUri": job_uri},
    MediaFormat="m4a",             # specify format for clarity
    LanguageCode="ko-KR",          # Korean transcription
    OutputBucketName="transcribe-medical-demo-kinori",
    OutputKey="my-output-files/"
)

# Poll until the job finishes
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status["TranscriptionJob"]["TranscriptionJobStatus"] in ["COMPLETED", "FAILED"]:
        break
    print("Not ready yet...")
    time.sleep(5)

print(status)
