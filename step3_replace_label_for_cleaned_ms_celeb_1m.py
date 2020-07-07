
import os
import shutil

# copy face from uncleaned face folder to cleaned face folder with new label

# Any questions pls contact me by wechat : italybaby

datasetDir="/dataset/"

uncleanedFacedir=datasetDir+"MsCelebV1-Faces-Aligned/";

cleanSaveDir=datasetDir+"Cleaned-MsCelebV1-Faces-Aligned/";

with open(datasetDir+'C-MS-Celeb/clean_list/relabel_list_128Vec_T058.txt', 'r') as f:

    for line in f:

        relabelFaceDir=line.split()[1]

        fullRelabelFaceDir=uncleanedFacedir+relabelFaceDir

        if os.path.exists(fullRelabelFaceDir):

            print(fullRelabelFaceDir+'\n')

            newLabel=line.split()[0];

            newCleanedFaceSaveDir=cleanSaveDir+newLabel

            if not os.path.exists(newCleanedFaceSaveDir):

               os.mkdir(newCleanedFaceSaveDir)

            shutil.copy(fullRelabelFaceDir,newCleanedFaceSaveDir)





