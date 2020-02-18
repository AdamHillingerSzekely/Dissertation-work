#! /bin/sh


filebox='/Users/adamszekely/primitive_shapes_generator/Aligned_shapes/boxes/*.pcd'
filecylinder='/Users/adamszekely/primitive_shapes_generator/Aligned_shapes/cylinders/*.pcd'
filesphere='/Users/adamszekely/primitive_shapes_generator/Aligned_shapes/spheres/*.pcd'
touch profilesaligned.csv
for f in $filebox $filecylinder $filesphere;
do
./shapes_profiling.py $f
paste "/Users/adamszekely/shapes-recognition/profile_0.csv" >>profiles.csv
paste "/Users/adamszekely/shapes-recognition/profile_1.csv" >>profiles.csv
paste "/Users/adamszekely/shapes-recognition/profile_2.csv" >>profiles.csv
done


