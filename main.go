package main

import (
	"flag"
	"log"
	"time"

	"github.com/Nuevo009/SDU-Dormitory-Electricity-Inquiry/utils"
)

func main() {
	var configPath string
	flag.StringVar(&configPath, "c", "config/config.json", "config.json 的路径")
	flag.Parse()
	conf := utils.LoadConfig(configPath)
	count, maxRetries, sleepSeconds := 0, 5, 5
	var msg string
	var err error
	for count < maxRetries {
		msg, err = conf.RequestData.GetMsg()
		if err != nil || msg == "获取数据异常" {
			count++
			time.Sleep(time.Duration(sleepSeconds))
		} else {
			break
		}
	}
	if count == maxRetries {
		conf.Telegram.SendMsg("异常")
		log.Fatal(err)
	} else {
		err = conf.Telegram.SendMsg(msg)
		if err != nil {
			log.Fatal(err)
		}
	}

}
