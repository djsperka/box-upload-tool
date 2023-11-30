'''
Created on Aug 30, 2023

@author: dan
'''

from video_files import GPVideoFolder, GPVideo
from argparse import ArgumentParser
from pathlib import Path
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
        dt = datetime.fromisoformat(video_stream_meta['tags']['creation_time'].replace('Z', ''))
    except Exception as e:
        print(e)
        print('Error getting creation date from video stream for GPVideo: ', str(gpv))
        dt = None        
    return dt
    
# Concatenate the list of GoPro videos in gplist. 
# Assumes GoPro raw video is 1920x1080@60fps, and applies filters to 
# - change resolution to 1024x576
# - encodes video with h264 codec (GoPro codec consumes lots of space)
# - draw date and video position on-screen
# - reduce frame rate to 30fps
# 
# The output file is approximately 1-2% the combined size of the input list. 
#
def concatenate_video_files(gplist, text_overlay_string, output_file, dry_run=False, use_audio=True):
    naudio=1
    if not use_audio:
        naudio=0
    input_list=list()
    for f in gplist:
        input_list.append(ffmpeg.input(f).video)
        if use_audio:
            input_list.append(ffmpeg.input(f).audio)
    print("Contactenating segments:")
    pprint(input_list)
    new_video = (
        ffmpeg
        .concat(*input_list, v=1, a=naudio)
        .filter('fps', fps=30) 
        .filter('scale', '1024x576')
        .drawtext(text=text_overlay_string, escape_text=False, expansion='default', font='Cambria', fontsize=24, fontcolor='white', box=1, boxcolor='black', x=10, y='h-text_h-10')
        .output(output_file, vcodec='h264')
    )

    print(new_video.get_args())
    if not dry_run:
        new_video.run()
    else:
        print(new_video.get_args())


def reduce_video(input_filename, output_filename):
    new_video = (
        ffmpeg
        .input(input_filename)
        .filter('fps', fps=30)
        .filter('scale', '1024x576')
        .output(output_filename)
        .run()
    )
    
def concatenate_gpvideos(gpv, mnum, trtype, output_folder, dry_run, use_audio=True):
    creation_date = get_creation_date(gpv)
    if not creation_date:
        raise RuntimeError('Cannot get creation date from first video')

    # check output folder and filename
    pathFolder = Path(output_folder)
    if not pathFolder.is_dir():
        raise RuntimeError(f'output folder {output_folder} not found')
    str_creation_date=creation_date.strftime('%Y-%m-%d-%H%M')
    pathOutputFile = pathFolder.joinpath(f"{mnum}_{str_creation_date}_{trtype}.mp4")
    print(f"Writing file {str(pathOutputFile)}")

    # Form overlay text
    overlay_text='%s %s %s %s' % (str_creation_date, mnum, trtype, '%{pts:hms}')
    concatenate_video_files(gpv.filenames, overlay_text, str(pathOutputFile), dry_run, use_audio)

def concatenate_all_gpvideos(gpvf, mnum, trtype, output_folder, dry_run, use_audio=True):
    for gpv in gpvf.vdict.values():
        concatenate_gpvideos(gpv, mnum, trtype, output_folder, dry_run, use_audio)

if __name__ == '__main__':    
    parser = ArgumentParser()
    parser.add_argument("-s", "--source-folder", required=True, help="folder containing (source) movie files")
    parser.add_argument("-o", "--output-folder", required=False, default=None, help='folder for output videos')
    parser.add_argument("-d", "--dry-run", required=False, default=False, action='store_true', help='When output file specified, prints out command line args for ffmpeg and exits.')
    parser.add_argument("-n", "--number", required=False, default=None, help='process only this video, not all videos in source folder')
    parser.add_argument("-v", "--verbose", required=False, default=False, action='store_true', help="Verbose logging")
    parser.add_argument("-t", "--training_type", required=False, default='Training', help='Training type, short string will be in filename and overlayed on video')
    parser.add_argument("-m", "--monkey", required=False, default='00000', help='Monkey number, will be in filename and overlayed on video')
    parser.add_argument("-q", "--no-audio", required=False, default=True, action='store_false', help='Do not pass audio - produce silent film')
    args = parser.parse_args()
    argsdict = vars(args)

    gpvf=GPVideoFolder(argsdict['source_folder'])
    if argsdict['verbose']:
        for v in gpvf.all_gpvideos():
            print('vid num %s, files %s' % (v.video_number, v.filenames))
        
    if 'number' in argsdict and argsdict['number'] is not None:
        if not argsdict['number'] in gpvf.vdict:
            print("Video number %s not found in folder %s" % (argsdict['number'], argsdict['source_folder']))
            exit()
        else:
            concatenate_gpvideos(gpvf.vdict[argsdict['number']], argsdict['monkey'], argsdict['training_type'], argsdict['output_folder'], argsdict['dry_run'], argsdict['no_audio'])
    else:
        concatenate_all_gpvideos(gpvf, argsdict['monkey'], argsdict['training_type'], argsdict['output_folder'], argsdict['dry_run'], argsdict['no_audio'])
        

