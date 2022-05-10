# complementary-pair
「目的」　

2つのライブラリ間で、5'末端側１０塩基の相補ペアを見つける

[version1_1]
出力ファイルが2つになりました。1つは、RNAペアのカウントデータ。もう1つは、library_1のSequence_IDと相補的なlibrary_2のSequence_ID。
library_1のIDカウントが10,000毎にメッセージが出力されます。カウントが10,000から20,000になるまでの時間から、終了までにかかる時間を推測できます。


「使い方」

complementary_analysis.py をダウンロード

2つの比べたいライブラリを用意する。　fasta形式で、ヘッダーは除く。大文字を使用する。

プログラムと2つのライブラリデータを同じフォルダに置く。

そのフォルダにて、ターミナルを開き、以下の例のように実行する。

python complementary_analysis.py library_1.fasta library_2.fasta
