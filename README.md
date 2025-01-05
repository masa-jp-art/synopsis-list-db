# 概要
- このプロジェクトでは、OpenAI o1 proが出力した登場人物の設定、鑑賞者の体験するカタルシスのタイプ、プロットタイプの分類データからデータベースを作り、ランダムに取り出して物語の設定資料のアイデアを作ります。
- このプロジェクトは、ChatGPT Proで使用できる、OpenAIのo1 pro modeの検証を兼ねています

# 手順
- ChatGPT Proのo1 pro modeに、物語のキャラクタータイプを生成させます
  - [character-type-protagonist-1.md](https://github.com/masa-jp-art/character-type-db/blob/main/character-type-protagonist-1.md)
  - [character-type-protagonist-2.md](https://github.com/masa-jp-art/character-type-db/blob/main/character-type-protagonist-2.md)
  - [Character-type-SubCharacter.md](https://github.com/masa-jp-art/character-type-db/blob/main/Character-type-SubCharacter.md)
  - [Character-type-antagonist.md](https://github.com/masa-jp-art/character-type-db/blob/main/Character-type-antagonist.md)
- ChatGPT Proのo1 pro modeに、「鑑賞者が体験するカタルシス」を分類させます
  - [catharsis-type.md](https://github.com/masa-jp-art/catharsis-type-db/blob/main/catharsis-type.md)
- ChatGPT Proのo1 pro modeに、物語のプロットを分類させます
  - [prot-type.md](https://github.com/masa-jp-art/prot-type-db/blob/main/prot-type.md)
- 出力された分類をスプレッドシートに転記してデータベースを作ります
  - [20250104-synopsis-list-snapshot](https://docs.google.com/spreadsheets/d/1qx4aUV2JA5RszAm4ghgAnzcDY3JY6dv5f7dpCJJ2lD8/edit)
- Google colabでプログラムを動かし、物語の設定を出力させます
  - https://github.com/masa-jp-art/synopsis-list-db/blob/main/cord-for-google-colab.py
 
# 関連
- [OpenAI o1 pro mode検証：o1 proが出力したアイデアを組み合わせて小説やシナリオを出力させられるか](https://note.com/msfmnkns/n/nc2e69de0ca26)
