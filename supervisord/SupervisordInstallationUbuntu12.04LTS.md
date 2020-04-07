# Supervisord Installation on Ubutnu 12.04 LTS

There are a [number of solutions](http://serverfault.com/questions/96499/how-to-automatically-start-supervisord-on-linux-ubuntu) for installing [supervisord](http://supervisord.org/running.html) and automatically running it on Ubuntu - this is what worked for me (on multiple installations...).

## Installation

### Quick & Easy

```bash
sudo bash < <(curl https://gist.githubusercontent.com/alexhayes/814fd0d0f7020e918a95/raw/full-install.sh)
```

### Longer, But Still Easy

Firstly, we need to install requirements;

```bash
apt-get install python-dev git-core
```

Then, install supervisor, my preferred approach (and the approach that works with the `install.sh` below) is as follows;

```bash
sudo pip install supervisor
```

Then clone this Gist and run it's "installer";

```bash
git clone https://gist.github.com/814fd0d0f7020e918a95.git
cd 814fd0d0f7020e918a95
sudo ./install.sh
```


## Creating programs

Place your [supervisor program configurations](http://supervisord.org/running.html#adding-a-program) in `/etc/supervisor/conf.d/myprogram.conf`.

## Start supervisord

```bash
sudo service supervisord start
```

# Authors

- [Alex Hayes](http://github.com/alexhayes)
- [Dan Mackinlay](http://github.com/howthebodyworks) for the init.d script in [this gist](https://gist.github.com/howthebodyworks/176149) discovered at [serverfault](http://serverfault.com/a/96500)

