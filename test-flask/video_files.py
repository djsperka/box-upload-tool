'''
Created on Aug 24, 2023

@author: dan
'''

from argparse import ArgumentParser
import pathlib
import os
import re
import shutil

class GPVideo:
    def __init__(self, videonumber):
        self.video_number = videonumber
        self.filenames = list()
    def __lt__(self, num):
        return self.video_number < num
    def __str__(self):
        return "%s: %s" % (self.video_number, self.filenames)
    def add_video(self, filename):
        self.filenames.append(filename)

class GPVideoFolder:
    def __init__(self, folder):
        self.path = pathlib.Path(folder)
        if not self.path.is_dir():
            raise RuntimeError("gopro video folder %s not found!" % (folder))
        self.vdict = dict()
        
        # regex to see filename pattern thatthe GOPRO uses.
        # First capture group is the sequence number, second is the video id.
        video_name_pattern = re.compile('^GH([0-9]{2})([0-9]{4}).MP4$')
        
        # scan source folder. Create new GPVideo if needed. Add video 
        # files as they come up.
        obj = os.scandir(folder)
        for entry in obj:
            if entry.is_file():
                m = video_name_pattern.match(entry.name)
                if m is not None:
                    movie_id = m.groups()[1]
                    movie_seq = m.groups()[0]
                    if movie_id not in self.vdict:
                        self.vdict[movie_id] = GPVideo(movie_id)
                    self.vdict[movie_id].add_video(str(self.path.joinpath(entry.name)))
                    
        # sort file lists
        for v in self.vdict.values():
            v.filenames.sort()
    def all_video_files(self):
        '''
        Returns a list of all video filenames (no path, string) in this folder.  
        '''
        l = list()
        for gpv in self.vdict.values():
            for f in gpv.filenames:
                l.append(f)
        return l
    def all_videos(self):
        '''
        Returns list of GPVideo
        '''
        return self.vdict.values()        
    def copy_and_delete(self, dest, doDelete=True):
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
            print("Copying %s to %s..." % (str(srcpath), str(destination_folder)))
            shutil.copy(self.path.joinpath(f), destination_folder)
            dstpath = destination_folder.joinpath(f)
            if srcpath.stat().st_size == dstpath.stat().st_size :
                if doDelete:
                    srcpath.unlink()
                    print(f"Removed {str(srcpath)}")
                else:
                    print(f"Source file {str(srcpath)} not deleted.")
            else: 
                raise RuntimeError("Incomplete file copy for %s, src/dest size %d/%d" % (f, srcpath.stat().st_size, dstpath.stat().st_size))

if __name__ == '__main__':    
    parser = ArgumentParser()
    parser.add_argument("-s", "--source-folder", required=True, help="folder containing (source) movie files")
    parser.add_argument("-d", "--dest-folder", required=True, help='destination folder for file operations (copy, compress)')
    parser.add_argument("-n", "--no-delete", required=False, default=False, action='store_true', help="If set, do not delete files from source location after copy")
    args = parser.parse_args()
    argsdict = vars(args)
    
    #vdict=GPVideoFolder('/Users/dan/workspace-python/gpcopy/testsrc')
    videos=GPVideoFolder(argsdict['source_folder'])
    videos.copy_and_delete(argsdict['dest_folder'], not argsdict['no_delete'])

    