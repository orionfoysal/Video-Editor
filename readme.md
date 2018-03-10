## Video Splitter
__Cut a video file at different time frames and combine them to generate a new video file. A CSV file contains the Start and End times data.__

### Input: 
1. Video in avi or mp4 format.
2. csv file with timestamps. 

### Example Valid CSV Formats:
```
Time stamp in second format:
___________
| 17 | 35 |
|---------| 
|200 |340 |
'''''''''''

OR

TimeStamp in HH:MM:SS format: [Working ? Need To Check]
______________________
|00:10:05 | 00:15:20 |
|--------------------|
|01:01:10 | 01:15:10 | 
''''''''''''''''''''''
```
   
### Output:
1. Output video file path
2. Output will be saved in .mp4 format 
 
