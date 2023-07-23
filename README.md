<div align="center">
<pre>
 __  __         _____  _                        
|  \/  | _   _ |_   _|(_) _ __ ___    ___  _ __ 
| |\/| || | | |  | |  | || '_ ` _ \  / _ \| '__|
| |  | || |_| |  | |  | || | | | | ||  __/| |   
|_|  |_| \__, |  |_|  |_||_| |_| |_| \___||_|   
         |___/                                  

</pre>

<pre>
 _  ____        _____  _  _         ____    __    
/ ||___ \   _  |___ / | || |    _  | ___|  / /_   
| |  __) | (_)   |_ \ | || |_  (_) |___ \ | '_ \  
| | / __/   _   ___) ||__   _|  _   ___) || (_) | 
|_||_____| (_) |____/    |_|   (_) |____/  \___/  
</pre>

<h1>MyTimer</h1>

<a href="https://badge.fury.io/py/mytimer"><img src="https://badge.fury.io/py/mytimer.svg" alt="PyPI version" height="18"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>

</div>	

----------
## Table of contents					
   * [Overview](https://github.com/sepandhaghighi/mytimer#overview)
   * [Installation](https://github.com/sepandhaghighi/mytimer#installation)
   * [Usage](https://github.com/sepandhaghighi/mytimer#usage)
   * [Issues & Bug Reports](https://github.com/sepandhaghighi/mytimer#issues--bug-reports)
   * [Contribution](https://github.com/sepandhaghighi/mytimer/blob/main/.github/CONTRIBUTING.md)
   * [References](https://github.com/sepandhaghighi/mytimer#references)
   * [Authors](https://github.com/sepandhaghighi/mytimer/blob/main/AUTHORS.md)
   * [License](https://github.com/sepandhaghighi/mytimer/blob/main/LICENSE)
   * [Show Your Support](https://github.com/sepandhaghighi/mytimer#show-your-support)
   * [Changelog](https://github.com/sepandhaghighi/mytimer/blob/main/CHANGELOG.md)
   * [Code of Conduct](https://github.com/sepandhaghighi/mytimer/blob/main/.github/CODE_OF_CONDUCT.md)			
				
## Overview						
Simple timer for your terminal!

<table>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/project/mytimer"><img src="http://pepy.tech/badge/mytimer"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/mytimer"><img src="https://img.shields.io/github/stars/sepandhaghighi/mytimer.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">main</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/mytimer/workflows/CI/badge.svg?branch=main"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/mytimer/workflows/CI/badge.svg?branch=dev"></td>
	</tr>
</table>


<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a href="https://www.codefactor.io/repository/github/sepandhaghighi/mytimer"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/mytimer/badge" alt="CodeFactor" /></a></td>
		<td align="center"><a href="https://www.codacy.com/gh/sepandhaghighi/mytimer/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/mytimer&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/1bf28500431a498998ac79891cd79cda"/></a></td>
		<td align="center"><a href="https://codebeat.co/projects/github-com-sepandhaghighi-mytimer-main"><img alt="codebeat badge" src="https://codebeat.co/badges/ae1c0ac1-9890-4149-b260-b1f3174ef520" /></a></td>
	</tr>
</table>


## Installation		

### Source Code
- Download [Version 0.7](https://github.com/sepandhaghighi/mytimer/archive/v0.7.zip) or [Latest Source ](https://github.com/sepandhaghighi/mytimer/archive/dev.zip)
- `pip install .`				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install mytimer==0.7`						


## Usage

⚠️ You can use `mytimer` or `python -m mytimer` to run this program

### Version

```console
mytimer --version
```

### Basic

⚠️ Press `Ctrl + C` to exit

```console
mytimer
```

### Time Limit

```console
mytimer --minute=7 --second=30
```

```console
mytimer --hour=2 --minute=20
```

### Timer Mode

⚠️ The default mode is `count-up`

```console
mytimer --minute=7 --second=30 --countdown
```	

```console
mytimer --minute=7 --second=30 --countup
```		

### Alarm

⚠️ This mode may not be supported on all systems

```console
mytimer --minute=7 --second=30 --countdown --alarm
```

### Tone

⚠️ The default tone is `1`

```console
mytimer --minute=7 --second=30 --countdown --alarm --tone=2
```
* [Tones List](https://github.com/sepandhaghighi/mytimer/blob/main/TONES.md)

### Face


```console
mytimer --minute=7 --second=30 --face=3
```
* [Faces List](https://github.com/sepandhaghighi/mytimer/blob/main/FACES.md)


### Program

```console
mytimer --program=black-tea
```
* [Programs List](https://github.com/sepandhaghighi/mytimer/blob/main/PROGRAMS.md)

### Message


```console
mytimer --minute=7 --second=30 --message="Test message"
```
		

<div align="center">

<img src="https://github.com/sepandhaghighi/mytimer/raw/main/otherfiles/help.gif">
<p>Screen Record</p>

</div>


## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!

- Please complete the issue template
 			

## References

<blockquote>1- <a href="https://mixkit.co/free-sound-effects/alarm/">Mixkit Free Alarm Sound Effects</a></blockquote>

<blockquote>2- <a href="https://www.online-timers.com/">Online Timer</a></blockquote>

<blockquote>3- <a href="https://www.mediacollege.com/">Media College</a></blockquote>


## Show your support
								
<h3>Star this repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to our project</h3>	

<h4>Bitcoin</h4>
1KtNLEEeUbTEK9PdN6Ya3ZAKXaqoKUuxCy
<h4>Ethereum</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Litecoin</h4>
Ldnz5gMcEeV8BAdsyf8FstWDC6uyYR6pgZ
<h4>Doge</h4>
DDUnKpFQbBqLpFVZ9DfuVysBdr249HxVDh
<h4>Tron</h4>
TCZxzPZLcJHr2qR3uPUB1tXB6L3FDSSAx7
<h4>Ripple</h4>
rN7ZuRG7HDGHR5nof8nu5LrsbmSB61V1qq
<h4>Binance Coin</h4>
bnb1zglwcf0ac3d0s2f6ck5kgwvcru4tlctt4p5qef
<h4>Tether</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Dash</h4>
Xd3Yn2qZJ7VE8nbKw2fS98aLxR5M6WUU3s
<h4>Stellar</h4>		
GALPOLPISRHIYHLQER2TLJRGUSZH52RYDK6C3HIU4PSMNAV65Q36EGNL
<h4>Zilliqa</h4>
zil1knmz8zj88cf0exr2ry7nav9elehxfcgqu3c5e5
<h4>Coffeete</h4>
<a href="http://www.coffeete.ir/opensource">
<img src="http://www.coffeete.ir/images/buttons/lemonchiffon.png" style="width:260px;" />
</a>

