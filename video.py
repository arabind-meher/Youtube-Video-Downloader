import os
import ffmpeg

from pytube import YouTube
from random_word import RandomWords


class YoutubeVideo:
    @staticmethod
    def get_video(url):
        if url == '':
            return None
        try:
            video = YouTube(url)
        except:
            return None

        video_data = dict()

        video_data['url'] = url
        video_data['title'] = video.title
        video_data['author'] = video.author
        video_data['description'] = video.description
        video_data['length'] = video.length
        video_data['views'] = video.views
        video_data['rating'] = video.rating

        video_data['streams'] = video.streams.filter(only_video=True, subtype='mp4').order_by('resolution').desc()
        video_data['audios'] = video.streams.filter(only_audio=True).order_by('abr').desc()
        video_data['captions'] = video.captions

        print('Title:', video_data['title'])
        print('Author:', video_data['author'])
        print('Description:\n', video_data['description'])
        print('Length:', video_data['length'])
        print('Views:', video_data['views'])
        print('Rating:', video_data['rating'])
        print('Streams:')
        for stream in video_data['streams']:
            print(stream)
        print('Audios:')
        for audio in video_data['audios']:
            print(audio)
        print('Captions:')
        for caption in video_data['captions']:
            print(caption)

        return video, video_data

    @staticmethod
    def download_video(video, title, description, path, video_itag, audio_itag, lang):
        try:
            os.mkdir(os.path.join(path, title))
            path = os.path.join(path, title)
        except OSError:
            word = RandomWords().get_random_word()
            os.mkdir(os.path.join(path, title + word))
            path = os.path.join(path, title + word)

        if video_itag != '':
            print('video --', end=' ')
            video.streams.get_by_itag(video_itag).download(path)
            print('done')

        if audio_itag != '':
            print('audio --', end=' ')
            video.streams.get_by_itag(audio_itag).download(path)
            print('done')

        if lang != '':
            print('caption --', end=' ')
            caption = video.captions.get_by_language_code(lang)
            caption = caption.generate_srt_captions()

            file = open(os.path.join(path, title + '.srt'), 'w')
            file.write(caption)
            file.close()
            print('done')

        if description != '':
            print('description --', end=' ')
            file = open(os.path.join(path, title + '.txt'), 'w')
            file.write(description)
            file.close()
            print('done')

        video_ext = ['mp4', 'mkv']
        audio_ext = ['m4a', 'webm']

        video_file = [
            file for file in os.listdir(path)
            if os.path.isfile(os.path.join(path, file)) and file[0] != '.' and file.split('.')[-1] in video_ext
        ]

        audio_file = [
            file for file in os.listdir(path)
            if os.path.isfile(os.path.join(path, file)) and file[0] != '.' and file.split('.')[-1] in audio_ext
        ]

        video_file = ffmpeg.input(os.path.join(path, video_file[0]))
        audio_file = ffmpeg.input(os.path.join(path, audio_file[0]))

        ffmpeg.concat(video_file, audio_file, v=1, a=1).output(os.path.join(path, '_' + title + '.mp4')).run()
        print('Done!')
