import re
 
# Open input file for reading and output file for writing
with open("taerelwikitextstage1.txt", "r") as input_file, open("taerelwikitextstage2.txt", "w") as output_file:
 
    input = input_file.read()
    
    pattern = r"(==History==|====Stone Age: Before 1E 0==|====Copper Age: 1E 1-1E 2200==|====Bronze Age: 1E 2200-1E 4400==|====Iron Age: 2E 0-2E 700==|====Ancient Age: 2E 700-2200==|====Middle Ages: 3E 0-2050==|====Early Modern Age: 2050-3E 2600==|====Industrial Age: 3E 2600-3E 2700==|====Machine Age: 3E 2700-3E 2800==|====Atomic Age: 3E 2800-3E 2850==|====Space Age: 2E 2850-2E 2900==|====Information Age: 3E 2850-3E 2900==|====Genetic Age: 3E 2950-3E 3000==|====Awakening Age: 3E 3000-3E 3415==|======Shattering Age: 4E 0 - 4E 250==|==History==|==Geography==|==Plants==|==Animals==|==Biology==|==Psychology==|==Culture==|==Government==|==Military==|==Religion==|==Miscellany==|==History (A'voreld kin'toni Clan)==|==Biology (A'voreld kin'toni Clan)==|==Psychology (A'voreld kin'toni Clan)==|==Culture (A'voreld kin'toni Clan)==|==Government (A'voreld kin'toni Clan)==|==Military (A'voreld kin'toni Clan)==|==Religion (A'voreld kin'toni Clan)==|==Miscellany (A'voreld kin'toni Clan)==|===Stone Age: Before 1E 0===|===Copper Age: 1E 1-1E 2200===|===Bronze Age: 1E 2200-1E 4400===|===Iron Age: 2E 0-2E 700===|===Ancient Age: 2E 700-2200===|===Middle Ages: 3E 0-2050===|===Early Modern Age: 2050-3E 2600===|===Industrial Age: 3E 2600-3E 2700===|===Machine Age: 3E 2700-3E 2800===|===Atomic Age: 3E 2800-3E 2850===|===Space Age: 2E 2850-2E 2900===|===Information Age: 3E 2850-3E 2900===|===Genetic Age: 3E 2950-3E 3000===|===Awakening Age: 3E 3000-3E 3415===|===Shattering Age: 4E 0-4E 250===|== History ==|== Geography ==|== Plants ==|== Animals ==|===Industrial Age:  3E 2600-3E 2700===|===Shattering Age: 4E 0 - 4E 250 ===|==Content ==|===Life in Kran-Xtar===|===The Journey Northward===|===Arrival in Zypron and Duhain’s Rule===|===The Crowning and Unification Wars===|===The First Decade of Peace- Aelain’s Reforms===|===The Return of Uron Drak===|===The Second Decade of Peace- Isolation===|===Final Vengeance and Death===|==Personality==|==Appearance==|==Abilities and Traits==|==Allies==|==Enemies==|\[\[Taerel:[^\]]*?\]\]|\[\[Category:[^\]]*?\]\])"
    template_pattern = r"\{\{[\s\S]*?\}\}"
 
    # Compile regex
    pattern_regex = re.compile(pattern)
    template_regex = re.compile(template_pattern)
    
    # Remove matches from file
    input = pattern_regex.sub("", input)
    input = template_regex.sub("", input)
    
    # Output to new file
    output_file.write(input)

   
