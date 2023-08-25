'''
Created on Aug 24, 2023

@author: dan
'''

import pathlib
import os
import re
import shutil

class GPVideo:
    def __init__(self, videonumber):
        self.video_number = videonumber
        self.video_files = list()
    def __lt__(self, num):
        return self.video_number < num
    def __str__(self):
        return "%s: %s" % (self.video_number, self.video_files)
    def add_video(self, filename):
        self.video_files.append(filename)
class GPVideoFolder:
    def __init__(self, folder):
        self.path = pathlib.Path(folder)
        if not self.path.is_dir():
            raise RuntimeError("gopro video folder %s not found!" % (folder))
        self.videos = dict()
        video_name_pattern = re.compile('^GH([0-9]{2})([0-9]{4}).MP4$')
        obj = os.scandir(folder)
        for entry in obj:
            if entry.is_file():
                m = video_name_pattern.match(entry.name)
                if m is not None:
                    movie_id = m.groups()[1]
                    movie_seq = m.groups()[0]
                    if movie_id not in self.videos:
                        self.videos[movie_id] = GPVideo(movie_id)
                    self.videos[movie_id].add_video(entry.name)
    def all_video_files(self):
        '''
        Returns a list of all video filenames (no path, string) in this folder. 
        '''
        l = list()
        for gpv in self.videos.values():
            for f in gpv.video_files:
                l.append(f)
        return l        
    def copy_and_delete(self, dest):
        '''
        Copy all video files in this folder to the folder in dest, deleting each file from source folder after copy.
        :param dest: (string) destination folder for files.
        '''
        destination_folder = pathlib.Path(dest)
        if not destination_folder.is_dir():
            raise RuntimeError("destination video folder %s not found!" % (dest))
        all_files = self.all_video_files()
        for f in all_files:
            srcpath = self.path.joinpath(f)
            shutil.copy(self.path.joinpath(f), destination_folder)
            print("Copied %s to %s" % (str(srcpath), str(destination_folder)))
            dstpath = destination_folder.joinpath(f)
            if srcpath.stat().st_size == dstpath.stat().st_size :
                srcpath.unlink()
                print(f"Removed {str(srcpath)}")
            else: 
                raise RuntimeError("Incomplete file copy for %s, src/dest size %d/%d" % (f, srcpath.stat().st_size, dstpath.stat().st_size))

if __name__ == '__main__':
    videos=GPVideoFolder('/Users/dan/workspace-python/gpcopy/testsrc')
    videos.copy_and_delete('/Users/dan/workspace-python/gpcopy/testdst')

    