'''
Created on Aug 30, 2023

@author: dan
'''

from video_files import GPVideoFolder, GPVideo
from argparse import ArgumentParser
import pathlib
import ffmpeg
from pprint import pprint
from datetime import datetime

#Nfrom datetime import fromisoformat, now

def get_creation_date(gpv):
    '''
    Use the video stream from first video file to get creation date.

    This method assumes that the metadata has tags, and one of the tags is 'creation_time', 
    and that time is in UTC iso format. 
    
    Returns creation date as a datetime object (or None if not found in metadata)

    :param gpv:GPVideo object
    '''

    dt = None
    try:    
        meta = ffmpeg.probe(gpv.filenames[0])
        gen = (stream for stream in meta['streams'] if stream['codec_type'] == 'video')
        video_stream_meta = next(gen)
        #pprint(video_stream_meta)
        d = datetime.isoformat(video_stream_meta['tags']['creation_time'].replace('Z', ''))
    except:
        print('Error getting creation date from video stream')
        dt = None        
    return dt
def concatenate_video_files(gpv, text_overlay_string, output_file):
    input_list=list()
    for f in gpv.filenames:
        input_list.append(ffmpeg.input(f))
    print("Contactenating files:")
    pprint(input_list)
    # (
    #     ffmpeg
    #     .concat(*input_list)
    #     .drawtext(text=text_overlay_string, font='Cambria', fontsize=48, fontcolor='white', box=1, boxcolor='black', x=10, y='h-text_h-10')
    #     .output(output_file)
    #     .run()
    # )
    

if __name__ == '__main__':    
    parser = ArgumentParser()
    parser.add_argument("-s", "--source-folder", required=True, help="folder containing (source) movie files")
    parser.add_argument("-o", "--output-file", required=False, default=None, help='output filename (full path)')
    parser.add_argument("-n", "--number", required=True, default=False, help="Video number to process")
    parser.add_argument("-v", "--verbose", required=False, default=False, action='store_true', help="Verbose logging")
    parser.add_argument("-p", "--probe", required=False, default=False, action='store_true', help='Probe files for metadata info, print metadata.')
    args = parser.parse_args()
    argsdict = vars(args)
    
    if not argsdict['probe'] and argsdict['output_file'] is None:
        parser.error('Output file required unless using --probe')
        
    #videos=GPVideoFolder('/Users/dan/workspace-python/gpcopy/testsrc')
    videos=GPVideoFolder(argsdict['source_folder'])
    if argsdict['verbose']:
        for v in videos.all_videos():
            print('vid num %s, files %s' % (v.video_number, v.filenames))
    #     text_overlay_string = 'Venni(12345) PC Training 2023-08-04 %{pts : hms}'
    #     concatenate_video_files(v, text_overlay_string) 
        
    if not argsdict['number'] in videos.vdict:
        print("Video number %s not found in folder %s" % (argsdict['number'], argsdict['source_folder']))
        exit()

    if not argsdict['probe']:    
        text_overlay_string = 'Venni(12345) PC Training 2023-08-04 %{pts : hms}'
        concatenate_video_files(videos.vdict[argsdict['number']], text_overlay_string, argsdict['output_file']) 
    else:
        dt = get_creation_date(videos.vdict[argsdict['number']])
        print(f'creation date: {dt}')
        

