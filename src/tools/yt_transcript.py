from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable
)
from urllib.parse import urlparse, parse_qs


def get_video_id(url):
    parsed_url = urlparse(url)

    if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(parsed_url.query).get("v", [None])[0]

    elif parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]

    return None


def get_transcript_from_url(url):
    video_id = get_video_id(url)

    if not video_id:
        raise ValueError("Invalid YouTube URL")

    ytt = YouTubeTranscriptApi()

    try:
        # Try English transcript first
        transcript_list = ytt.fetch(video_id, languages=["en"])

    except NoTranscriptFound:
        try:
            # Fetch any available transcript
            transcript_list = ytt.fetch(video_id)

        except NoTranscriptFound:
            raise ValueError("No transcript available for this video.")

    except TranscriptsDisabled:
        raise ValueError("Transcripts are disabled for this video.")

    except VideoUnavailable:
        raise ValueError("Video is unavailable or private.")

    except Exception as e:
        raise ValueError(f"Transcript fetch failed: {str(e)}")

    transcript = " ".join(item.text for item in transcript_list)

    return transcript