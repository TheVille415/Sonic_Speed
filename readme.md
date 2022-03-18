# Playing Sonic with AI <img src="https://c.tenor.com/qdwKeropqtsAAAAC/sonic-sonic-the-hedgehog.gif" width="50px">

Since Gym and Retro Gym run only on some version of python we need to make sure we have the proper version of python.

The easist way to do this is to install annoconda and make a virtual enviornment.

Running this command will make sure you are running the correct version of python.

```
$ conda create --name gym36 python=3.6 
```

Activating the enviornment 

```
$ conda activate gym36 
```

In order to get this project running you first need to install the dependencies:

```
$ pip install -r requirements.txt
```

The next step is to find your LEGAL copy of Sonic the Hedgehog.

You will need to make sure your rom is placed in the correct folder for your game. In my case once retro is installed it will be located in 

```
$ [your hard drive] retro/retro/data/stable/SonicTheHedgehog-Genesis
```

Once you have your copy of Sonic the Hedgehog you can run the sonic.py file.

```
$ python sonic.py
```


For informaiton on this or guidance check out these resources here:
[Open AI Getting Started](https://retro.readthedocs.io/en/latest/getting_started.html)
[Open AI Retro Github](https://github.com/openai/retro)
[Sonic Steam Link](https://store.steampowered.com/app/71113/Sonic_The_Hedgehog/)

