#! /bin/sh


filebox='/Users/adamszekely/primitive_shapes_generator/clean/boxes/*.pcd'
filecylinder='/Users/adamszekely/primitive_shapes_generator/clean/cylinders/*.pcd'
filesphere='/Users/adamszekely/primitive_shapes_generator/clean/spheres/*.pcd'
touch profilesold.csv
for f in $filebox $filecylinder $filesphere;
do
./shapes_profiling.py $f
paste "/Users/adamszekely/shapes-recognition/profile_0.csv" >>profilesold.csv
paste "/Users/adamszekely/shapes-recognition/profile_1.csv" >>profilesold.csv
paste "/Users/adamszekely/shapes-recognition/profile_2.csv" >>profilesold.csv
done


