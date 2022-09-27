# complementary-pair


**Objective: To find a complementary pair on the 5' end between two RNA libraries**

---

Version1_4  
This program compares the 9th-1st base from the 5' end of library_1 with the 2nd-10th base from the 5' end of library_2, and find a pair that is fully complementary. A wobble base-pair "G-U" is also considered to be complementary. The number of GU pair in that region is also output.

---

**使い方**

complementary_analysis.py をダウンロード

2つの比べたいライブラリを用意する。　fasta形式で、ヘッダーは除く。大文字を使用する。

プログラムと2つのライブラリデータを同じフォルダに置く。

そのフォルダにて、ターミナルを開き、以下の例のように実行する。

python complementary_analysis.py library_1.fasta library_2.fasta
