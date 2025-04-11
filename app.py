from fastapi import FastAPI
from pydantic import BaseModel , HttpUrl
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

app = FastAPI()

class Linkurl(BaseModel):
    url:HttpUrl

@app.post("/transcript")
async def YTtranscript(Link_request:Linkurl):
    url_str = str(Link_request.url)

    parsed_url = urlparse(url_str)
    query_params = parse_qs(parsed_url.query)

    video_id = query_params['v'][0]
    print(video_id)
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.get_transcript(video_id,("hi","en"))

    transcript_text = ""
    for i in transcript:
        transcript_text += " " + i["text"]

    print(transcript_text)
    # print(Link_request.url)
    return transcript_text