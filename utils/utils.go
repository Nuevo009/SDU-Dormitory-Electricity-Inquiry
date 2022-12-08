package utils

import (
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net"
	"net/http"
	"net/url"
	"os"
)

type Telegram struct {
	BotToken string
	UserID   string
	APIHost  string
	Proxy    string
}

type RequestData struct {
	API     string
	Headers map[string]string
	UserXq  string
	UserFj  string
}

type Config struct {
	Telegram    Telegram
	RequestData RequestData
}

func LoadConfig(configPath string) (conf *Config) {

	file, err := os.Open(configPath)
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	decoder := json.NewDecoder(file)

	err = decoder.Decode(&conf)
	if err != nil {
		log.Fatal(err)
	}
	return
}
func checkProxyAddr(proxyAddr string) (u *url.URL, err error) {
	if proxyAddr == "" {
		return nil, errors.New("proxy addr is empty")
	}

	host, port, err := net.SplitHostPort(proxyAddr)
	if err == nil {
		u = &url.URL{
			Host: net.JoinHostPort(host, port),
		}
		return
	}

	u, err = url.Parse(proxyAddr)
	if err == nil {
		return
	}

	return
}

func (T *Telegram) SendMsg(text string) (err error) {
	params := url.Values{
		"chat_id": {T.UserID},
		"text":    {text},
	}

	posturl := fmt.Sprintf("https://%s/bot%s/sendMessage", T.APIHost, T.BotToken)

	client := http.Client{
		Transport: &http.Transport{
			Proxy: func(req *http.Request) (*url.URL, error) {
				u, err := checkProxyAddr(T.Proxy)
				if err != nil {
					return http.ProxyFromEnvironment(req)
				}

				return u, err
			},
		},
	}
	resp, err := client.PostForm(posturl, params)
	if err != nil {
		return
	}
	if resp.StatusCode != 200 {
		fmt.Printf("Telegram Bot 推送失败\n")
	} else {
		fmt.Printf("Telegram Bot 推送成功\n")
	}
	return
}
func (R *RequestData) GetMsg() (msg string, err error) {
	params := url.Values{
		"userFj": {R.UserFj},
		"userXq": {R.UserXq},
	}
	Url, _ := url.Parse(R.API)
	Url.RawQuery = params.Encode()
	urlPath := Url.String()
	client := &http.Client{}

	req, _ := http.NewRequest("POST", urlPath, nil)
	for k, v := range R.Headers {
		req.Header.Set(k, v)
	}

	resp, err := client.Do(req)
	if err != nil {
		return
	}
	defer resp.Body.Close()

	decoder := json.NewDecoder(resp.Body)

	var res struct {
		Success bool `json:"success"`
		Message struct {
			FeeElec  float64 `json:"feeElec,string"`
			NegElec  float64 `json:"negElec,string"`
			Status   string  `json:"status"`
			FreeElec float64 `json:"freeElec,string"`
			PlusElec float64 `json:"plusElec,string"`
			Room     string  `json:"room"`
		} `json:"message"`
	}
	err = decoder.Decode(&res)
	if err != nil {
		return
	}

	status := res.Message.Status
	elec := res.Message.PlusElec
	if status == "获取数据异常" {
		msg = status
		fmt.Println(status)
		return
	} else if elec < 10.0 {
		fmt.Println(elec)
		msg = fmt.Sprintf("您的电量不足 10 度，当前电量为 %.2f 度，请及时充电！", elec)
	} else {
		msg = fmt.Sprintf("您的电量为 %.2f 度，请放心使用！", elec)
	}
	return

}
