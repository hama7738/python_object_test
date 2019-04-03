以下のように、ファイル名を指定して、commandを実行してください
python test.py --input_file='ファイル名'

# FizzBuzz問題

## 内容

- FizzBuzzというプログラムは、3の倍数が入力されると”Fizz”を出力し、5の倍数が入力されると”Buzz”を出力し、3の倍数でも5の倍数でもある数が入力されると”FizzBuzz”を出力します
- FizzBuzzの拡張として、複数の(整数i, 文字列s)のペアと一つの整数mが渡され、mがiの倍数ならsを出力するプログラムを作成しなさい
- sはiの小さい順に出力してください(※iが小さい順に並んでいるとは限りません)
- どのsも出力されなければmを出力してください
- iとsのペアは"input.txt"に一行ずつ「i:s」形式で渡されます
- mは"input.txt"の下から２番目の行で渡されます
- "input.txt"の最終行は空行です
- 解答のコードはtest.pyに書いてください
- 解答を任意のgitレポジトリにプッシュし、そのurlを提出してください（githubでもかまいません）

## 入力例と出力例

### 例1

入力

```txt:input.txt
5:buzz
3:fizz
8:hoge
2:huga
24

```

出力

hugafizzhoge

### 例2

入力

```txt:input.txt
3:yoshida
5:takuma
2

```

出力

2
