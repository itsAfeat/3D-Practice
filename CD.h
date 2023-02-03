#ifndef CD_H
#define CD_H

#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <psxcd.h>

// Loading files from the CD
void *loadFile(const char* filename)
{
	CdlFILE filePos;
	int		numsecs;
	char	*buff;

	buff = NULL;

	// Locate the file on the CD
	if (CdSearchFile(&filePos, filename) == NULL)
		printf("%s could not be found", filename);
	else
	{
		numsecs = (filePos.size+2047)/2048;				// Calculate the number of sectors to read
		buff = (char*)malloc(2048*numsecs);				// Allocate buffer for the file
		CdControl(CdlSetloc, (u_char*)&filePos.pos, 0);	// Set the file as the read target
		CdRead(numsecs, (uint32_t*)buff, CdlModeSpeed);	// Start the read operation
		CdReadSync(0, 0);								// Wait until the read operation is complete
	}

	return buff;
}

int getFileSize(const char* filename)
{
	CdlFILE filePos;
	CdSearchFile(&filePos, filename);
	return filePos.size;
}

#endif