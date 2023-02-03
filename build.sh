#!/bin/bash

clear

rm -rf ./build
rm -rf ./release
mkdir ./release

cmake --preset default .
cmake --build ./build

mkpsxiso -o game.iso -y -lba ISO_BUILD.log ./build/cd_image_f1540cc84fd80c11.xml
mv game.iso release/

PCSX-Redux-HEAD-x86_64.AppImage -run -stdout -iso ./release/game.iso

echo ""
read -n 1 -s -r -p "Press any key to continue..."
echo ""
echo ""

rm *.mcd
rm offscreen.*
rm output.*