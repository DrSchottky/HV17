#include <stdio.h>
#include "ice.h"

int main()
{
	
	ICE_KEY *key = ice_key_create(1); 
	ice_key_set(key, "ice-cold"); 
	FILE * fp = fopen("HV17-flag", "rb");
	char in_buffer[32];
	char out_buffer[29];
	fread(in_buffer, 32, 1, fp);
	fclose(fp);
	int i = 0;
	for(i = 0; i < 32; i += 8)
		ice_key_decrypt (key, in_buffer+i, out_buffer+i); 
	fp = fopen("HV17-flag.dec", "wb");
	fwrite(out_buffer, 29, 1, fp);
	fclose(fp);
	
	return 0;
}