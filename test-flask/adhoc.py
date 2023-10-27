import video_files as vf
import process_video_files as pvf
import tvfmay1 as tvf
gpvf=vf.GPVideoFolder(tvf.folder, tvf.data)
#gpvf=vf.GPVideoFolder('c:/Users/djsperka/Desktop/raw')
#gpv=gpvf.vdict['0149']
#pvf.concatenate_gpvideos(gpv, '41636', 'PCTraining-30fps', 'c:/Users/djsperka/Desktop/reduced', False)

pvf.concatenate_all_gpvideos(gpvf, '41636', 'PCTraining-30fps', 'c:/Users/djsperka/Desktop/reduced-may2023', False)