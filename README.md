Bulk File Rename Tool: 
Sometimes, you need to name all the files in a directory according to certain conventions. For
example, you can rename all the files in a directory with File0001.jpg, where the numbers
increase based on the number of files in the directory. Doing this manually can be stressful
and repetitive.
The Bulk File Rename Tool allows users to rename a large number of files, without having to
manually rename files.
This saves users a lot of time. It spares them the trouble of having to do boring repetitive
work and make mistakes. With the Bulk File Rename Tool, users can rename files in a couple
of seconds without any mistakes.
Examples of Bulk File Rename Tools
Here are some implementations of the Bulk File Rename idea:
• Ren,
• Rename

Technical Details: 
The main objective of this project idea is to rename files. So, the application needs to find a
way to manipulate the target files. The os, sys, and shutil libraries will be useful for a large part
of this project.
Your users will be able to rename all the files in the directory, using naming conventions.
Therefore, they should be able to pass in the naming convention of choice. The regex module
will help match the required naming patterns, if you understand how regex works.
A user may want to pass in a naming convention such as myfiles as part of the commands and
expect that the tool renames all the files like myfilesXYZ, where XYZ is a number. They should
also be able to choose the directory where the files to be renamed are.

Extra Challenge(Optional): 
The major challenge in this project is to rename all the files in a directory. But users may
only need to name a certain number of files. You can implement a feature to allow users to
choose the number of files to be renamed, instead of all the files.
Also, instead of a script, you can build a file manager like UI to select the files.
Note that renaming only a certain number of files will require the tool to sort the files
based on alphabetical order, time of file creation, or file size, depending on the user’s
requirements.
