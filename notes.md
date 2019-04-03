*NOTES*

_Pending Items:_
   - Review score list and make it dynamic in terms of innings captured
   - Testing of overall game play and statistics
   - Some UI clean up and fine tuning
   - Incorporate some probability to the types of hits that currently being generated at random          
   - Review some functions and switch arguments to lists and unpack arguments within the function 
   - Review advance runner; if there are runners on base, make sure after an out they remain on base 
     unless it is the third out
   - Rebuild the score list vs score_list_team_roster; put into a function and run as a test before
     the game ends. The totals between the two structures should tie out.


_Completed:_

   - Convert main Innings For Loop which loops through nine innings to a While loop that checks for the 
     completion of nine innings. After nine innings the scores are checked for a tie. Need to incorporate
     extra innings if there is a tie.   *** Keeping for Loop, checking for tie after nine innings
     
   - Moved Inning process to a function
        
   - Run extra innings process after tie detected after nine innings
   
   - Rebuilding score box to allow variable number of total innings
   
   - Moved most of the data structures to the function file
   
   - Print score box after a run is scored
     - Print after a team is done with their at bat