# PSn00bSDK example CMake script
# (C) 2021 spicyjpeg - MPL licensed

cmake_minimum_required(VERSION 3.21)

project(
	PSn00bSDK-template
	LANGUAGES    C CXX ASM
	VERSION      1.0.0
	DESCRIPTION  "3D practice"
	HOMEPAGE_URL "http://lameguy64.net/?page=psn00bsdk"
)

psn00bsdk_add_executable(game GPREL main.c)

psn00bsdk_add_cd_image(
	iso      # Target name
	game	 # Output file name (= game.bin + game.cue)
	iso.xml  # Path to config file
	DEPENDS game
)
