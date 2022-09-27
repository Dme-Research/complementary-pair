# complementary-pair


**Objective: To find a complementary pair on the 5' end between two RNA libraries**

---
Version1_4  
This program compares the 9th-1st base from the 5' end of library_1 with the 2nd-10th base from the 5' end of library_2, and find a pair that is fully complementary. A wobble base-pair "G-U" is also considered to be complementary. The number of GU pair is also output.


Version1_3  
Library_1 の5'末端側９〜１、９〜２、９〜3塩基と、 Library_2 の5'末端側２−１０、２〜９、２〜８塩基とを比べて、完全に相補的であるペアの数を出力。
ただし、GU、あるいはUGペアも相補的であるとする。GU、UGペアの数も出力する。


Version1_2  
相補ペアを見つける領域を変更した。Library_1の5'末端側２〜８、２〜９、２−１０塩基と、Library_2の5'末端側３〜９、２〜９、１〜９塩基と比べて、完全に相補的であるペアの数を出力。
ただし、GU、あるいはUGペアも相補的であるとする。GU、UGペアの数も出力する。


Version1_1  
出力ファイルが2つになりました。1つは、RNAペアのカウントデータ。もう1つは、library_1のSequence_IDと相補的なlibrary_2のSequence_ID。
library_1のIDカウントが10,000毎にメッセージが出力されます。カウントが10,000から20,000になるまでの時間から、終了までにかかる時間を推測できます。

---

**使い方**

complementary_analysis.py をダウンロード

2つの比べたいライブラリを用意する。　fasta形式で、ヘッダーは除く。大文字を使用する。

プログラムと2つのライブラリデータを同じフォルダに置く。

そのフォルダにて、ターミナルを開き、以下の例のように実行する。

python complementary_analysis.py library_1.fasta library_2.fasta
