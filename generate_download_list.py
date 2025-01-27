import os
import re
from pathlib import Path

import pandas as pd

__file_dir = Path(os.path.dirname(os.path.abspath(__file__)))


def load_youtube_videos():
    file_path = os.path.join(__file_dir, 'data/youtube.csv')
    return pd.read_csv(file_path)


def main():
    youtube_videos = load_youtube_videos()
    downloads_dir = Path(__file_dir / 'data/downloads')

    def get_downloaded_audio_path(video_id: str) -> Path:
        return downloads_dir / f"{video_id}.wav"

    def get_video_url(video_id: str) -> str:
        return 'https://www.youtube.com/watch?v=' + video_id

    def is_valid_video_id(video_id: str) -> bool:
        return re.match(r'^[a-zA-Z0-9_-]{11}$', video_id) is not None

    valid_video_ids = [video_id for video_id in youtube_videos.link if is_valid_video_id(video_id)]
    invalid_video_ids = [video_id for video_id in youtube_videos.link if not is_valid_video_id(video_id)]
    downloaded_video_ids = set(link for link in valid_video_ids if get_downloaded_audio_path(link).exists())
    missing_video_ids = list(set(valid_video_ids) - downloaded_video_ids)

    print(f'{len(invalid_video_ids)} invalid')
    print(f'{len(downloaded_video_ids)} already downloaded')
    print(f'{len(missing_video_ids)} are missing')

    links = [get_video_url(vid) for vid in missing_video_ids]
    Path('download-list.txt').write_text('\n'.join(links))


if __name__ == '__main__':
    main()
