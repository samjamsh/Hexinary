# Hexinary
Hex Visualizar and editor, this program allows you to view binary files bytes in hex and also edit them



Hexadecimal Viewer - README

Descrição:
-----------
Programa para visualizar arquivos em formato hexadecimal, mostrando também os caracteres ASCII.

Uso básico:
-----------
No terminal, rode:

    python3 hexviewer.py nome_do_arquivo

Opções comuns:
--------------
- -O <arquivo>       Salvar saída em arquivo
- -ho               Ocultar coluna de offset
- -ha               Ocultar caracteres ASCII
- -hb               Ocultar offset e ASCII, só hex
- -offset <tipo>     Formato do offset: dec, hex, oct, bin (padrão: dec)
- -bl <número>       Bytes por linha (padrão: 16)
- -io <número>       Offset inicial (posição do byte)
- -fo <número>       Offset final
- --help             Mostrar ajuda
- --version          Mostrar versão

Exemplo simples:
----------------
    python3 hexviewer.py arquivo.bin

Licença:
--------
Apache License 2.0

Autor:
------
Sam Jamsh

---
