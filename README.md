### 启一个新环境
conda create --name lemon_mastodon_bot python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/


### 激活环境

 conda activate lemon_mastodon_bot


### 类库地址

https://github.com/halcy/Mastodon.py


### 安装依赖

pip3 install Mastodon.py

pip3 install BeautifulSoup4

pip3 install requests

### Hello World


### 在全新机器上安装
	mkdir ~/.venvs
	mkdir ~/.venvs/lemon_mastodon_bot
	python3 -m venv ~/.venvs/lemon_mastodon_bot
	source ~/.venvs/lemon_mastodon_bot/bin/activate

	mkdir lemon_mastodon_bot


### 推送到到本地的gitea上去

	# 设置http:
	git config --global http.proxy http://127.0.0.1:1080
	# 设置https:
	git config --global https.proxy https://127.0.0.1:1080
	# 设置socks:
	git config --global http.proxy 'socks5://127.0.0.1:1080'
	git config --global https.proxy 'socks5://127.0.0.1:1080'
	## 取消
	git config --global --unset http.proxy
	git config --global --unset https.proxy
	————————————————
	版权声明：本文为CSDN博主「sunpro518」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
	原文链接：https://blog.csdn.net/sunjinshengli/article/details/108862226

先unset掉不太好的代理

然后 按照提示push 咯

### 正常地址

	api_base_url = 'https://cmx-im.work/'

### 开始部署

	sudo docker run -it lemonhall/mask_chatpic bash

	dnf update

	mkdir ~/.venvs
	mkdir ~/.venvs/lemon_mastodon_bot
	python3 -m venv ~/.venvs/lemon_mastodon_bot
	source ~/.venvs/lemon_mastodon_bot/bin/activate

	cd ~

	git clone http://git.lemonhall.me/lemonhall/lemon_mastodon_bot.git

	cd lemon_mastodon_bot/

	pip3 install Mastodon.py
	pip3 install BeautifulSoup4
	pip3 install requests

### 新建一个文件
	#!/bin/bash

	# For dhclient/dhclient-script debugging.
	# Copy this into /etc/dhcp/ and make it executable.
	# Run 'dhclient -d <interface>' to see info passed from dhclient to dhclient-script.
	# See also HOOKS section in dhclient-script(8) man page.

	cd /root/lemon_mastodon_bot
	source ~/.venvs/lemon_mastodon_bot/bin/activate
	python guancha.py

### 安装
	#https://www.baeldung.com/ops/docker-cron-job
	dnf install cronie
	crontab -e
	*/1 * * * * /root/lemon_mastodon_bot/entry.sh


### 
### 试试

	sudo docker ps

	sudo docker commit -m "lemon_mastodon_bot" -a "lemonhall" 622024b0e18e lemonhall/lemon_mastodon_bot

	sudo docker login

	sudo docker push lemonhall/lemon_mastodon_bot

	sudo docker run -it lemonhall/mask_chatpic bash

### 
https://stackoverflow.com/questions/37458287/how-to-run-a-cron-job-inside-a-docker-container

docker-compose.yml

services:
    tasker:
        image: strm/tasker
        volumes:
            - "/var/run/docker.sock:/var/run/docker.sock"
        environment:
            configuration: |
                logging:
                    level:
                        ROOT: WARN
                        org.springframework.web: WARN
                        sh.strm: DEBUG
                schedule:
                    - every: minute
                      task: lemon_mastodon_bot

                tasks:
                    docker:
                        - name: lemon_mastodon_bot
                          image: lemonhall/lemon_mastodon_bot
                          script:
                              - /root/lemon_mastodon_bot/entry.sh

sudo docker-compose up


###

	sudo docker run -it --rm -v /home/lemongall/ lemonhall/lemon_mastodon_bot bash -c 'cd /root/lemon_mastodon_bot;source ~/.venvs/lemon_mastodon_bot/bin/activate;python guancha.py' 