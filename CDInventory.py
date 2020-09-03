#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# Maria Dacutanan, 2020-Sept-01, added __init__ method to class IO
# Maria Dacutanan, 2020-Sept-01, added @property to class IO for newTable attribute
# Maria Dacutanan, 2020-Sept-01, added @property to class IO for newTable attribute
# Maria Dacutanan, 2020-Sept-01, added load_inventory method to class IO
# Maria Dacutanan, 2020-Sept-01, added save_inventory method to class IO
# Maria Dacutanan, 2020-Sept-02, removed debug statements
# Maria Dacutanan, 2020-Sept-02, added comments for clarity

#------------------------------------------#
import pickle
# -- DATA -- #
strFileName = 'CDInventory.dat'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        add_cd: append new entries into existing list of CD objects

    """
    def __init__(self,id,title,artist): #initialize default attributes
        self.__cd_id=id
        self.__cd_title=title
        self.__cd_artist=artist
    
    #Add property to cd_id to allow setting value for attribute cd_id
    @property
    def cd_id(self):
        return (self.__cd_id)
    
    @cd_id.setter
    def cd_id (self,val1):
        #Check for numeric entry; if not numberic, raise an exception
        if not val1.isnumeric():
            raise Exception('ID cannot be null and must be numeric.\n')
        else:
            self.__cd_id=val1
    
    #Add property to allow setting the value for attribute cd_title
    @property
    def cd_title(self):
        return (self.__cd_title)
   
    @cd_title.setter
    def cd_title(self,val1):
        #Check for null cd_title; if empty, raise an exception
        if (val1):
            self.__cd_title=val1
        else:
            print()
            raise Exception('CD Title must not be empty.\n')

    #Add property to allow setting value for attribute cd_artist
    @property
    def cd_artist(self):
        return (self.__cd_artist)
   
    @cd_artist.setter
    def cd_artist(self,val1):
        #Check for null cd_artist; if empty, raise an exception
        if (val1):
            self.__cd_artist=val1
        else:
            raise Exception('CD Artist must not be empty.\n')

    def noAnswer(self):
        return('I am an object of class CD')
    
    def __str__(self):
        return self.noAnswer()
    #-----------METHODS------------#
    #Method to append new CD info into table
    def add_CD(self,table):
        dicRow = {'ID': self.__cd_id, 'Title': self.__cd_title, 'Artist': self.__cd_artist}
        table.append(dicRow)
        


# -- PROCESSING -- #
class FileIO():
    """Processes data to and from file:

    properties:
        newTable(table): list of CD objects
        

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    #Initialize default attributes for class FileIO
    def __init__(self,file_name,table):
        self.__filename=file_name
        self.__newTable=table
        self.__loadctr=0
        self.__savectr=len(table)
    
    #Add property to define getter method for newTable
    @property
    def newTable(self):
        return self.__newTable
    
    #-----------METHODS-------------#
    def load_inventory(self):
        self.__newTable=[]
        try:
            with open(self.__filename, 'rb') as objFile:
                data=pickle.load(objFile) #dump 2D list into data
            while self.__loadctr <  len(data):
                self.__newTable.append(data[self.__loadctr]) #append list element (which is a dictionary) into table
                self.__loadctr+=1 #count number of rows loaded into memory
            print ('{} CD(s) loaded into inventory.\n'.format(self.__loadctr))
        except FileNotFoundError as e:
            print('Unable to load inventory from ' + self.__filename + '.') #exception handling for file not existing
            print ()
            print (e, e.__doc__, sep='\n')
            print()
        except EOFError as e:
            print(self.__filename + ' is empty.') #exception handling for empty file
            print ()
            print (e, e.__doc__, sep='\n')
            print()
        except pickle.UnpicklingError as e:
            print(self.__filename + ' is corrupted.') #exception handling for unpickling error
            print ()
            print (e, e.__doc__, sep='\n')
            print()
        return self.__newTable
    
    def noAnswer(self):
        return('I am an object of class FileIO')
    
    def __str__(self):
        return self.noAnswer()
    
    #Method to save new CD objects into binary file
    def save_inventory(self):
        try:
            with open (self.__filename, 'wb') as objFile:
                pickle.dump(self.__newTable,objFile) #pickle my 2D list
            print ('{} CD(s) saved into {}.\n'.format(self.__savectr,self.__filename))
        except PermissionError as e:
            print('Not enough rights to create/modify ' + self.__filename + '.') #if unable pickle data due to permission issues
            print ()
            print (e, e.__doc__, sep='\n')
            print ()
        except IOError as e:
            print ('I/O error({0}): {1}'.format(e.errno,e.strerror))#if unable to pickle data due to IO errors such as disk space issues
            print ()
            print (e, e.__doc__, sep='\n')
            print ()
        except pickle.PickleError as e:
            print ('Unable to write data into ' + self.__filename + '.') #if unable to pickle 2D list, exception handling for pickling errors
            print ()
            print (e, e.__doc__, sep='\n')
            print ()

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation wouild you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        if (table):
            print('======= The Current Inventory: =======')
            print('ID\tCD Title (by: Artist)\n')
            for row in table:
                print('{}\t{} (by:{})'.format(*row.values()))
            print('======================================')
        else:
            print ('Inventory is empty.\n')
    # TODO add code to get CD data from user
    @staticmethod
    def get_newInventory():
        """Prompts User to provide ID, Title and Arist Name 


        Args:
            None

        Returns:
            strID (string) - ID
            strTitle (string) - Title
            strArtist (string) - Artist

        """
        
        strID = str(input('Enter an ID: ').strip())
        strTitle = input('Enter the CD\'s Title: ').strip()
        strArtist = input('Enter the Artist\'s Name: ').strip()
        return (strID, strTitle, strArtist)

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
objFileIO=FileIO(strFileName,lstOfCDObjects) #create new object thru classs FileIO
objFileIO.load_inventory() #Invoke load_inventory method from class FileIO
lstOfCDObjects=objFileIO.newTable #Copy contents of the attribute newTable into list


#Start main loop
while True:
    # Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    #Process menu selection
    #Process exit first
    if strChoice == 'x':
        break
    #procless load inventory
    if strChoice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
            if strYesNo.lower() == 'yes':
                 print('reloading...')
                 objLoadFile=FileIO(strFileName,lstOfCDObjects) #create new object thru class FileIO
                 objLoadFile.load_inventory() #invoke load_inventory method from class FileIO
                 lstOfCDObjects=objLoadFile.newTable #overwrite contents of lstOfCDObjects
                 IO.show_inventory(lstOfCDObjects) #show contents of lstOfCDObjects
            else:
                 input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                 IO.show_inventory(lstOfCDObjects)

    #process add a CD
    elif strChoice == 'a':
        #Ask user for new ID, CD Title and Artist
        intID,strTitle,strArtist=IO.get_newInventory() #function call to prompt user for ID, CD Title and Artist and unpack return values
        objCD=CD(intID,strTitle,strArtist) #create new object through class CD
        try:
            #assign values retrieved via IO.get_newInventory function call into object
            objCD.cd_id=intID
            objCD.cd_title=strTitle
            objCD.cd_artist=strArtist
            objCD.add_CD(lstOfCDObjects)
        except Exception as e:
            print(e)
        print ()
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    #process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 's':
        #Display current inventory and ask user for confirmation to save
        if (lstOfCDObjects): #check for empty list
             IO.show_inventory(lstOfCDObjects) #function call to show current inventory
             strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
             #Process choice
             if strYesNo == 'y':
                 #save data
                 objSaveFile=FileIO(strFileName,lstOfCDObjects)
                 objSaveFile.save_inventory()
             else:
                 input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        else:
             print('Nothing to save. Inventory is empty.\n')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')