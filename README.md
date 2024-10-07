<div align="center">
<img src="https://github.com/sepandhaghighi/mytimer/raw/main/otherfiles/logo.png" width="500">
<h1>MyTimer: A Geeky Timer for Terminal Enthusiasts</h1>
<br/>
<a href="https://badge.fury.io/py/mytimer"><img src="https://badge.fury.io/py/mytimer.svg" alt="PyPI version" height="18"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
</div>			
				
## Overview	

<p align="justify">					
<strong>MyTimer</strong> is a Python project that aims to provide a simple yet efficient timer for terminal users, particularly targeting the geek community. This project allows users to set timers directly from their command line interface, making it convenient for those who spend a significant amount of time working in the terminal!

The main objective of <strong>MyTimer</strong> is to offer a minimalistic and distraction-free timer experience. It provides a clean and straightforward interface, ensuring that users can focus solely on tracking time without any unnecessary clutter or distractions.
</p>

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
		<td align="center"><img src="https://github.com/sepandhaghighi/mytimer/actions/workflows/test.yml/badge.svg?branch=main"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/mytimer/actions/workflows/test.yml/badge.svg?branch=dev"></td>
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
- Download [Version 1.7](https://github.com/sepandhaghighi/mytimer/archive/v1.7.zip) or [Latest Source](https://github.com/sepandhaghighi/mytimer/archive/dev.zip)
- `pip install .`				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install mytimer==1.7`						


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

⚠️ The default mode is `countdown`

```console
mytimer --minute=7 --second=30 --countdown
```	

```console
mytimer --minute=7 --second=30 --countup
```	

### Repeat

⚠️ The default value is `1`

```console
mytimer --repeat=3 --second=4
```
* Use `--repeat=-1` for infinite loop

### Alarm

⚠️ This mode may not be supported on all systems

```console
mytimer --minute=7 --second=30 --alarm
```

### Alarm Repeat

⚠️ The default value is `1`

```console
mytimer --minute=7 --second=30 --alarm --alarm-repeat=5
```

### Tone

⚠️ The default tone is `1`

```console
mytimer --minute=7 --second=30 --alarm --tone=2
```
* [Tones List](https://github.com/sepandhaghighi/mytimer/blob/main/TONES.md)

### Face


```console
mytimer --minute=7 --second=30 --face=3
```
* [Faces List](https://github.com/sepandhaghighi/mytimer/blob/main/FACES.md)
* `mytimer --faces-list`


### Vertical/Horizontal Shift

⚠️ The vertical and horizontal shift both have default values of `0`

```console
mytimer --v-shift=20 --h-shift=30
```

### Timer Sign

⚠️ Valid choices: [`""`, `"+"`, `"-"`]

```console
mytimer --sign="+"
```

### Keep on

In this mode, the timer will continue running after it times out

```console
mytimer --minute=5 --keep-on
```

### Set on

⚠️ Local time

In this mode, the timer sets on the given time. For example, here we set a timer for `15:05`.

```console
mytimer --hour=15 --minute=5 --set-on
```

### Program

```console
mytimer --program=black-tea
```
* [Programs List](https://github.com/sepandhaghighi/mytimer/blob/main/PROGRAMS.md)
* `mytimer --programs-list`

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

<blockquote>4- <a href="https://en.wikipedia.org/wiki/Pomodoro_Technique">Pomodoro Technique</a></blockquote>

<blockquote>5- <a href="https://www.themuse.com/advice/the-rule-of-52-and-17-its-random-but-it-ups-your-productivity">The Rule of 52 and 17: It's Random, But it Ups Your Productivity</a></blockquote>

<blockquote>6- <a href="https://desktime.com/blog/productivity-research">Desktime’s Productivity Research: An Overview of Our Finds Throughout the Years</a></blockquote>

<blockquote>7- <a href="https://ankushkun.github.io/animedoro-timer/Animedoro/">AnimeDoro Timer</a></blockquote>

<blockquote>8- <a href="https://worldteadirectory.com/know-tea-guide-tea-steeping-time/">Know Your Tea: Your Guide to Tea Steeping Time</a></blockquote>

<blockquote>9- <a href="https://artfultea.com/blogs/101/loose-leaf-tea-steep-time">How Long to Steep Tea: A Complete Guide</a></blockquote>

<blockquote>10- <a href="https://majestycoffee.com/blogs/posts/how-long-to-steep">How Long to Steep French Press: Mastering the Perfect Brew</a></blockquote>

<blockquote>11- <a href="https://freesound.org">Freesound</a></blockquote>


## Show Your Support
								
<h3>Star This Repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to Our Project</h3>	

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

