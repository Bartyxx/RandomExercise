"""

The users got ask gender and type of the character: 
    
Gender ---> can be male, female or other.
            - Male -> stronger
            - Female -> more dexterity
            - Other -> more intelligent
Class ----> if the users prefer a strong, agile or intelligent character
            - Strong -> Warrior
            - Agile -> Ranger
            - Intelligence -> Mage

Strenght -> Defined by the strenght point, male - strenght receive bonus.
Dexterity -> Define by the agility point, female - dexterity receive bonus.
Intellligence -> Define by the intelligencer poit, other - mage receive bonus.

Extra abilities ---> They are 3:
                     - Strenght ability
                     - Agility ability
                     - Intelligence ability
                     The extra ability is activated when the poit for the stats
                     is => 70.

==============================================================================

The max for every indicator is 100, after the 50 point for a special ability 
is unlocked. Every indicator begin with 0 for the creation of the character 
and the point are assigned as follows:

Strenght -> + 15 point strenght 
Dexterity -> + 15 point dexterity
Intelligence -> + 15 point intelligence

Male -> + 15 point strenght
Female -> + 15 point dexterity
Other -> + 15 point intelligence

A random number between 0 ad 45 is created for every indicator, the sum of the
previous choice and the random number define the character.

There are three bonus:
Male + Strenght 
Female + Agility
Other + Intelligence
In this three case the random number si generated between 10 and 55. 


"""