#!/bin/bash

cd /home/lemonhall/lemon_mastodon_bot
source /home/lemonhall/.venvs/lemon_mastodon_bot/bin/activate

python guancha.py > log.txt
