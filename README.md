# complementary-pair


**Objective: To find a complementary pair on the 5' end between two RNA libraries**

---

Version1_4  
This program compares the 9th-1st base from the 5' end of library_1 with the 2nd-10th base from the 5' end of library_2, and find a pair that is fully complementary. A wobble base-pair "G-U" is also considered to be complementary. The number of GU pair in that region is also output.

---

**How to use**

Download complementary_analysis.py

Prepare the two RNA libraries to be compared in fasta format. Use uppercase letters for nucleotides and exclude any headers.

Place the program and the two RNA library data in the same folder.

In that folder, open a terminal and execute as in the following example.

python complementary_analysis.py library_1.fasta library_2.fasta
