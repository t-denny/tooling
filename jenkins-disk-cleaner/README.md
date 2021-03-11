# Disk Cleaner for Jenkins Executors

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Features

- Flexible cleanup by persentage disk usage
- Cleanup single or more disk per/mounting path. 

## Directory Structure
    .
    ├── clean_hj.sh             # Shell script to find & remove unused dir in path `/home/jenkins`.
    ├── clean_tmp.sh            # Shell script to find & remove unused dir in path `/tmp`.
    ├── main.go                 # Cron apps for executing script by percentage of disk usage.
    └── README.md

## How to use
Cleaner requires [go](https://golang.org/) to run.

```sh
go run main.go
```

## Maintain
```sh
17 |    CLEAN_WHEN = 80 //in percents
```
> Line 17 is for change persentage when clean app will running


```sh
20 |    var (
21 |        partition = map[string]string{
22 |    	    "/home/jenkins": "clean_hj.sh",
23 |   	        "/tmp": "clean_tmp.sh",
24 |        }
25 |    )
```
> Define mount path of disk (line 22) and script name to run. It can be define a lot.

```sh
73 |    s.Every(5).Minute().Do(CleanUp)
```
> Line 73 for change cron time checker running, on the example above it will run checking every 5 minutes.

Highfive
