### Скачивание
Сначала надо составить список для скачивания: запустить generate_download_list.py
Скачивалось только 60 минут звука с каждого видео в датасете: 
```
cd data/downloads
yt-dlp -x --audio-format wav  --download-sections "*00:00:00-00:01:00" -f 'worstaudio[ext=m4a][format_id!$=-drc]' -a ..\..\download-list.txt -o '%(id)s.%(ext)s' -w -c
```

`-x --audio-format wav` -> конвертировать в wav  
`--download-sections "*00:00:00-00:01:00"` -> скачать только первую минуту  
`-f worstaudio[ext=m4a][format_id!$=-drc]` -> самое ужасное качество (для ускорения загрузки), drc отключен для однообразия)  
`-a ..\..\download-list.txt` -> список для скачивания в этом файле   
`-o '%(id)s.%(ext)s'` -> не включать название видео в название файла 
`-w` -> не скачивать то, что уже скачано
`-c` -> не останавливаться при ошибках

### Использование VGGish для получения эмбеддингов
В models/ надо 2 файла с весами скачать отсюда
https://github.com/tensorflow/models/blob/master/research/audioset/vggish/README.md

А извлекаются эмбеддинги тут:
embeddings.ipynb

### Тренировка
classification.ipynb
