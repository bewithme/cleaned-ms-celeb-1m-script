
import os
import shutil

# clean the ms celeb face
# Any questions pls contact me by wechat : italybaby


# change datasetDir to your own path
datasetDir="/dataset/"

# uncleaned dataset path
uncleanedFacedir=datasetDir+"MsCelebV1-Faces-Aligned/";

cleanSaveDir=datasetDir+"Cleaned-MsCelebV1-Faces-Aligned/";

if not os.path.exists(cleanSaveDir):

    os.mkdir(cleanSaveDir)

with open(datasetDir+'C-MS-Celeb/clean_list/clean_list_128Vec_WT051_P010.txt', 'r') as f:

    for line in f:

        cleanedFaceDir=line.split()[1];

        fullCleanedFaceDir=uncleanedFacedir+cleanedFaceDir;

        if os.path.exists(fullCleanedFaceDir):

            print(fullCleanedFaceDir+'\n')

            name=cleanedFaceDir.split("/")[0]

            fullCleanedFaceSaveDir=cleanSaveDir+name

            if not os.path.exists(fullCleanedFaceSaveDir):

               os.mkdir(fullCleanedFaceSaveDir)

            shutil.copy(fullCleanedFaceDir,fullCleanedFaceSaveDir)



