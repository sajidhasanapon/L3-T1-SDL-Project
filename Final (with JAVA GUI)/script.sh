#!/bin/bash 
cd python

rm -R name dob mob nid mail
rm name.png mob.png dob.png nid.png mail.png rotated.png

python ./rotate.py $1
python ./crop.py ./rotated.png
python ./sc.py
python ./main.py

#rm -R name dob mob nid mail
#rm name.png mob.png dob.png nid.png mail.png rotated.png