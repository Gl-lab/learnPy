import os
import shutil

from language_sort.sorter.api.api import API


class LocalFiles:
    def __init__(self, in_dir, out_dir):
        if not os.path.isdir(in_dir) or not os.path.isdir(out_dir):
            raise ValueError("Paths must be directories")
        self.in_dir = in_dir
        self.out_dir = out_dir
        self.api = API()

    def read_file(self, file):
        with open(os.path.join(self.in_dir, file), encoding="utf-8") as f:
            text = f.read(400)
        return text

    def _make_out_dir(self, language):
        if language == '':
            raise ValueError("directory name must contain letters")
        full_path = os.path.join(self.out_dir, language)
        if not os.path.exists(full_path):
            os.makedirs(full_path)

    def prepare_paths(self):
        texts = []
        for file in os.listdir(self.in_dir):
            texts.append(self.read_file(file))
        self.api.pull_languages(texts)

    def move_files(self):
        for file in os.listdir(self.in_dir):
            text = self.read_file(file)
            language = self.api.get_language(text)
            if language is None:
                language = NOT_LABELED_LANGUAGE
            self._make_out_dir(language)
            shutil.copy(
                os.path.join(self.in_dir, file),
                os.path.join(self.out_dir, language, file)
            )
