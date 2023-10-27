import video_files as vf

folder='c:/Users/djsperka/Desktop/m2023/41636_March2023/'
data={
'41636_03092023': 
[
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03092023/P_CTraining_41636_3 9 23_A.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03092023/P_CTraining_41636_03 09 23_B.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03092023/P_CTraining_41636_03 09 23_C.MP4'
], 
'41636_03102023':
[
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03102023/P_CTraining_41636_3 10 23_A.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03102023/P_CTraining_41636_03 10 23_B.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03102023/P_CTraining_41636_03 10 23_C.MP4'
],
'41636_03132023':
[
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03132023/P_CTraining_41636_03 13 23_A.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03132023/P_CTraining_41636_3 13 23_B.MP4'
],
'41636_03152023':
[
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03152023/P_CTraining_41636_03 15 23_A.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03152023/P_CTraining_41636_3 15 23_B.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03152023/P_CTraining_41636_3 15 23_C.MP4'
],
'41636_03162023':
[
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03162023/P_CTraining_41636_03 16 23_A.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03162023/P_CTraining_41636_3 16 23_B.MP4'
],
'41636_03212023':
[
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03212023/P_CTraining_41636_3 21 23_A.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03212023/P_CTraining_41636_03 21 23_B.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03212023/P_CTraining_41636_03 21 23_C.MP4'
],
'41636_03222023':
[
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03222023/P_CTraining_41636_03 22 23A.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03222023/P_CTraining_41636_03 22 23B.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03222023/P_CTraining_41636_03 22 23C.MP4'
],
'41636_03232023':
[
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03232023/P_CTraining_41636_03 23 23_A.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03232023/P_CTraining_41636_03 23 23_B.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03232023/P_CTraining_41636_03 23 23_C.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03232023/P_CTraining_41636_03 23 23_D.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03232023/P_CTraining_41636_03 23 23_E.MP4'
],
'41636_03272023':
[
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03272023/41636_P_CTraining_03 27 23_A.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03272023/41636_P_CTraining_03 27 23_B.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03272023/41636_P_CTraining_03 27 23_C.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03272023/41636_P_CTraining_03 27 23_D.MP4'
],
'41636_03282023':
[
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03282023/41636_P_CTraining_03_28_23_A.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03282023/41636_P_CTraining_03_28_23_B.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03282023/41636_P_CTraining_03_28_23_C.MP4'
],
'41636_03292023':
[
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03292023/41636_P_CTraining_03_29_23_A.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03292023/41636_P_CTraining_03_29_23_B.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03292023/41636_P_CTraining_03_29_23_C.MP4'
],
'41636_03302023':
[
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03302023/41636_P_CTraining_03_30_23_A.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03302023/41636_P_CTraining_03_30_23_B.MP4',
'c:/Users/djsperka/Desktop/m2023/41636_March2023/41636_03302023/41636_P_CTraining_03_30_23_C.MP4'
]
}
