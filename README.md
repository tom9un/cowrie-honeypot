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
        
7. Cloning source code cowrie di account tersebut :

*       git clone http://153.92.4.68:4445/tomy.gunawan/cowrie-honeypot/  cowrie
        
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

    ![Screen_Shot_2020-04-07_at_16.35.15](/uploads/5f3ecef8a5a5c24972af4e28f1a2479e/Screen_Shot_2020-04-07_at_16.35.15.png)
    
    *   rubah hostname, atau yang akan menjadi fake hostname saat attacker masuk ke ssh/telnet :
    
    ![Screen_Shot_2020-04-07_at_16.34.41](/uploads/2eeddcc2a739c93565fbcc3b846fab1e/Screen_Shot_2020-04-07_at_16.34.41.png)
        
10. Memulai cowrie :

*       cd ..
        bin/cowrie start

    *   ssh jalan di port 2222 dan telnet jalan di port 2223, cek dengan :

*       netstat -an

    ![Screen_Shot_2020-04-07_at_16.30.12](/uploads/828e9925a7384334be270d3832123453/Screen_Shot_2020-04-07_at_16.30.12.png)

    *   Simulasi akses SHH dan Telnet :
   
    ![Screen_Shot_2020-04-07_at_16.32.52](/uploads/084791aead7c43bd5230928840e9c0a4/Screen_Shot_2020-04-07_at_16.32.52.png)
    ![Screen_Shot_2020-04-07_at_16.31.20](/uploads/286b29663f6fbe23c89bca8c9932a979/Screen_Shot_2020-04-07_at_16.31.20.png)
        
   
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

        **Please read for optional n modification ==>  https://cowrie.readthedocs.io/en/latest/INSTALL.html**

