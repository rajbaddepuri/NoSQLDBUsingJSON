# JSON BASED NOSQL USING PYTHON

This file is to explain about the NOSQL implementation usage which is developed based on
JSON format.
Note that this program will take care of creating json file at present location if no json file is available.
For the time, it will ask about the field names. Please follow the instructions carefully.
Since main base of the project is NOSQL, this project will be useful to save data in
key-value pair. Following are the basic functionalities which supports in this project.

1. Add a record
2. Delete a record
3. Find record(s)
4. Save
5. Quit

### 1. Add a record

This functionalty is used to add a record (row in database) based on fields (columns in database).
If the addition of the record is first time, then this project will automatically ask about the field names.
Fields names should be in comma saparated value (ex: ID,Name,Age). Once Fields are added, then you are good
to add the values to provided fields. Program will walk you through by providing neccessary instructions.
Please follow the instructions carefully

**NOTE: ALL TRANSACTIONS ARE NOT AUTO-COMMIT, SO PLEASE GOTO MAIN MENU AFTER TRANSACTION AND SELECT OPTION
      4 IN ORDER TO EFFECT THE TRANSACTION COMMIT SIMILAR TO DATABASE**

### 2. Delete a record

This fuctionality is similar like deleting a row based on field (column in database) and its value.
Once you select the option, program will ask you the field name to be sorted and select the record.
once you have given the field name and its value, this will delete the entry from all records.

**NOTE: ALL TRANSACTIONS ARE NOT AUTO-COMMIT, SO PLEASE GOTO MAIN MENU AFTER TRANSACTION AND SELECT OPTION
      4 IN ORDER TO EFFECT THE TRANSACTION COMMIT SIMILAR TO DATABASE**

### 3. Find record(s):

This functionality is used to select the record based on the condition provided similar to WHERE CLAUSE
in database. First program will ask about the field names and its values. After this, program will ask about
the condition based field name and its value similar to WHERE AGE='33'. note that you need to enter both
field name and value based on the instructions provided by program.

 Please follow the program instructions carefully to get better functionality from program. After taking the
 input program will display the content in table format on cosole

### 4. Save

This is used to perform COMMIT operation followed by Add a record and delete a record operations on selection based.
Note that this option must be selected in order to commit the transactions such as add and delete.

### 5. Quit

This is used to exit the program safely. This will automatically save the transactions if any pending then
exit the program.
