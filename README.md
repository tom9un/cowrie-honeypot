# cowrie-honeypot
**Instalasi cowrie di ubuntu 12.04 server x64**

1. Buat VM dari iso ubuntu 12.04 server;

2. Setelah selesai instalasi os, jalankan update sbb :
    
*       sudo apt-get update
        sudo apt-get install -f
        sudo rm -rf /var/lib/apt/lists/*
        sudo apt-get update
        sudo apt-get upgrade
        sudo apt-get dist-upgrade
        sudo apt-get autoremove

3. Install depedencies sbb :
    
*       sudo apt-get install git python-virtualenv libssl-dev libffi-dev build-essential python3-minimal authbind

4. Install Python3.6.3 sbb :

*       wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
        tar -xvf Python-3.6.3.tgz
        cd Python-3.6.3
        sudo ./configure --enable-optimizations
        sudo make -j8
        sudo make install
        
5. Instalasi Virtual Environment sbb :

*       sudo pip3 install virtualenv

6. Buar user account yang non-root dan akses ke account tersebut sbb :

*       sudo adduser --disabled-password cowrie
        sudo su - cowrie
        
7. Cloning source code cowrie pada account tersebut :

*       git clone https://github.com/tom9un/cowrie-honeypot.git  cowrie
        
8. Buat Virtual Environment :

*       cd cowrie/
        virtualenv --python=python3 cowrie-env
        source cowrie-env/bin/activate
        pip install --upgrade pip
        pip install --upgrade -r requirements.txt
        
9. Setting Configurasi (standar) :

*       cd ./etc/
        cp cowrie.cfg.dist cowrie.cfg
        nano cowrie.cfg
        
    *   cari Telnet Specific Options dan rubah enable menjadi true :

    <img width="695" alt="Screen Shot 2020-04-07 at 16 35 15" src="https://user-images.githubusercontent.com/33028642/78693598-ac519500-7925-11ea-9fce-7ce1135b50f1.png">
    
    *   rubah hostname, atau yang akan menjadi fake hostname saat attacker masuk ke ssh/telnet :
    
    <img width="647" alt="Screen Shot 2020-04-07 at 16 34 41" src="https://user-images.githubusercontent.com/33028642/78693652-bffcfb80-7925-11ea-9533-b822111b3c56.png">
        
10. Memulai cowrie :

*       cd ..
        bin/cowrie start

    *   ssh jalan di port 2222 dan telnet jalan di port 2223, cek dengan :

*       netstat -an

    <img width="801" alt="Screen Shot 2020-04-07 at 16 30 12" src="https://user-images.githubusercontent.com/33028642/78693703-d440f880-7925-11ea-8b2b-5b575b0ab754.png">

    *   Simulasi akses SHH dan Telnet :
   
    <img width="569" alt="Screen Shot 2020-04-07 at 16 32 52" src="https://user-images.githubusercontent.com/33028642/78693770-eb7fe600-7925-11ea-8686-0d83289d932a.png">
    <img width="571" alt="Screen Shot 2020-04-07 at 16 31 20" src="https://user-images.githubusercontent.com/33028642/78693805-f6d31180-7925-11ea-86ee-410da07477c5.png">
        
   
11. Menjalankan saat startup menggunakan supervisord :

*       exit
        sudo pip3 install supervisor
        cd /home/cowrie/cowrie/supervisord
        sudo ./install.sh
        
    *   Buat file configurasi dengan nama cowrie.conf sbb :
    
*       sudo nano /etc/supervisor/conf.d/cowrie.conf

    *   Dengan isi sbb :
    
*       [program:cowrie]
        command=/home/cowrie/cowrie/bin/cowrie start
        directory=/home/cowrie/cowrie/
        user=cowrie
        autorestart=true
        redirect_stderr=true
        
    *   Update cowrie script pada :
    
*       sudo nano /bin/cowrie

    *   Rubah DAEMONIZE="" menjadi DAEMONIZE="-n"
    
    *   Jalankan service supervisord dengan :
    
*       sudo service supervisord force-reload

12. Instalasi standar selesai.

        ** Please read for optional n modification  ==>  cowrie-2020.pdf **

