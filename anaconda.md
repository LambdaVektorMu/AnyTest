# Pythonの環境構築
Miniconda（CLIで操作するAnaconda）
https://docs.conda.io/en/latest/miniconda.html

$ wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh
anaconda設定
Conda環境が自動的に有効にならないように設定する場合
$ conda config --set auto_activate_base false
有効化
$ conda activate
無効化
$ conda deactivate
コマンドなどで必要なパッケージを検索
$ conda search
インストール
$ conda install
環境構築
$ conda create --name py36 python=3.6